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



def graphe_colorie(graphe, coloration):
    """
    Colorie un graphe selon une coloration donnée.

    :param graphe: Dictionnaire représentant le graphe.
    :param coloration: Dictionnaire {sommet: couleur}.
    :return: Dictionnaire d'un graphe coloré avec la strucutre {Sommet: (couleur, [voisins])}.
    """
    graphe_colore = {}

    for sommet, couleur in coloration.items():
        graphe_colore[sommet] = (couleur, graphe[sommet])

    return graphe_colore


def evaluer_coloration(graphe_colore):
    """
    Évalue la qualité d'une coloration.

    :param graphe_colore: Dictionnaire d'un graphe coloré avec la strucutre {Sommet: (couleur, [voisins])}.
    :return: Nombre de conflits dans la coloration.
    """
    conflits = 0

    for sommet, (couleur, voisins) in graphe_colore.items():
        for voisin in voisins:
            if couleur == graphe_colore[voisin][0]:
                conflits += 1

    return conflits // 2  # Chaque conflit est compté deux fois
    

graphe = {}
fichier = "graphe/test1.col"

graphe  = ls.lire_graphe_col(fichier)
print("Graphe : ", graphe)

coloration = welsh_Powell(graphe)

print("Coloration : ", coloration)

graphe_colore = graphe_colorie(graphe, coloration)
print("Graphe coloré : ", graphe_colore)

score = evaluer_coloration(graphe_colore)
print("Score : ", score)


