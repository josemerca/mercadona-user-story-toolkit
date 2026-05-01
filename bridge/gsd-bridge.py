#!/usr/bin/env python3
"""
gsd-bridge — Mantiene consistencia entre artefactos GSD (.planning/) y el trabajo
ejecutado por Superpowers (o cualquier ejecutor).

Subcomandos:
  sync       Detecta cambios desde last-sync, marca REQ-IDs done en PLAN.md,
             actualiza STATE.md, y avanza ROADMAP.md si fase completa.
  mark-done  Marca explícitamente uno o más REQ-IDs como done.
  amend      Registra un SPEC-AMENDMENT cuando la implementación divergió del diseño.
  status     Reporta divergencia entre realidad (commits) y artefactos GSD.

Uso:
  gsd-bridge sync [--planning .planning/] [--quiet] [--dry-run]
  gsd-bridge mark-done REQ-01 REQ-02 ... [--planning .planning/]
  gsd-bridge amend "<reason>" [--phase N] [--planning .planning/]
  gsd-bridge status [--planning .planning/]

Diseñado para invocarse:
  - Manualmente por el ejecutor (PM o desarrollador)
  - Como Stop hook de Claude Code (sync --quiet --auto)
  - Como step en CI tras merge a main

Filosofía:
  - Read-mostly sobre `.planning/` (solo escribe en STATE/PLAN/ROADMAP/VERIFICATION/AMENDMENTS)
  - Nunca reescribe SPEC.md (preserva trail con SPEC-AMENDMENTS.md)
  - Idempotente: ejecutar dos veces no duplica entradas
  - Honesto: si no puede determinar el estado, lo reporta como "unknown"
"""

import argparse
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional


REQ_ID_PATTERN = re.compile(r'\b([A-Z]{2,8}-\d{1,4})\b')
PHASE_DIR_PATTERN = re.compile(r'^(\d+)(?:-.*)?$')


