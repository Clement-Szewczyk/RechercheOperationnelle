import liste_successeur as ls
import welsh_Powell as wp


graphe = {}
fichier = "graphe/test4.col"

graphe  = ls.lire_graphe_col(fichier)
print("Graphe : ", graphe)

coloration = wp.welsh_Powell(graphe)

print("Coloration : ", coloration)

graphe_colore = wp.graphe_colorie(graphe, coloration)
print("Graphe coloré : ", graphe_colore)

score = wp.evaluer_coloration(graphe, {})
print("Score : ", score)
