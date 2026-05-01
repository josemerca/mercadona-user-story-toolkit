# Ejemplos de TDD — Step 2: Clasificador de Ambigüedad

Ejemplo ilustrativo del ciclo **red → green → refactor** que aplica `/superpowers:test-driven-development` para implementar la story DETECT-01.

---

## Ciclo 1: Test rojo

**Test:** "Query con 4 categorías de peso similar en top-20 se clasifica como `ambiguous`"

```python
def test_query_with_high_dispersion_is_classified_ambiguous():
    top_k_results = [
        Product(id="p1", category="cafe-molido"),
        Product(id="p2", category="cafe-molido"),
        Product(id="p3", category="cafe-grano"),
        Product(id="p4", category="cafe-grano"),
        Product(id="p5", category="cafe-soluble"),
        # ... (15 más con dispersión similar)
    ]
    classifier = SearchClassifier(threshold=AmbiguityThreshold(min_categories=3, min_weight=0.10))

    result = classifier.classify(top_k_results)

    assert result == QueryClassification.AMBIGUOUS
```

**Estado:** ❌ Falla — `SearchClassifier` no existe todavía.

---

## Ciclo 1: Implementación mínima (verde)

```python
@dataclass
class AmbiguityThreshold:
    min_categories: int  # ej: 3
    min_weight: float    # ej: 0.10

class SearchClassifier:
    def __init__(self, threshold: AmbiguityThreshold):
        self.threshold = threshold

    def classify(self, top_k_results: list[Product]) -> QueryClassification:
        if not top_k_results:
            return QueryClassification.SPECIFIC

        # Contar peso de cada categoría
        from collections import Counter
        counter = Counter(p.category for p in top_k_results)
        total = len(top_k_results)
        weights = {cat: count / total for cat, count in counter.items()}

        # Categorías que superan el min_weight
        significant = [cat for cat, w in weights.items() if w >= self.threshold.min_weight]

        if len(significant) >= self.threshold.min_categories:
            return QueryClassification.AMBIGUOUS
        return QueryClassification.SPECIFIC
```

**Estado:** ✅ Test verde.

---

## Ciclo 2: Test rojo nuevo

**Test:** "Query con 1 categoría dominante (>80%) se clasifica como `specific`"

```python
def test_query_with_dominant_category_is_classified_specific():
    top_k_results = [Product(id=f"p{i}", category="cafe-molido") for i in range(18)]
    top_k_results += [
        Product(id="p19", category="cafe-grano"),
        Product(id="p20", category="cafe-soluble"),
    ]
    classifier = SearchClassifier(threshold=AmbiguityThreshold(min_categories=3, min_weight=0.10))

    result = classifier.classify(top_k_results)

    assert result == QueryClassification.SPECIFIC
```

**Estado:** ✅ Verde directamente — la implementación ya cubre este caso (solo 1 categoría con peso ≥10%).

---

## Ciclo 3: Test rojo (DETECT-02 — feature flag)

**Test:** "Cambio del threshold en runtime modifica la clasificación sin reiniciar"

```python
def test_threshold_changes_at_runtime_via_feature_flag():
    flag_provider = MockFeatureFlagProvider(threshold=AmbiguityThreshold(3, 0.10))
    classifier = SearchClassifier.from_feature_flag(flag_provider)

    top_k_results = [...] # 4 categorías similares

    # Threshold inicial: ambigua
    assert classifier.classify(top_k_results) == QueryClassification.AMBIGUOUS

    # Cambio runtime
    flag_provider.update_threshold(AmbiguityThreshold(min_categories=5, min_weight=0.15))

    # Mismo input → ahora específica (threshold más estricto)
    assert classifier.classify(top_k_results) == QueryClassification.SPECIFIC
```

**Estado:** ❌ Falla — `from_feature_flag` no existe.

---

## Ciclo 3: Implementación + refactor

```python
class SearchClassifier:
    def __init__(self, threshold: AmbiguityThreshold):
        self._fixed_threshold = threshold
        self._flag_provider = None

    @classmethod
    def from_feature_flag(cls, flag_provider: FeatureFlagProvider) -> "SearchClassifier":
        instance = cls(threshold=flag_provider.get_threshold())
        instance._flag_provider = flag_provider
        return instance

    def _current_threshold(self) -> AmbiguityThreshold:
        if self._flag_provider:
            return self._flag_provider.get_threshold()
        return self._fixed_threshold

    def classify(self, top_k_results: list[Product]) -> QueryClassification:
        threshold = self._current_threshold()
        # ... (resto igual)
```

**Estado:** ✅ Verde. Todos los tests previos siguen pasando.

**Refactor:** El código está limpio. La separación entre `_fixed_threshold` y `_flag_provider` es clara. No requiere refactor.

---

## Ciclo 4: Test de performance (DETECT-03)

**Test:** "Clasificación <10ms p99 en 1000 ejecuciones"

```python
def test_classify_performance_under_10ms_p99():
    classifier = SearchClassifier(threshold=AmbiguityThreshold(3, 0.10))
    top_k_results = generate_synthetic_top_k(20)  # fixture

    latencies = []
    for _ in range(1000):
        start = time.perf_counter_ns()
        classifier.classify(top_k_results)
        latencies.append((time.perf_counter_ns() - start) / 1_000_000)  # ms

    p99 = sorted(latencies)[990]  # p99 de 1000
    assert p99 < 10.0, f"p99 = {p99:.2f}ms, esperado <10ms"
```

**Estado:** ✅ Verde con la implementación actual (Counter de stdlib es muy rápido).

---

## Verificación final (verification-before-completion)

Antes de declarar Step 2 completado:

```bash
$ pytest tests/search/test_classifier.py -v
tests/search/test_classifier.py::test_query_with_high_dispersion_is_classified_ambiguous PASSED
tests/search/test_classifier.py::test_query_with_dominant_category_is_classified_specific PASSED
tests/search/test_classifier.py::test_threshold_changes_at_runtime_via_feature_flag PASSED
tests/search/test_classifier.py::test_classify_performance_under_10ms_p99 PASSED
... (22 tests más para casos edge: empty results, todas mismas categoría, threshold extremos, etc.)

26 passed in 1.42s
```

✅ **Todos los tests verdes. Step 2 completado.**

Commit:

```
git commit -m "feat(search): implement DETECT-01 + DETECT-02 + DETECT-03 ambiguity classifier

- Add SearchClassifier with category dispersion heuristic
- Support runtime threshold updates via feature flag
- Performance: <10ms p99 over 1000 executions

Refs: DETECT-01, DETECT-02, DETECT-03"
```

---

## Lo que NO se ve en este ejemplo

Por brevedad, el documento muestra solo el ciclo TDD del clasificador (Step 2). Los Steps 3 (generador), 4 (ordenación), 5 (integración) y 6 (performance + regresión) siguen el mismo patrón:

1. Test que captura el behavior change (red)
2. Implementación mínima que pasa el test (green)
3. Refactor solo si emerge una smell concreta
4. Verificación con suite completa antes de commit
5. Commit con REQ-IDs en mensaje (para que el bridge GSD↔SP los detecte)

**Token cost estimado para todo el Batch 1:** 180k-280k (subagent-driven) o 90k-150k (sin subagents). El subagent-driven es ~2x el coste pero ~1.5x la velocidad y mejor aislamiento de bugs.
