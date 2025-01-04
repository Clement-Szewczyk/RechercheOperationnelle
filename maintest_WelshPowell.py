import liste_successeur as ls
import welsh_Powell as wp


graphe = {}
fichier = "graphe/DSJC1000.9.col"

graphe  = ls.lire_graphe_col(fichier)
#print("Graphe : ", graphe)

print("Nombre de sommets :", len(graphe))
print("Nombre d'arêtes :", sum(len(voisins) for voisins in graphe.values()) // 2)

coloration, temps = wp.welsh_Powell(graphe)
print("Fichier : ", fichier)
#print("Coloration : ", coloration)
print("Temps d'exécution : ", temps)
nb_couleur = wp.nb_couleur(coloration)
print("Nombre de couleurs : ", nb_couleur)


graphe_colore = ls.graphe_colorie(graphe, coloration)
#print("Graphe coloré : ", graphe_colore)

score = ls.evaluer_coloration(graphe_colore)
print("Score : ", score)



