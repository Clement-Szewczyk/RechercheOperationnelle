import liste_successeur  as ls 
import time

def welsh_Powell(graphe):
    """
    Algorithme de coloration de graphe de Welsh-Powell.

    :param graphe: Dictionnaire représentant le graphe.
    :return: Dictionnaire d'une coloration {sommet: couleur}.
    """
    start_time = time.perf_counter()

    # Tri décroissant des sommets par degrés
    Sommet_trié = sorted(graphe, key=lambda sommet: len(graphe[sommet]), reverse=True)
    # Dictionaire de coloration
    coloration = {}

    # Parcours des sommets triés
    for sommet in Sommet_trié:
        couleurs_voisins = {coloration[voisin] for voisin in graphe[sommet] if voisin in coloration}

        # Trouver la plus petite couleur non utilisée
        couleur = 0
        while couleur in couleurs_voisins:
            couleur += 1
        coloration[sommet] = couleur

    end_time = time.perf_counter()
    duree = end_time - start_time

    return coloration, duree



def nb_couleur(coloration):
    """
    Calcul du nombre de couleur utilisée dans une coloration.

    :param coloration: Dictionnaire d'une coloration {sommet: couleur}.
    :return: Nombre de couleur utilisée.
    """
    return len(set(coloration.values()))






