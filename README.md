# Résolution du Problème de Sac à Dos Quadratique par Recuit Simulé

## Description

Ce projet porte sur la résolution du problème de sac à dos quadratique (Quadratic Knapsack Problem - QKP) à l’aide d’un algorithme de recuit simulé implémenté en Python.

L’objectif est de maximiser une fonction de profit quadratique tout en respectant :

- une contrainte de capacité,
- une contrainte de cardinalité.

Le projet inclut :
- la génération de solutions réalisables,
- l’utilisation d’un voisinage de type SWAP,
- l’étude expérimentale des paramètres du recuit simulé,
- ainsi que l’analyse des résultats obtenus sur plusieurs instances.


# Fonction objectif

La fonction objectif étudiée est donnée par :

\[
F(x)=
\sum_{i=1}^{n} P_{ii}x_i
+
\sum_{i=1}^{n}\sum_{j=i+1}^{n} P_{ij}x_ix_j
\]

avec :

- \(x_i \in \{0,1\}\)
- \(P_{ij}\) : profits quadratiques
- \(W_i\) : poids des objets
- \(C\) : capacité du sac
- \(k\) : cardinalité imposée

# Méthode utilisée

## Recuit simulé

Le recuit simulé est une métaheuristique inspirée du phénomène physique de refroidissement des métaux.

Le principe consiste à :
1. générer une solution initiale réalisable ;
2. explorer un voisinage ;
3. accepter certaines dégradations avec une probabilité dépendant de la température ;
4. réduire progressivement la température.

# Structure du projet

Projet/
│
├── code/
│   ├── recuit_simule.py
│   ├── instances/
│
├── rapport/
│   ├── rapport.tex
│   ├── images/
│
├── resultats/
│
├── README.md
│
└── requirements.txt

# Voisinage utilisé

Le voisinage utilisé est un voisinage SWAP.

Principe :

* retirer un objet sélectionné ;
* ajouter un objet non sélectionné.

Ce voisinage conserve automatiquement la cardinalité des solutions.


# Paramètres étudiés

Les principaux paramètres analysés sont :

* Température initiale (T)
* Taux de décroissance
* Température minimale (\varepsilon)
* Paramètre (\lambda_1)


# Résultats

Les expérimentations montrent que :

* le recuit simulé converge vers des solutions de bonne qualité ;
* les paramètres influencent fortement les performances ;
* certaines valeurs de (\lambda_1) apparaissent de manière récurrente dans les meilleures solutions.



# Technologies utilisées

* Python
* NumPy
* Matplotlib
* LaTeX



# Exécution

Exécuter :


python Récuit_Simulé.ipynb


# Perspectives

Améliorations possibles :

* optimisation automatique des paramètres ;
* étude du recuit quantique ;
* amélioration des voisinages.



# Auteur

LUC CARLOS ASSO

Étudiant en Informatique et Sciences Mathématiques (ISEM) Institut National Polytechnique Félix Houphouët-Boigny (INP-HB).

Projet réalisé dans le cadre d'un stage réalisé à SORBONE PARIS NORD.
# collègue
benziane
# Encadrants
Pr LUCAS LETOCART
Camille GRANGE
Baptiste Deshayes


