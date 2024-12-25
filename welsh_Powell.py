import liste_successeur  as ls 



def welsh_Powell(graphe):
    """
    Algorithme de coloration de graphe de Welsh-Powell.

    :param graphe: Dictionnaire représentant le graphe.
    :return: Dictionnaire d'un graphe coloré.
    """
    # tri décroissant des sommets par degrés

    Sommet_trié = sorted(graphe, key=lambda sommet: len(graphe[sommet]), reverse=True)
    print(Sommet_trié)

    graphes_colores = {}
    couleur = 0

    for sommet in Sommet_trié:
        couleur_disponible = True
        for voisin in graphe[sommet]:
            if voisin in graphes_colores and graphes_colores[voisin] == couleur:
                couleur_disponible = False
                break

        if couleur_disponible:
            graphes_colores[sommet] = couleur
        else:
            couleur += 1
            graphes_colores[sommet] = couleur
    
    return graphes_colores


def verifier_Coloration(graphe):
    pass 


graphe = {}
fichier = "graphe/test1.col"


graphe  = ls.lire_graphe_col(fichier)

ls.afficher_graphe(graphe)

print(welsh_Powell(graphe))




