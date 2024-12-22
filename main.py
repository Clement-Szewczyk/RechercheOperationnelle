from graphe import Graphe

graphe = Graphe()
graphe.creerGrapheDimacs('test3.col')

print(graphe)
graphe.to_png('graphe_dimacs')