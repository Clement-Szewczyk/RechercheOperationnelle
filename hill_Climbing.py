import liste_successeur  as ls 

import random

def evaluation(graphe, coloration):
    """
    Évalue la qualité d'une coloration.
    :param graphe: Dictionnaire représentant le graphe.
    :param coloration: Dictionnaire {sommet: couleur}.
    :return: Nombre de conflits dans la coloration.
    """
    conflits = 0
    for sommet, voisins in graphe.items():
        for voisin in voisins:
            if coloration[sommet] == coloration[voisin]:
                conflits += 1
    return conflits // 2  # Chaque conflit est compté deux fois

def generer_voisin(coloration, graphe, couleurs):
    """
    Génère une nouvelle solution en modifiant aléatoirement la couleur d'un sommet.
    :param coloration: Dictionnaire {sommet: couleur}.
    :param graphe: Dictionnaire représentant le graphe.
    :param couleurs: Liste des couleurs possibles.
    :return: Une nouvelle coloration.
    """
    voisin = coloration.copy()
    sommet_a_modifier = random.choice(list(graphe.keys()))
    nouvelle_couleur = random.choice(couleurs)
    voisin[sommet_a_modifier] = nouvelle_couleur
    return voisin

def hill_climbing(graphe, solution_initiale, couleurs, max_iterations=1000):
    """
    Implémente l'algorithme de Hill-Climbing pour la coloration de graphe.
    :param graphe: Dictionnaire représentant le graphe.
    :param solution_initiale: Dictionnaire {sommet: couleur}.
    :param couleurs: Liste des couleurs possibles.
    :param max_iterations: Nombre maximal d'itérations.
    :return: Meilleure solution trouvée et son score.
    """
    solution = solution_initiale
    meilleure_solution = solution
    meilleure_score = evaluation(graphe, solution)

    for _ in range(max_iterations):
        voisin = generer_voisin(solution, graphe, couleurs)
        score_voisin = evaluation(graphe, voisin)

        if score_voisin < meilleure_score:
            meilleure_solution = voisin
            meilleure_score = score_voisin

        # Critère d'arrêt si aucune erreur
        if meilleure_score == 0:
            break

    return meilleure_solution, meilleure_score
