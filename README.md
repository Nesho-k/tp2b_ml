# Clustering non supervisé des maladies cardiaques

Projet de clustering (K-Means) sur des données de patients cardiaques.
La variable `target` (maladie ou non) n'est **jamais** utilisée pour construire les clusters : elle sert seulement à la comparaison finale.

## Données

- Fichier : `data/raw/Heart_disease_statlog.csv` 
- 270 lignes, 14 colonnes, aucune valeur manquante, aucun doublon
- Variables continues : `age`, `trestbps`, `chol`, `thalach`, `oldpeak`
- Variables catégorielles (codées en nombres) : `sex`, `cp`, `fbs`, `restecg`, `exang`, `slope`, `ca`, `thal`
- Cible : `target` (0 = pas de maladie, 1 = maladie)

Le fichier brut n'est jamais modifié. Le jeu nettoyé est écrit dans `data/processed/heart_propre.csv`.

## Structure

```
data/raw/             données brutes (ne pas modifier)
data/processed/       données nettoyées (créées par le notebook 1)
notebooks/1_exploration.ipynb   exploration, valeurs suspectes, sauvegarde
notebooks/2_clustering.ipynb    PCA, K-Means, choix de k, comparaison avec target
src/heart/a_config.py    chemins, graine (RANDOM = 42), listes de variables
src/heart/b_dataset.py   chargement, doublons, valeurs suspectes, sauvegarde
src/heart/c_features.py  standardisation et encodage one-hot
src/heart/d_clustering.py  PCA 2D, K-Means, inertie, silhouette
src/heart/e_plots.py     dispersion 2D, courbe du coude (figures)
reports/reponses_questions.md   réponses aux questions de cours
```

## Installation

```bash
pip install -r requirements.txt
```

## Exécution

### Option 1 : scripts (src/)

Depuis le dossier `src/`, lancer les modules dans l'ordre :

```bash
cd src
python -m heart.b_dataset    # nettoie les données, écrit data/processed/heart_propre.csv
python -m heart.c_features   # affiche la forme de la matrice de clustering
python -m heart.d_clustering # teste k de 2 à 10, clustering final, comparaison avec target
python -m heart.e_plots      # écrit les figures dans reports/graphiques/ (écrasées si elles existent)
```

### Option 2 : notebooks

Lancer les notebooks dans l'ordre, depuis le dossier `notebooks/` :

1. `1_exploration.ipynb` : crée `data/processed/heart_propre.csv`
2. `2_clustering.ipynb` : crée les figures dans `reports/graphiques/`

## Résultats principaux

- Valeurs suspectes (`thal = 0`, `ca = 4`) : aucune dans ce jeu.
- Choix de k : k = 2, car la silhouette est maximale (0,165). La courbe du coude n'a pas de cassure nette.
- La qualité des clusters est faible (silhouette < 0,17) : les groupes se recouvrent beaucoup.
- Comparaison avec `target` (après clustering) : le cluster 0 compte 73,4 % de patients malades, le cluster 1 en compte 19,9 %.
