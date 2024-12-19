# Suivie du projet


**16/12/2024**

Clément : 

- Création du Git
- Création du fichier etat.py contenant la classe Etat. Elle permet de créer des états avec un nom. 
- Création du fichier transition.py contenant la classe Transition. Elle permet de créer des transitions avec un état de départ et un état d'arrivée.
- Création du fichier graphe.py contenant la classe graphe. Elle permet de créer des automates avec une liste d'états et une liste de transitions.
- Création du fichier main.py contenant un exemple d'utilisation des classes précédentes.

*Dans le fichier graphe.py*

-  ajout de la méthode ajouter_etat(self, etat) qui permet d'ajouter un état à la liste d'états du graphe.
-  ajout de la méthode ajouter_transition(self, transition) qui permet d'ajouter une transition à la liste de transitions du graphe.
-  ajout de la méthode __str__(self) qui permet d'afficher les états et les transitions du graphe.
-  ajout de la méthode to_dot(self) qui permet de générer un fichier un contenu au format dot pour visualiser le graphe.
-  ajout de la méthode to_png(self, filename) qui permet de générer un fichier png à partir du fichier dot.
-  ajout de la méthode exporter(self, filename) qui permet d'exporter le graphe au format txt.
-  ajout de la méthode importer(self, filename) qui permet d'importer un graphe à partir d'un fichier txt.
-  

**19/12/2024**

Clément :

- Créaion de la méthode lireDimacs(self, filename) qui permet de lire un fichier au format Dimacs et d'intégrer les informations dans un graphe avec la bibliothèque Networkx.
- Création de la méthode creerGrapheDIacs(self, filename) qui permet de créer un graphe à partir d'un fichier au format Dimacs en utilisant la méthode lireDimacs(self, filename). Les données sont ensuite ensuite rentrée dans nos classes Etat et Transition pour les utilisées dans notre classe Graphe.
- Suppression de la méthode exporter(self, filename) qui n'était pas utile.
- Supression de la méthode importer(self, filename) qui n'était pas utile.