# Suivie du projet

**22/12/2024**

Jade :

J'aimerai bien que tu m'expliques en détail tout ce que tu importes parce que j'ai du mal à comprends l'utilité des bibliothèques. De ce que j'ai compris :

- Graphviz : c'est pour transféré nos graphes en image
- NetworkX : j'ai l'impression que c'est une bibliothèque que tu implémentes pour gérer les graphes, je la connais pas du tout je vais essayer de me renseigner.

Dans tous les cas, est ce que tu as fais une commande pour l'implémenter dans ton VScode ? Si oui, je veux bien les avoir pour être à jour avec toi.

Je suis pas hyper convaincu par les objets état/transition en revanche, mais j'ai un piste à ce propos : d'après le bouquin que j'ai récupéré, il existe pleins de manière différente de représenter des graphes. Moi il liste 4 manières : matrice d'incidence, deux tableaux, matrice d'adjacence, liste de successeurs.

En terme de consommation de mémoire et de manipulation, c'est visiblement la liste de successeurs qui est la plus adaptée (même si je trouve que c'est la moins "visuelle").Au delà de ça, vu que c'est la plus simple pour parcourir les voisins d'un sommet, ça sera plus simple pour vérifier que tous les voisins sont pas de la même couleur par exemple. Je pense que c'est le meilleure moyen. Donc je vois pour implémenter ça en fonction de ce que tu as déjo fait.

J'ai du coups créé un fichier liste_successeur qui vient créer la liste de successeurs d'un graphe.
Je te donne un exemple de comment ça rends une liste de successeurs avec le fichier test1.col :
Graphe lu avec succès :
1 -> 2, 3
2 -> 1, 3, 4  
3 -> 1, 2, 4  
4 -> 2, 3

Pour les algorithmes à choisir, je sais pas trop vers quoi on peut s'orienter, dis moi ce que tu préfères (j'arrive pas à savoir notamment si on peut en choisir 2 du Greedy Search)

J'attends que tu m'ais vite fait expliqué ta vision sur le projet (pourquoi les objets états, transistion, etc, pourquoi faire et dans quel but ?) avant de modifier quoi que ce soit ^^ Lundi on peut voir pour s'organiser vite fait appel si tu veux mais je pourrais pas la faire longue :) mais ça peut valoir le coups parce qu'après il faudra attendre le 25 :)
D'ailleurs pour info, j'aurai tendance à travailler sur le projet le soir ou le midi pendant mes pauses

**16/12/2024**

Clément :

- Création du Git
- Création du fichier etat.py contenant la classe Etat. Elle permet de créer des états avec un nom.
- Création du fichier transition.py contenant la classe Transition. Elle permet de créer des transitions avec un état de départ et un état d'arrivée.
- Création du fichier graphe.py contenant la classe graphe. Elle permet de créer des automates avec une liste d'états et une liste de transitions.
- Création du fichier main.py contenant un exemple d'utilisation des classes précédentes.

_Dans le fichier graphe.py_

- ajout de la méthode ajouter_etat(self, etat) qui permet d'ajouter un état à la liste d'états du graphe.
- ajout de la méthode ajouter_transition(self, transition) qui permet d'ajouter une transition à la liste de transitions du graphe.
- ajout de la méthode **str**(self) qui permet d'afficher les états et les transitions du graphe.
- ajout de la méthode to_dot(self) qui permet de générer un fichier un contenu au format dot pour visualiser le graphe.
- ajout de la méthode to_png(self, filename) qui permet de générer un fichier png à partir du fichier dot.
- ajout de la méthode exporter(self, filename) qui permet d'exporter le graphe au format txt.
- ajout de la méthode importer(self, filename) qui permet d'importer un graphe à partir d'un fichier txt.
- **19/12/2024**

Clément :

- Créaion de la méthode lireDimacs(self, filename) qui permet de lire un fichier au format Dimacs et d'intégrer les informations dans un graphe avec la bibliothèque Networkx.
- Création de la méthode creerGrapheDIacs(self, filename) qui permet de créer un graphe à partir d'un fichier au format Dimacs en utilisant la méthode lireDimacs(self, filename). Les données sont ensuite ensuite rentrée dans nos classes Etat et Transition pour les utilisées dans notre classe Graphe.
- Suppression de la méthode exporter(self, filename) qui n'était pas utile.
- Supression de la méthode importer(self, filename) qui n'était pas utile.
