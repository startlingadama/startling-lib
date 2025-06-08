# startling_lib

Une librairie Python modulaire pour la gestion des compétences, des profils professionnels et des aspects techniques.

## Structure du package

```text
startling_lib/
├── competence/
│   ├── __init__.py
│   └── competence.py
├── cv/
│   └── __init__.py
├── engineering/
│   └── __init__.py
````

## Modules

### `startling_lib.competence`

Contient les outils liés à la gestion des compétences (modèles, calculs, filtres, etc.).

Exemple d'utilisation :

```python
from startling_lib.competence import competence

competence.analyze_skills(["python", "llm"])
```

### `startling_lib.cv`

Gère les représentations de CV ou les données liées au parcours professionnel.

### `startling_lib.engineering`

Composants techniques transversaux, outils pour l'intégration, l'automatisation, ou l'inférence.

##  Installation (locale)

```bash
pip install -e .
```

> Assure-toi d’avoir `pyproject.toml` configuré correctement.

## Dépendances

Aucune dépendance externe obligatoire pour le cœur de la lib.

## Licence

MIT - libre d'utilisation, modification et distribution.
