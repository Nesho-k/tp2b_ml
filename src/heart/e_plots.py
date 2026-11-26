# Graphiques : PCA 2D, dispersion des clusters et courbe du coude
import matplotlib.pyplot as plt

from .a_config import DOSSIER_FIGURES
from .b_dataset import charger_propres
from .c_features import preparer_matrice
from .d_clustering import K_RETENU, kmeans_pour_k, projeter_pca_2d, tester_plage_k


def tracer_dispersion_2d(X_pca, etiquettes=None, titre="", chemin=None):
    # Sans étiquettes, les points sont gris ; avec étiquettes, chaque cluster a sa couleur
    plt.figure(figsize=(7, 5))
    if etiquettes is None:
        plt.scatter(X_pca[:, 0], X_pca[:, 1], color="gray", s=25, alpha=0.8)
    else:
        plt.scatter(X_pca[:, 0], X_pca[:, 1], c=etiquettes, cmap="tab10", s=25, alpha=0.8)
    plt.title(titre)
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    if chemin is not None:
        plt.savefig(chemin, dpi=120)
    plt.close()


def tracer_coude_silhouette(tableau_k, chemin=None):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

    ax1.plot(tableau_k["k"], tableau_k["inertie"], marker="o")
    ax1.set_title("Courbe du coude")
    ax1.set_xlabel("Nombre de clusters k")
    ax1.set_ylabel("Inertie")

    ax2.plot(tableau_k["k"], tableau_k["silhouette"], marker="o", color="darkorange")
    ax2.set_title("Coefficient de silhouette")
    ax2.set_xlabel("Nombre de clusters k")
    ax2.set_ylabel("Silhouette moyenne")

    for ax in (ax1, ax2):
        ax.set_xticks(tableau_k["k"])
    plt.tight_layout()
    if chemin is not None:
        plt.savefig(chemin, dpi=120)
    plt.close()


def main():
    # Produit les trois figures dans reports/graphiques/ (les fichiers existants sont écrasés)
    DOSSIER_FIGURES.mkdir(parents=True, exist_ok=True)
    df = charger_propres()
    X, _ = preparer_matrice(df)
    X_pca, _ = projeter_pca_2d(X)
    etiquettes, _, _ = kmeans_pour_k(X, K_RETENU)

    tracer_dispersion_2d(X_pca, titre="Données projetées en 2D (PCA)",
                         chemin=DOSSIER_FIGURES / "pca_2d.png")
    tracer_coude_silhouette(tester_plage_k(X), chemin=DOSSIER_FIGURES / "courbe_coude.png")
    tracer_dispersion_2d(X_pca, etiquettes, titre=f"Clusters K-Means (k = {K_RETENU}) projetés par PCA",
                         chemin=DOSSIER_FIGURES / "clusters_pca.png")
    print("Figures écrites dans", DOSSIER_FIGURES)


if __name__ == "__main__":
    main()
