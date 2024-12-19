from etat import Etat
from transition import Transition
from graphviz import Digraph
import networkx as nx

class Graphe:

    def __init__(self):
        self.etats = []
        self.transitions = []

    def ajouter_etat(self, nom ):
        etat = Etat(nom)
        self.etats.append(etat)
        
    def ajouter_transition(self, depart, arrive):
        transition = Transition(depart, arrive)
        self.transitions.append(transition)
    
    def __str__(self):
        result = 'Etats:\n'
        for etat in self.etats:
            result += f'{etat}\n'
        result += 'Transitions:\n'
        result += '----------------\n'
        for transition in self.transitions:
            result += f'{transition}\n'
        return  result
        
        
    def to_dot(self):
        dot = Digraph()
        for etat in self.etats:
            dot.node(etat.nom , shape='circle')
        for transition in self.transitions:
            dot.edge(transition.depart, transition.arrive)
        return dot 
    
    def to_png(self, filename):
        dot = self.to_dot()
        path = "images/"+filename
        dot.render(path, format='png', cleanup=True)

    
    def lireDimacs(self, filename): 
        graph = nx.Graph()
        with open(filename, 'r') as file:
            for line in file:
                if line.startswith('c'):
                    continue  # Skip comment lines
                elif line.startswith('p'):
                    parts = line.split()
                    num_vertices = int(parts[2])
                    num_edges = int(parts[3])
                elif line.startswith('e'):
                    parts = line.split()
                    u = int(parts[1])
                    v = int(parts[2])
                    graph.add_edge(u, v)
        return graph
    
    def creerGrapheDimacs(self, filename):
        dimacs = self.lireDimacs(filename)
        for node in dimacs.nodes():
            self.ajouter_etat(str(node))
        for edge in dimacs.edges():
            self.ajouter_transition(str(edge[0]), str(edge[1]))



