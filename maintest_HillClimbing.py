import hill_Climbing as hc
import liste_successeur as ls

# Chargement du graphe à partir d'un fichier DIMACS
fichier = "graphe/test5.col"
graphe = ls.lire_graphe_col(fichier)

if graphe:
    # Exécuter l'algorithme de Hill Climbing
    solution, nb_colors, execution_time, iterations, residual_conflicts = hc.hill_climbing(graphe)

    # Afficher les résultats
    print("Fichier :", fichier)
    print("Nombre de couleurs utilisées :", nb_colors)
    print("Temps d'exécution :", execution_time, "secondes")
    print("Nombre d'itérations :", iterations)
    print("Conflits résiduels :", residual_conflicts)

    # Exporter la solution colorée
    graphe_colore = ls.graphe_colorie(graphe, solution)
    ls.exporter_graphe_colore(graphe_colore, "graphe/solution_hill_climbing.col")
else:
    print("Le graphe n'a pas pu être chargé.")