class GsdBridge:
    def __init__(self, planning_dir: Path, quiet: bool = False, dry_run: bool = False):
        self.planning = planning_dir
        self.quiet = quiet
        self.dry_run = dry_run
        self._validate()

    def _validate(self):
        if not self.planning.exists():
            raise FileNotFoundError(f"Directorio GSD no encontrado: {self.planning}")
        for required in ("PROJECT.md", "REQUIREMENTS.md", "ROADMAP.md"):
            if not (self.planning / required).exists():
                raise FileNotFoundError(f"Artefacto requerido faltante: {required}")

    def log(self, msg: str):
        if not self.quiet:
            print(msg)

    def _run_git(self, *args: str) -> str:
        try:
            result = subprocess.run(
                ["git", *args],
                cwd=self.planning.parent,
                capture_output=True,
                text=True,
                check=True,
            )
            return result.stdout.strip()
        except (subprocess.CalledProcessError, FileNotFoundError):
            return ""

    def _last_sync_sha(self) -> Optional[str]:
        state = self.planning / "STATE.md"
        if not state.exists():
            return None
        for line in state.read_text(encoding="utf-8").splitlines():
            m = re.match(r"\*\*last-sync-sha:\*\*\s*(\w+)", line.strip(), re.IGNORECASE)
            if m:
                return m.group(1)
        return None

    def _current_sha(self) -> str:
        return self._run_git("rev-parse", "HEAD") or "unknown"

    def _commits_since(self, since_sha: Optional[str]) -> list[dict]:
        if since_sha and since_sha != "unknown":
            log_range = f"{since_sha}..HEAD"
        else:
            log_range = "HEAD"
        log_output = self._run_git(
            "log", log_range, "--no-merges", "--pretty=format:%H|%s|%b<<COMMIT-END>>"
        )
        if not log_output:
            return []
        commits = []
        for raw in log_output.split("<<COMMIT-END>>"):
            raw = raw.strip()
            if not raw:
                continue
            parts = raw.split("|", 2)
            if len(parts) < 2:
                continue
            sha, subject = parts[0], parts[1]
            body = parts[2] if len(parts) > 2 else ""
            commits.append({"sha": sha, "subject": subject, "body": body})
        return commits

    def _extract_req_ids(self, text: str) -> set[str]:
        return set(REQ_ID_PATTERN.findall(text))

    def _phase_dirs(self) -> list[Path]:
        phases_root = self.planning / "phases"
        if not phases_root.exists():
            return []
        dirs = []
        for child in phases_root.iterdir():
            if child.is_dir() and PHASE_DIR_PATTERN.match(child.name):
                dirs.append(child)
        return sorted(dirs, key=lambda p: int(PHASE_DIR_PATTERN.match(p.name).group(1)))

    def _find_req_in_plans(self, req_id: str) -> list[Path]:
        hits = []
        for phase_dir in self._phase_dirs():
            for plan_file in phase_dir.glob("*PLAN.md"):
                content = plan_file.read_text(encoding="utf-8")
                if req_id in content:
                    hits.append(plan_file)
        # also check root REQUIREMENTS.md
        return hits

    def _mark_req_done_in_file(self, file: Path, req_id: str) -> bool:
        content = file.read_text(encoding="utf-8")
        # find line `- [ ] **REQ-ID**` and replace with `- [x] **REQ-ID**`
        pattern = re.compile(
            rf"^(\s*)- \[ \](\s+\*\*{re.escape(req_id)}\*\*)",
            re.MULTILINE,
        )
        new_content, n = pattern.subn(r"\1- [x]\2", content)
        if n > 0 and not self.dry_run:
            file.write_text(new_content, encoding="utf-8")
        return n > 0

    def _all_reqs_done_in_phase(self, phase_dir: Path) -> bool:
        # phase complete only if at least one done REQ AND no pending REQs
        has_done = False
        for plan_file in phase_dir.glob("*PLAN.md"):
            content = plan_file.read_text(encoding="utf-8")
            if re.search(r"^\s*- \[ \]\s+\*\*[A-Z]{2,8}-\d{1,4}\*\*", content, re.MULTILINE):
                return False
            if re.search(r"^\s*- \[x\]\s+\*\*[A-Z]{2,8}-\d{1,4}\*\*", content, re.MULTILINE):
                has_done = True
        return has_done

    def _mark_phase_complete_in_roadmap(self, phase_num: int) -> bool:
        roadmap = self.planning / "ROADMAP.md"
        content = roadmap.read_text(encoding="utf-8")
        # `- [ ] **Phase N: ` → `- [x] **Phase N: `
        pattern = re.compile(
            rf"^(\s*)- \[ \](\s+\*\*Phase {phase_num}:)",
            re.MULTILINE,
        )
        new_content, n = pattern.subn(r"\1- [x]\2", content)
        # also update progress table row
        # | N. Name | X/Y | Not started | - |  → | N. Name | Y/Y | Complete | <date> |
        date_str = datetime.now().strftime("%Y-%m-%d")
        progress_pattern = re.compile(
            rf"^(\|\s*{phase_num}\..*?\|)\s*\d+/(\d+)\s*\|\s*(?:Not started|In progress)\s*\|\s*-?\s*\|",
            re.MULTILINE,
        )
        new_content, m = progress_pattern.subn(
            rf"\1 \2/\2 | Complete | {date_str} |",
            new_content,
        )
        if (n > 0 or m > 0) and not self.dry_run:
            roadmap.write_text(new_content, encoding="utf-8")
        return n > 0 or m > 0

    def _all_reqs_in_phase(self, phase_dir: Path) -> list[str]:
        reqs = set()
        for plan_file in phase_dir.glob("*PLAN.md"):
            content = plan_file.read_text(encoding="utf-8")
            for m in re.finditer(r"^\s*- \[[ x]\]\s+\*\*([A-Z]{2,8}-\d{1,4})\*\*", content, re.MULTILINE):
                reqs.add(m.group(1))
        return sorted(reqs)

    def _write_verification(self, phase_dir: Path, completed_reqs: list[str]):
        all_reqs = self._all_reqs_in_phase(phase_dir)
        verify = phase_dir / "VERIFICATION.md"
        content = (
            f"# Verification — Phase {phase_dir.name}\n\n"
            f"**Verified:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
            f"**Source:** gsd-bridge auto-sync\n\n"
            "## Requirements completed\n\n"
        )
        for req in all_reqs:
            content += f"- [x] {req}\n"
        content += (
            "\n## Notes\n\n"
            "Generated by gsd-bridge based on git commits referencing each REQ-ID. "
            "Manual verification (test runs, acceptance walkthrough) recommended before considering the phase shipped.\n"
        )
        if not self.dry_run:
            verify.write_text(content, encoding="utf-8")

    def _update_state(self, summary: str, sha: str, completed_reqs: list[str]):
        state = self.planning / "STATE.md"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        new_block = (
            f"## gsd-bridge sync — {timestamp}\n\n"
            f"**last-sync-sha:** {sha}\n"
            f"**Requirements marked done this sync:** {', '.join(completed_reqs) if completed_reqs else 'none'}\n"
            f"**Summary:** {summary}\n\n"
        )
        if state.exists():
            existing = state.read_text(encoding="utf-8")
            content = new_block + existing
        else:
            content = (
                "# Project State\n\n"
                "Living memory of project progress. Updated by gsd-bridge after each sync.\n\n"
                + new_block
            )
        if not self.dry_run:
            state.write_text(content, encoding="utf-8")

    # --- public commands ---

    def cmd_sync(self):
        last_sha = self._last_sync_sha()
        current_sha = self._current_sha()
        if current_sha == "unknown":
            self.log("✗ No es un repositorio git (o git no disponible). Use mark-done manual.")
            return 1
        if last_sha == current_sha:
            self.log("✓ Sin cambios desde la última sincronización.")
            return 0

        commits = self._commits_since(last_sha)
        if not commits:
            self.log("✓ Sin commits nuevos.")
            return 0

        self.log(f"→ Procesando {len(commits)} commit(s) desde {last_sha or 'inicio'}…")

        marked: dict[str, list[Path]] = {}
        for commit in commits:
            text = f"{commit['subject']}\n{commit['body']}"
            for req_id in self._extract_req_ids(text):
                files = self._find_req_in_plans(req_id)
                for f in files:
                    if self._mark_req_done_in_file(f, req_id):
                        marked.setdefault(req_id, []).append(f)

        # detect phases now complete
        completed_phases: list[Path] = []
        for phase_dir in self._phase_dirs():
            if self._all_reqs_done_in_phase(phase_dir):
                phase_num = int(PHASE_DIR_PATTERN.match(phase_dir.name).group(1))
                if self._mark_phase_complete_in_roadmap(phase_num):
                    completed_phases.append(phase_dir)
                    reqs_in_phase = [
                        r for r, files in marked.items()
                        if any(phase_dir in f.parents for f in files)
                    ]
                    self._write_verification(phase_dir, reqs_in_phase)

        summary = f"{len(marked)} REQ(s) marcados, {len(completed_phases)} fase(s) completada(s)"
        self._update_state(summary, current_sha, list(marked.keys()))

        self.log(f"✓ Sync completado: {summary}")
        if marked:
            for req, files in marked.items():
                self.log(f"  - {req} done en {len(files)} fichero(s)")
        if completed_phases:
            for ph in completed_phases:
                self.log(f"  - Fase completada: {ph.name} → VERIFICATION.md generado")
        if self.dry_run:
            self.log("  (dry-run: sin escribir cambios)")
        return 0

    def cmd_mark_done(self, req_ids: list[str]):
        marked = []
        for req_id in req_ids:
            files = self._find_req_in_plans(req_id)
            if not files:
                self.log(f"⚠ {req_id} no encontrado en ningún PLAN.md")
                continue
            for f in files:
                if self._mark_req_done_in_file(f, req_id):
                    marked.append(req_id)
                    self.log(f"✓ {req_id} marcado en {f.relative_to(self.planning.parent)}")

        # check phase completion
        for phase_dir in self._phase_dirs():
            if self._all_reqs_done_in_phase(phase_dir):
                phase_num = int(PHASE_DIR_PATTERN.match(phase_dir.name).group(1))
                if self._mark_phase_complete_in_roadmap(phase_num):
                    self.log(f"✓ Fase {phase_num} completada → ROADMAP.md actualizado")
                    self._write_verification(phase_dir, marked)

        sha = self._current_sha()
        self._update_state(
            f"manual mark-done: {', '.join(req_ids)}",
            sha,
            marked,
        )
        return 0

    def cmd_amend(self, reason: str, phase: Optional[int]):
        if phase is None:
            # detect active phase from STATE or default to last
            dirs = self._phase_dirs()
            if not dirs:
                self.log("✗ No hay fases en .planning/phases/. Especifica --phase N.")
                return 1
            target_dir = dirs[-1]
        else:
            target_dir = next(
                (d for d in self._phase_dirs() if int(PHASE_DIR_PATTERN.match(d.name).group(1)) == phase),
                None,
            )
            if not target_dir:
                self.log(f"✗ Fase {phase} no encontrada.")
                return 1

        amendments = target_dir / "SPEC-AMENDMENTS.md"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        sha = self._current_sha()
        new_entry = (
            f"## Amendment — {timestamp}\n\n"
            f"**Commit:** {sha[:8] if sha != 'unknown' else 'no-git'}\n"
            f"**Reason:** {reason}\n\n"
        )
        if amendments.exists():
            content = amendments.read_text(encoding="utf-8") + "\n" + new_entry
        else:
            content = (
                f"# SPEC Amendments — Phase {target_dir.name}\n\n"
                "Diseño que cambió durante la implementación. Se anexan aquí en orden cronológico.\n"
                "El `SPEC.md` original NO se reescribe — preserva el trail.\n\n"
                + new_entry
            )
        if not self.dry_run:
            amendments.write_text(content, encoding="utf-8")
        self.log(f"✓ Amendment registrado en {amendments.relative_to(self.planning.parent)}")
        return 0

    def cmd_status(self):
        last_sha = self._last_sync_sha()
        current_sha = self._current_sha()
        commits_pending = self._commits_since(last_sha) if current_sha != "unknown" else []

        pending_reqs = set()
        if commits_pending:
            for c in commits_pending:
                pending_reqs.update(self._extract_req_ids(f"{c['subject']}\n{c['body']}"))

        phase_status = []
        for phase_dir in self._phase_dirs():
            todo = sum(
                1
                for f in phase_dir.glob("*PLAN.md")
                for line in f.read_text(encoding="utf-8").splitlines()
                if re.match(r"\s*- \[ \]\s+\*\*[A-Z]{2,8}-\d{1,4}\*\*", line)
            )
            done = sum(
                1
                for f in phase_dir.glob("*PLAN.md")
                for line in f.read_text(encoding="utf-8").splitlines()
                if re.match(r"\s*- \[x\]\s+\*\*[A-Z]{2,8}-\d{1,4}\*\*", line)
            )
            phase_status.append((phase_dir.name, done, todo))

        print(f"GSD Bridge Status — {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        print(f"Last sync sha:    {last_sha or 'never synced'}")
        print(f"Current sha:      {current_sha}")
        print(f"Commits pending:  {len(commits_pending)}")
        if pending_reqs:
            print(f"REQs in pending commits: {', '.join(sorted(pending_reqs))}")
        print()
        print("Phases:")
        for name, done, todo in phase_status:
            total = done + todo
            print(f"  {name}: {done}/{total} done")
        return 0


def main():
    parser = argparse.ArgumentParser(prog="gsd-bridge", description=__doc__.split("\n")[1])
    parser.add_argument("--planning", default=".planning/", help="Path al directorio GSD")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sync = sub.add_parser("sync", help="Auto-sync desde git commits")
    sync.add_argument("--quiet", action="store_true")
    sync.add_argument("--dry-run", action="store_true")

    md = sub.add_parser("mark-done", help="Marcar REQ-IDs done explícitamente")
    md.add_argument("req_ids", nargs="+")
    md.add_argument("--quiet", action="store_true")
    md.add_argument("--dry-run", action="store_true")

    am = sub.add_parser("amend", help="Registrar SPEC amendment")
    am.add_argument("reason")
    am.add_argument("--phase", type=int, default=None)
    am.add_argument("--quiet", action="store_true")
    am.add_argument("--dry-run", action="store_true")

    st = sub.add_parser("status", help="Mostrar divergencia")

    args = parser.parse_args()
    planning = Path(args.planning).resolve()

    try:
        bridge = GsdBridge(
            planning,
            quiet=getattr(args, "quiet", False),
            dry_run=getattr(args, "dry_run", False),
        )
    except FileNotFoundError as e:
        print(f"✗ {e}", file=sys.stderr)
        return 1

    if args.cmd == "sync":
        return bridge.cmd_sync()
    if args.cmd == "mark-done":
        return bridge.cmd_mark_done(args.req_ids)
    if args.cmd == "amend":
        return bridge.cmd_amend(args.reason, args.phase)
    if args.cmd == "status":
        return bridge.cmd_status()
    return 1


if __name__ == "__main__":
    sys.exit(main())
