# Réponses aux questions

## 7. Objectif de l'apprentissage non supervisé et différence avec le supervisé

En non supervisé, on n'a pas de réponse attendue. Le but est de trouver des groupes dans les données : on regroupe les patients qui se ressemblent. En supervisé, on a une cible à prédire (ici `target`) et on entraîne un modèle à la retrouver à partir des autres variables. Dans notre projet, les clusters sont faits sans `target`. On utilise `target` après, pour voir ce que représentent les groupes.

## 8. Comment choisir le nombre de clusters k avec K-Means

On essaie plusieurs valeurs de k et on regarde deux critères.

- L'inertie mesure la distance des points à leur centre. Elle baisse toujours quand k augmente. On cherche le point où la baisse ralentit fortement : c'est le « coude ».
- La silhouette mesure si chaque point est bien dans son cluster, plutôt que proche d'un autre. On garde le k qui donne la plus grande valeur.

Dans notre projet, la silhouette est la plus haute pour k = 2 (0,165). La courbe du coude n'a pas de cassure nette, donc on garde donc k = 2.

## 9. Pourquoi standardiser les variables

K-Means calcule des distances entre les patients. Si une variable a de grandes valeurs, comme le cholestérol (autour de 250), elle pèse beaucoup plus que `oldpeak` (autour de 1). La standardisation met chaque variable continue à moyenne 0 et écart-type 1. Elles comptent alors à peu près autant. Il n'y a pas de découpage train/test en non supervisé, donc le scaler est calculé sur tout le jeu de données.

## 10. Avantages et limites de K-Means

Avantages : l'algorithme est simple, rapide, et chaque cluster se résume par son centre.

Limites :
- il faut choisir k à l'avance ;
- suppose des clusters à peu près de taille proche ;
- les valeurs extrêmes le perturbent ;
- il trouve un optimum local, pas forcément la meilleure solution.

## 11. Comment évaluer la qualité des clusters

Il y a deux types d'évaluation.

- Interne : on n'utilise que les données. On regarde l'inertie et la silhouette (entre -1 et 1, plus c'est haut, mieux c'est). L'inertie baisse avec k, donc elle se lit avec la courbe du coude. 
- Externe : on compare les clusters à une cible connue. On peut regarder le pourcentage de malades dans chaque cluster

Dans notre projet, la silhouette maximale est de 0,165. Les groupes se recouvrent donc beaucoup. Malgré cela, la répartition de `target` est différente d'un cluster à l'autre : 73,4 % de malades dans le cluster 0, contre 19,9 % dans le cluster 1.
