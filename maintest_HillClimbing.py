from liste_successeur import lire_graphe_col
from welsh_Powell import welsh_Powell
from hill_Climbing import hill_climbing

# Charger le graphe
chemin_fichier = 'graphe/test2.col'
graphe = lire_graphe_col(chemin_fichier)

# Générer une solution initiale avec Welsh-Powell
solution_initiale = welsh_Powell(graphe)

# Liste des couleurs possibles
couleurs = [0, 1, 2, 3, 4]  # Modifier selon les besoins

# Appliquer Hill-Climbing
solution_finale, score = hill_climbing(graphe, solution_initiale, couleurs)

print("Solution finale :", solution_finale)
print("Conflits restants :", score)
