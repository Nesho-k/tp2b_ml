# Préparation des variables : standardisation et encodage one-hot
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from .a_config import VARIABLES_CATEGORIELLES, VARIABLES_CONTINUES
from .b_dataset import charger_propres


def preparer_matrice(df):
    # Standardisation des variables continues (moyenne 0, écart-type 1)
    scaler = StandardScaler()
    continues = scaler.fit_transform(df[VARIABLES_CONTINUES])

    # Encodage one-hot des variables catégorielles
    encodeur = OneHotEncoder(sparse_output=False)
    categorielles = encodeur.fit_transform(df[VARIABLES_CATEGORIELLES])

    X = np.hstack([continues, categorielles])
    noms = VARIABLES_CONTINUES + list(encodeur.get_feature_names_out(VARIABLES_CATEGORIELLES))
    return X, noms


def main():
    # Affiche la forme de la matrice utilisée pour le clustering (la cible n'y figure pas)
    X, noms = preparer_matrice(charger_propres())
    print("Forme de la matrice X :", X.shape)
    print("Colonnes :", noms)


if __name__ == "__main__":
    main()
