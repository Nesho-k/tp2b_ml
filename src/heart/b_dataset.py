import pandas as pd

from .a_config import CHEMIN_BRUT, CHEMIN_PROPRE


def charger_donnees(chemin=CHEMIN_BRUT):
    return pd.read_csv(chemin, encoding="utf-8")


def charger_propres(chemin=CHEMIN_PROPRE):
    return pd.read_csv(chemin)


def supprimer_doublons(df):
    return df.drop_duplicates().reset_index(drop=True)


def trouver_valeurs_suspectes(df):
    return df[(df["thal"] == 0) | (df["ca"] == 4)]


def supprimer_valeurs_suspectes(df):
    return df[(df["thal"] != 0) & (df["ca"] != 4)].reset_index(drop=True)


def sauvegarder_donnees(df, chemin=CHEMIN_PROPRE):
    chemin.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(chemin, index=False)


def main():
    # Nettoie le fichier brut et écrit data/processed/heart_propre.csv
    df = charger_donnees()
    print("Lignes brutes :", len(df))

    df = supprimer_doublons(df)
    print("Lignes après suppression des doublons :", len(df))

    print("Lignes avec valeurs suspectes :", len(trouver_valeurs_suspectes(df)))
    df = supprimer_valeurs_suspectes(df)
    print("Lignes après suppression des valeurs suspectes :", len(df))

    sauvegarder_donnees(df)
    print("Fichier sauvegardé :", CHEMIN_PROPRE)


if __name__ == "__main__":
    main()
