from graphviz import Digraph

# Convertisseur de graphe en format DOT et PNG

def to_dot(graphe):
    """
    Convertit un graphe sous forme de liste d'adjacence en un graphe au format DOT.

    :param graphe: Dictionnaire représentant le graphe sous forme de liste d'adjacence.
    :return: Une chaîne de caractères représentant le graphe au format DOT.
    """
    dot = Digraph()
    
    # Sommets
    for sommet in graphe:
        dot.node(str(sommet))
    for sommet, voisins in graphe.items():
        for voisin in voisins:
            if sommet < voisin:
                dot.edge(str(sommet), str(voisin))

    return dot

def to_png(graphe, fichier_png):
    """
    Convertit un graphe sous forme de liste d'adjacence en un fichier PNG.

    :param graphe: Dictionnaire représentant le graphe sous forme de liste d'adjacence.
    :param fichier_png: Chemin du fichier PNG.
    """
    dot = to_dot(graphe)
    dot.render(fichier_png, format='png', cleanup=True)