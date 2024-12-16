from etat import Etat
from transition import Transition
from graphviz import Digraph

class Graphe:

    def __init__(self):
        self.etats = []
        self.transitions = []

    def ajouter_etat(self, nom):
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

    def exporter(self, filename):
        path = "graphe/"+filename
        with open(path, 'w') as file:
            file.write(' '.join([etat.nom for etat in self.etats])+ '\n')
            for transition in self.transitions:
                file.write(f'{transition.depart} {transition.arrive}\n')

    def importer(self, filename):
        with open(filename, 'r') as file:
            etats = file.readline().split()
            for etat in etats:
                self.ajouter_etat(etat)
            for line in file:
                depart, arrive = line.split()
                self.ajouter_transition(depart, arrive)

