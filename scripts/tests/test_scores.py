"""Tests para score_story, score_prd, score_priority, gap_score, redflags.

Ejecutar: cd scripts && python3 -m unittest discover tests/ -v
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from gap_score import band as gap_band
from gap_score import score as gap_score
from redflags import detect
from score_prd import gate
from score_prd import score as prd_score
from score_priority import band as priority_band
from score_priority import score as priority_score
from score_story import band as story_band
from score_story import score as story_score


class TestScoreStory(unittest.TestCase):
    def test_average_aceptable(self):
        self.assertEqual(story_score(8, 7, 9, 8, 6, 7), 7.5)

    def test_average_deficiente(self):
        self.assertEqual(story_score(3, 3, 3, 3, 3, 3), 3.0)

    def test_average_excelente(self):
        self.assertEqual(story_score(10, 10, 10, 10, 10, 10), 10.0)

    def test_band_deficiente(self):
        self.assertEqual(story_band(3.0)[0], "🔴 Deficiente")

    def test_band_necesita_mejora(self):
        self.assertEqual(story_band(6.0)[0], "🟡 Necesita mejora")

    def test_band_aceptable(self):
        self.assertEqual(story_band(7.5)[0], "🟢 Aceptable")

    def test_band_excelente(self):
        self.assertEqual(story_band(9.5)[0], "⭐ Excelente")

    def test_band_boundary_5(self):
        self.assertEqual(story_band(5.0)[0], "🟡 Necesita mejora")

    def test_band_boundary_7(self):
        self.assertEqual(story_band(7.0)[0], "🟢 Aceptable")

    def test_band_boundary_9(self):
        self.assertEqual(story_band(9.0)[0], "⭐ Excelente")


class TestScorePRD(unittest.TestCase):
    def test_average(self):
        self.assertEqual(prd_score(7, 6, 5), 6.0)

    def test_d3_below_5_forces_fail(self):
        decision, _, reason = gate(9, 9, 4)
        self.assertEqual(decision, "FAIL")
        self.assertIn("D3", reason)

    def test_pass_when_all_high(self):
        decision, _, _ = gate(8, 8, 8)
        self.assertEqual(decision, "PASS")

    def test_conditional_when_average_5_6(self):
        decision, _, _ = gate(6, 6, 6)
        self.assertEqual(decision, "CONDICIONAL")

    def test_fail_when_average_below_5(self):
        decision, _, _ = gate(4, 4, 5)
        self.assertEqual(decision, "FAIL")


class TestScorePriority(unittest.TestCase):
    def test_weighted_formula(self):
        # 5*0.30 + 5*0.25 + 5*0.20 + 5*0.15 + 5*0.10 = 5.0
        self.assertEqual(priority_score(5, 5, 5, 5, 5), 5.0)

    def test_min_score(self):
        self.assertEqual(priority_score(1, 1, 1, 1, 1), 1.0)

    def test_known_combination(self):
        # 4*0.30 + 3*0.25 + 2*0.20 + 4*0.15 + 3*0.10 = 1.2+0.75+0.4+0.6+0.3 = 3.25
        self.assertEqual(priority_score(4, 3, 2, 4, 3), 3.25)

    def test_band_top(self):
        self.assertEqual(priority_band(4.5), "🔥 Top — entregar primero")

    def test_band_baja(self):
        self.assertEqual(priority_band(1.5), "⚪ Baja — backlog largo")


class TestGapScore(unittest.TestCase):
    def test_formula(self):
        # 1*10 + 2*5 + 3*2 + 5*1 = 31
        self.assertEqual(gap_score(1, 2, 3, 5), 31)

    def test_zero(self):
        self.assertEqual(gap_score(0, 0, 0, 0), 0)

    def test_critical_blocks(self):
        self.assertIn("Bloqueante", gap_band(10, 1))

    def test_high_without_critical(self):
        self.assertIn("Alto", gap_band(20, 0))

    def test_minimal(self):
        self.assertIn("Mínimo", gap_band(2, 0))


class TestRedflags(unittest.TestCase):
    def test_detects_y(self):
        f = detect("Como usuario quiero buscar productos y filtrar resultados")
        self.assertIn("1. Conjunciones coordinantes", f)
        self.assertIn("y", f["1. Conjunciones coordinantes"])

    def test_detects_gestionar(self):
        f = detect("Quiero gestionar mi cuenta")
        self.assertIn("2. Conectores de acción", f)

    def test_word_boundary_no_substring_match(self):
        # "ya" no debe matchear "y", "yo" tampoco
        f = detect("Yo siempre uso ya esta funcionalidad")
        self.assertNotIn("1. Conjunciones coordinantes", f)

    def test_detects_incluyendo(self):
        f = detect("Filtros incluyendo precio y categoría")
        self.assertIn("4. Indicadores de alcance", f)

    def test_no_red_flags(self):
        f = detect("Como cliente busco productos por marca")
        self.assertEqual(f, {})

    def test_case_insensitive(self):
        f = detect("Quiero GESTIONAR pedidos")
        self.assertIn("2. Conectores de acción", f)

    def test_multi_word_phrase(self):
        f = detect("Filtrar productos a menos que estén agotados")
        self.assertIn("6. Indicadores de excepción", f)


if __name__ == "__main__":
    unittest.main()
