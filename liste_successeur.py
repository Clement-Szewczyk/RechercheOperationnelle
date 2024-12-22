# Parseur DIMACS pour les graphes au format .col

def lire_graphe_col(fichier):
    """
    Lit un fichier .col et retourne une structure de graphe sous forme de liste d'adjacence.

    :param fichier: Chemin du fichier .col.
    :return: Un dictionnaire représentant le graphe sous forme de liste d'adjacence.
    """
    graphe = {}
    
    try:
        with open(fichier, 'r') as f:
            lignes = f.readlines()

        for ligne in lignes:
            ligne = ligne.strip()
            # Ignorer les commentaires
            if ligne.startswith('c'):
                continue

            # Lire les propriétés du graphe
            elif ligne.startswith('p'):
                _, _, nb_sommets, _ = ligne.split()
                nb_sommets = int(nb_sommets)
                # Initialiser un dictionnaire vide pour chaque sommet
                graphe = {i: [] for i in range(1, nb_sommets + 1)}

            # Lire les arêtes
            elif ligne.startswith('e'):
                _, u, v = ligne.split()
                u, v = int(u), int(v)
                graphe[u].append(v)
                graphe[v].append(u)  # Ajouter l'arête dans les deux sens pour un graphe non orienté

    except FileNotFoundError:
        print(f"Erreur : le fichier {fichier} est introuvable.")
    except Exception as e:
        print(f"Une erreur s'est produite lors de la lecture du fichier : {e}")

    return graphe


def afficher_graphe(graphe):
    """
    Affiche le graphe sous forme de liste d'adjacence.

    :param graphe: Dictionnaire représentant le graphe.
    """
    for sommet, voisins in graphe.items():
        print(f"{sommet} -> {', '.join(map(str, voisins))}")


# Exemple d'utilisation
if __name__ == "__main__":
    # Exemple : Remplacez 'chemin_vers_fichier.col' par le chemin réel du fichier .col
    chemin_fichier = 'test1.col'
    graphe = lire_graphe_col(chemin_fichier)

    if graphe:
        print("Graphe lu avec succès :")
        afficher_graphe(graphe)
    else:
        print("Le graphe n'a pas pu être chargé.")
