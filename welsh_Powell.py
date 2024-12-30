import liste_successeur  as ls 

def welsh_Powell(graphe):
    """
    Algorithme de coloration de graphe de Welsh-Powell.

    :param graphe: Dictionnaire représentant le graphe.
    :return: Dictionnaire d'une coloration {sommet: couleur}.
    """
    # tri décroissant des sommets par degrés
    Sommet_trié = sorted(graphe, key=lambda sommet: len(graphe[sommet]), reverse=True)
    # Dictionaire de coloration
    coloration = {}
    couleur = 0

    # Parcours des sommets triés
    for sommet in Sommet_trié:

        couleur_disponible = True

        # Parcours des voisins du sommet
        for voisin in graphe[sommet]:
            # Si le voisin a la même couleur que le sommet
            if voisin in coloration and coloration[voisin] == couleur:
                couleur_disponible = False
                break
        
        if couleur_disponible:
            coloration[sommet] = couleur
        else:
            couleur += 1
            coloration[sommet] = couleur
    
    return coloration

def evaluer_coloration(graphe, coloration): # A revoir
    """
    Évalue une coloration de graphe en comptant le nombre de conflits.

    :param graphe: Dictionnaire représentant le graphe.
    :param coloration: Dictionnaire {sommet: couleur}.
    :return: Nombre de conflits.
    """
    conflits = 0

    for sommet, voisins in graphe.items():
        for voisin in voisins:
            if voisin in coloration and coloration[voisin] == coloration[sommet]:
                conflits += 1

    return conflits // 2

        




