# Réduction de dimension (PCA) et clustering (K-Means)
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

from .a_config import RANDOM
from .b_dataset import charger_propres
from .c_features import preparer_matrice

# Valeur de k retenue (silhouette maximale, voir le notebook 2)
K_RETENU = 2


def projeter_pca_2d(X):
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)
    return X_pca, pca.explained_variance_ratio_


def kmeans_pour_k(X, k):
    kmeans = KMeans(n_clusters=k, n_init=10, random_state=RANDOM) # n_init = nombre de fois que le kmeans est lancé avec des points de départ différent 
    etiquettes = kmeans.fit_predict(X)
    return etiquettes, kmeans.inertia_, silhouette_score(X, etiquettes)


def tester_plage_k(X, k_min=2, k_max=10):
    lignes = []
    for k in range(k_min, k_max + 1):
        _, inertie, silhouette = kmeans_pour_k(X, k)
        lignes.append({"k": k, "inertie": inertie, "silhouette": silhouette})
    return pd.DataFrame(lignes)


def main():
    df = charger_propres()
    X, _ = preparer_matrice(df)

    print("Test de k de 2 à 10 :")
    print(tester_plage_k(X).round(3))

    etiquettes, inertie, silhouette = kmeans_pour_k(X, K_RETENU)
    print(f"Pour k = {K_RETENU} : inertie {inertie:.2f}, silhouette {silhouette:.3f}")
    print(pd.Series(etiquettes).value_counts().sort_index())

    # Comparaison a posteriori avec target (le modèle ne l'a pas utilisée)
    print(pd.crosstab(etiquettes, df["target"], rownames=["cluster"]))


if __name__ == "__main__":
    main()
