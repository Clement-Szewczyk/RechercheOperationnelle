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



def exporter_graphe_col(fichier, graphe):
    """
    Exporte un graphe sous forme de liste d'adjacence dans un fichier .col.

    :param fichier: Chemin du fichier .col.
    :param graphe: Dictionnaire représentant le graphe sous forme de liste d'adjacence.
    """
    try:
        with open(fichier, 'w') as f:
            f.write(f"p edge {len(graphe)} {sum(len(v) for v in graphe.values()) // 2}\n")
            for sommet, voisins in graphe.items():
                for voisin in voisins:
                    if sommet < voisin:
                        f.write(f"e {sommet} {voisin}\n")
    except Exception as e:
        print(f"Une erreur s'est produite lors de l'écriture du fichier : {e}")


def ajouter_Sommet(graphe, sommet):
    """
    Ajoute un sommet au graphe.

    :param graphe: Dictionnaire représentant le graphe.
    :param sommet: Numéro du sommet à ajouter.
    """
    if sommet not in graphe:
        graphe[sommet] = []
    else:
        print(f"Le sommet {sommet} existe déjà dans le graphe.")


def ajouter_Arete(graphe, u, v):
    """
    Ajoute une arête entre deux sommets du graphe.

    :param graphe: Dictionnaire représentant le graphe.
    :param u: Numéro du premier sommet.
    :param v: Numéro du deuxième sommet.
    """
    if u in graphe and v in graphe:
        graphe[u].append(v)
        graphe[v].append(u)
    else:
        print("Les sommets spécifiés n'existent pas dans le graphe.")

def supprimer_Sommet(graphe, sommet):
    """
    Supprime un sommet du graphe.

    :param graphe: Dictionnaire représentant le graphe.
    :param sommet: Numéro du sommet à supprimer.
    """
    if sommet in graphe:
        for voisin in graphe[sommet]:
            graphe[voisin].remove(sommet)
        del graphe[sommet]
    else:
        print(f"Le sommet {sommet} n'existe pas dans le graphe.")


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
    chemin_fichier = 'graphe/test1.col'
    graphe = lire_graphe_col(chemin_fichier)

    if graphe:
        print("Graphe lu avec succès :")
        afficher_graphe(graphe)
        # Ajouter un sommet
        ajouter_Sommet(graphe, 6)
        # Ajouter une arête
        ajouter_Arete(graphe, 6, 1)
        print("Graphe modifié :")
        afficher_graphe(graphe)
        exporter_graphe_col('graphe/test1_export.col', graphe)
        #supprimer_Arete(graphe, 6, 1)
        supprimer_Sommet(graphe, 6)
        print("Graphe modifié :")
        afficher_graphe(graphe)
        print(graphe)
    else:
        print("Le graphe n'a pas pu être chargé.")
