import liste_successeur as ls
import welsh_Powell as wp


graphe = {}
fichier = "graphe/test1.col"

graphe  = ls.lire_graphe_col(fichier)
print("Graphe : ", graphe)


coloration = wp.welsh_Powell(graphe)

print("Coloration : ", coloration)

graphe_colore = ls.graphe_colorie(graphe, coloration)
print("Graphe coloré : ", graphe_colore)

score = wp.evaluer_coloration(graphe, {})
print("Score : ", score)

ls.exporter_graphe_colore(graphe_colore, "graphe/test1_colore.col")

graphe2 = ls.lire_graphe_colore("graphe/test1_colore.col")


print("Graphe 2 : ", graphe2)