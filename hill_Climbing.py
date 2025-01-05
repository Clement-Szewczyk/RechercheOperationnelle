import random
import time
import liste_successeur as ls
import welsh_Powell as wp


# Fonction pour générer une solution initiale
def initialiser_coloration(graphe):
    print("Initialisation de la coloration...")
    coloration = {sommet: random.randint(0, len(graphe) - 1) for sommet in graphe}
    print("Coloration initiale :", coloration)
    return coloration



# Fonction pour calculer les conflits dans une coloration
def compter_conflits(graphe, coloration):
    conflits = 0
    for sommet, voisins in graphe.items():
        for voisin in voisins:
            if coloration[sommet] == coloration[voisin]:
                conflits += 1
    return conflits // 2  # Chaque conflit est compté deux fois

# Fonction pour réduire activement le nombre de couleurs
def reduire_nombre_couleurs(graphe, coloration):
    print("Réduction active du nombre de couleurs...")
    couleurs_utilisees = set(coloration.values())
    for couleur in sorted(couleurs_utilisees):
        sommets_a_recolorier = [sommet for sommet, col in coloration.items() if col == couleur]
        for sommet in sommets_a_recolorier:
            for nouvelle_couleur in range(len(couleurs_utilisees)):
                if nouvelle_couleur != couleur:
                    coloration[sommet] = nouvelle_couleur
                    if compter_conflits(graphe, coloration) == 0:
                        break
            else:
                coloration[sommet] = couleur  # Restaurer si aucune couleur n'était valide
    print("Nouvelle coloration après réduction :", coloration)
    return coloration

# Fonction pour trouver une meilleure solution dans le voisinage
def ameliorer_coloration(graphe, coloration):
    print("Amélioration de la coloration...")
    meilleure_coloration = coloration.copy()
    meilleur_score = compter_conflits(graphe, coloration)
    print("Score actuel :", meilleur_score)

    for sommet in graphe:
        couleur_actuelle = coloration[sommet]
        for nouvelle_couleur in range(len(graphe)):
            if nouvelle_couleur != couleur_actuelle:
                coloration[sommet] = nouvelle_couleur
                score = compter_conflits(graphe, coloration)
                if score < meilleur_score:
                    meilleure_coloration = coloration.copy()
                    meilleur_score = score
        coloration[sommet] = couleur_actuelle  # Restaurer la couleur initiale

    print("Meilleur score après amélioration :", meilleur_score)
    return meilleure_coloration, meilleur_score

def hill_climbing_pasopti(graphe, max_iterations=1000, perturbation_prob=0.1):
    print("Démarrage de l'algorithme de Hill Climbing...")
    coloration = initialiser_coloration(graphe)
    conflits = compter_conflits(graphe, coloration)
    print("Conflits initiaux :", conflits)
    iterations = 0
    debut = time.time()

    while conflits > 0 and iterations < max_iterations:
        print(f"\nIteration {iterations + 1}...")
        nouvelle_coloration, nouveau_score = ameliorer_coloration(graphe, coloration)
        if nouveau_score < conflits:
            print("Amélioration trouvée. Mise à jour de la coloration.")
            coloration = nouvelle_coloration
            conflits = nouveau_score
        else:
            # Perturbation aléatoire pour échapper aux optima locaux
            if random.random() < perturbation_prob:
                sommet = random.choice(list(graphe.keys()))
                ancienne_couleur = coloration[sommet]
                coloration[sommet] = random.randint(0, len(graphe) - 1)
                print(f"Perturbation aléatoire : sommet {sommet} changé de couleur {ancienne_couleur} à {coloration[sommet]}.")

        # Réduction active des couleurs
        coloration = reduire_nombre_couleurs(graphe, coloration)
        iterations += 1

    temps_execution = time.time() - debut
    nombre_couleurs = len(set(coloration.values()))
    print("\nNombre de couleurs utilisées :", nombre_couleurs)
    print("Conflits restants après convergence :", conflits)
    return {
        "coloration": coloration,
        "conflits": conflits,
        "iterations": iterations,
        "temps_execution": temps_execution,
        "nombre_couleurs": nombre_couleurs,
    }

def hill_climbing_opti(graphe, max_iterations=1000, perturbation_prob=0.1):
    print("Démarrage de l'algorithme de Hill Climbing...")
    coloration, temps_initialisation = wp.welsh_Powell(graphe)
    print(f"Initialisation par Welsh-Powell effectuée en {temps_initialisation:.8f} secondes.")
    conflits = compter_conflits(graphe, coloration)
    print("Conflits initiaux :", conflits)
    iterations = 0
    debut = time.time()

    while conflits > 0 and iterations < max_iterations:
        print(f"\nIteration {iterations + 1}...")
        nouvelle_coloration, nouveau_score = ameliorer_coloration(graphe, coloration)
        if nouveau_score < conflits:
            print("Amélioration trouvée. Mise à jour de la coloration.")
            coloration = nouvelle_coloration
            conflits = nouveau_score
        else:
            # Perturbation aléatoire pour échapper aux optima locaux
            if random.random() < perturbation_prob:
                sommet = random.choice(list(graphe.keys()))
                ancienne_couleur = coloration[sommet]
                coloration[sommet] = random.randint(0, len(graphe) - 1)
                print(f"Perturbation aléatoire : sommet {sommet} changé de couleur {ancienne_couleur} à {coloration[sommet]}.")

        # Réduction active des couleurs
        coloration = reduire_nombre_couleurs(graphe, coloration)
        iterations += 1

    temps_execution = time.time() - debut
    nombre_couleurs = len(set(coloration.values()))
    print("\nNombre de couleurs utilisées :", nombre_couleurs)
    print("Conflits restants après convergence :", conflits)
    return {
        "coloration": coloration,
        "conflits": conflits,
        "iterations": iterations,
        "temps_execution": temps_execution,
        "nombre_couleurs": nombre_couleurs,
    }


# Exemple d'utilisation
if __name__ == "__main__":
    chemin_fichier = 'graphe/queen9_9.col'  # Remplacez par votre fichier
    graphe = ls.lire_graphe_col(chemin_fichier)

    if graphe:
        resultat = hill_climbing_opti(graphe, max_iterations=10000, perturbation_prob=0.05)
        print("\nRésultats finaux :")
        print("Coloration finale :", resultat["coloration"])
        print("Conflits restants :", resultat["conflits"])
        print("Nombre d'itérations :", resultat["iterations"])
        print("Temps d'exécution :", resultat["temps_execution"], "secondes")
        print("Nombre de couleurs utilisées :", resultat["nombre_couleurs"])
    else:
        print("Erreur lors de la lecture du graphe.")
