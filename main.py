import welsh_Powell as wp
import liste_successeur as ls




def main():

    print("Projet Coloration de Graphe")
    print("Auteur : Jade Delebecque et Clément Szewczyk")

    # Lecture d'un fichier de graphe modification

    fichier = "graphe/test1.col"
    print("Lecture du fichier : ", fichier)
    
    graphe = ls.lire_graphe_col(fichier)
    print("Nombre de sommets :", len(graphe))
    print("Nombre d'arêtes :", sum(len(voisins) for voisins in graphe.values()) // 2)

    # Affichage du graphe
    print(graphe)
    
    # Ajout d'un sommet
    print("Ajout d'un sommet")
    ls.ajouter_Sommet(graphe, 6)
    print(graphe)

    # Ajout d'une arête
    print("Ajout d'une arête")
    ls.ajouter_Arete(graphe, 1, 6)
    print(graphe)

    # Suppression d'un Sommet
    print("Suppression d'un sommet")
    ls.supprimer_Sommet(graphe, 6)

    print(graphe)



    print("\n")
    fichier = "graphe/anna.col"
    print("Lecture du fichier : ", fichier)

    graphe_Welsh_Powell = ls.lire_graphe_col(fichier)
    print("Nombre de sommets :", len(graphe_Welsh_Powell))
    print("Nombre d'arêtes :", sum(len(voisins) for voisins in graphe_Welsh_Powell.values()) // 2)
    print("\n")

    # Welsh-Powell

    print("Coloration de graphe avec Welsh-Powell")
    coloration_Welsh_Powell, temps = wp.welsh_Powell(graphe_Welsh_Powell)

    print("Temps d'exécution : ", temps, " secondes")
    nb_couleur = wp.nb_couleur(coloration_Welsh_Powell)
    print("Nombre de couleurs : ", nb_couleur)
    conflit_Welsh_Powell = ls.evaluer_coloration(ls.graphe_colorie(graphe_Welsh_Powell, coloration_Welsh_Powell))
    print("Conflit du Welsh Powell: ", conflit_Welsh_Powell)
    graphe_colore_Welsh_Powell = ls.graphe_colorie(graphe_Welsh_Powell, coloration_Welsh_Powell)
    print("\n")
    
    # Exportation d'un graphe coloré
    
    ls.exporter_graphe_colore(graphe_colore_Welsh_Powell, "graphe/coloration_Welsh_Powell.col")

    # Lecture d'un fichier de coloration
    print("Lecture d'un fichier de coloration Welsh-Powell")
    fichier_coloration = "graphe/coloration_Welsh_Powell.col"
    graphe_colorie = ls.lire_graphe_colore(fichier_coloration)

    
    # Regarde si on a bien un graphe colorié
    print("Validation ", ls.est_valide(graphe_colorie))

    # Evaluation de la coloration
    score = ls.evaluer_coloration(graphe_colorie)
    print("Score de l'import: ", score)
    nb_couleur_import = len(set([couleur for couleur, voisins in graphe_colorie.values()]))
    print("Nombre de couleurs de l'import: ", nb_couleur_import)
    print("\n")

    print("Coloration de graphe avec Hill Climbing")

if __name__ == "__main__":
    main()


