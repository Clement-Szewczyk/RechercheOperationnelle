from graphe import Graphe

graphe = Graphe()
graphe.ajouter_etat('A')
graphe.ajouter_etat('B')
graphe.ajouter_etat('C')
graphe.ajouter_transition('A', 'B')
graphe.ajouter_transition('B', 'C')
graphe.ajouter_transition('C', 'A')
print(graphe)

graphe.to_png('graphe')

graphe.exporter('graphe.txt')

graphe2 = Graphe()
graphe2.importer('graphe/graphe2.txt')

graphe2.to_png('graphe2')

print(graphe2)

