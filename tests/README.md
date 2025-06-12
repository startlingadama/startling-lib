# 📦 startling-lib

Une librairie Python modulaire pour gérer des compétences et agents intelligents.

## 🧪 Tests

Le projet est structuré avec 3 types de tests :

```
startling-lib/
├── tests/
│   ├── unit/                # Tests unitaires (fonctions/classes isolées)
│   ├── integration/         # Tests d'intégration (plusieurs modules ensemble)
│   ├── e2e/                 # Tests end-to-end (scénarios utilisateur complet)
│   └── conftest.py          # Fixtures partagées
```

## 🚀 Lancer les tests

Installe les dépendances :
```bash
pip install -e .[dev]
```

Lancer tous les tests :
```bash
pytest
```

Lancer un test spécifique :
```bash
pytest tests/unit/test_competence.py
```

Lancer un test spécifique dans un fichier :
```bash
pytest tests/unit/test_competence.py::test_nom_de_la_fonction
```

Tester avec couverture :
```bash
pytest --cov=startling_lib
```

## 🔍 Structure recommandée

- `unit/` : logique pure, indépendante (ex: validation Pydantic, fonctions simples)
- `integration/` : logique combinée (ex: parsing + enregistrement)
- `e2e/` : tests utilisateurs ou agents LLM complets

## 💡 Exemple de test
```python
from startling_lib.competence import Personal

def test_personal_fields():
    p = Personal(firstname="Adama", lastname="Kane")
    assert p.firstname == "Adama"
```
---
## Test

[![codecov](https://codecov.io/gh/startlingadama/startling-lib/branch/main/graph/badge.svg)](https://codecov.io/gh/startlingadama/startling-lib)

---

Développé avec ❤️ pour une IA plus modulaire et testable.
