"""Configuration du projet : chemins, graine aléatoire et listes de variables."""
from pathlib import Path

# Racine du projet (src/heart/config.py -> on remonte de 3 niveaux)
RACINE = Path(__file__).resolve().parents[2]

CHEMIN_BRUT = RACINE / "data" / "raw" / "Heart_disease_statlog.csv"
CHEMIN_PROPRE = RACINE / "data" / "processed" / "heart_propre.csv"
DOSSIER_FIGURES = RACINE / "reports" / "graphiques"

# Graine pour rendre les résultats reproductibles
RANDOM = 42

VARIABLES_CONTINUES = ["age", "trestbps", "chol", "thalach", "oldpeak"]
VARIABLES_CATEGORIELLES = ["sex", "cp", "fbs", "restecg", "exang", "slope", "ca", "thal"]
