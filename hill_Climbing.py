import random
import time
import liste_successeur as ls
import welsh_Powell as wp


# Fonction pour générer une solution initiale
def initialiser_coloration(graphe):
    """
    But de la fonction :
    Initialiser une coloration aléatoire pour chaque sommet du graphe.

    :param graphe : Dictionnaire représentant le graphe sous forme de liste d'adjacence.
    :return coloration : Dictionnaire {sommet: couleur} avec des couleurs aléatoires.
    """
    print("Initialisation de la coloration...")
    coloration = {sommet: random.randint(0, len(graphe) - 1) for sommet in graphe}
    print("Coloration initiale :", coloration)
    return coloration

# Fonction pour calculer les conflits dans une coloration
def compter_conflits(graphe, coloration):
    """
    But de la fonction :
    Compter le nombre de conflits dans une coloration donnée.

    :param graphe : Dictionnaire représentant le graphe.
    :param coloration : Dictionnaire {sommet: couleur} représentant la coloration actuelle.
    :return conflits : Nombre total de conflits détectés dans le graphe.
    """
    conflits = 0
    for sommet, voisins in graphe.items():
        for voisin in voisins:
            if coloration[sommet] == coloration[voisin]:
                conflits += 1
    return conflits // 2  # Chaque conflit est compté deux fois

# Fonction pour réduire activement le nombre de couleurs
def reduire_nombre_couleurs(graphe, coloration):
    """
    But de la fonction :
    Réduire le nombre de couleurs utilisées dans une coloration en minimisant les conflits.

    :param graphe : Dictionnaire représentant le graphe.
    :param coloration : Dictionnaire {sommet: couleur} représentant la coloration actuelle.
    :return coloration : Nouvelle coloration avec potentiellement moins de couleurs.
    """
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
    """
    But de la fonction :
    Améliorer la coloration actuelle en explorant les couleurs possibles pour chaque sommet.

    :param graphe : Dictionnaire représentant le graphe.
    :param coloration : Dictionnaire {sommet: couleur} représentant la coloration actuelle.
    :return meilleure_coloration : Dictionnaire {sommet: couleur} amélioré.
    :return meilleur_score : Nombre de conflits restants dans la meilleure coloration trouvée.
    """
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

# Hill Climbing avec initialisation aléatoire
def hill_climbing_pasopti(graphe, max_iterations=1000, perturbation_prob=0.1):
    """
    But de la fonction :
    Résoudre le problème de coloration de graphe avec Hill Climbing avec initialisation aléatoire.

    :param graphe : Dictionnaire représentant le graphe.
    :param max_iterations : Nombre maximum d'itérations autorisées.
    :param perturbation_prob : Probabilité de perturbation aléatoire pour échapper aux optima locaux.
    :return : Dictionnaire contenant la coloration finale, les conflits restants, le nombre d'itérations, le temps d'exécution et le nombre de couleurs utilisées.
    """
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
    return {
        "coloration": coloration,
        "conflits": conflits,
        "iterations": iterations,
        "temps_execution": temps_execution,
        "nombre_couleurs": nombre_couleurs,
    }

def forcer_conflits_progressif(coloration, max_couleurs, proportion=0.1):
    """
    Introduit des conflits en modifiant la couleur d'un pourcentage des sommets.
    :param coloration: Dictionnaire {sommet: couleur}.
    :param max_couleurs: Nombre maximum de couleurs à utiliser.
    :param proportion: Proportion des sommets à perturber (ex. 0.1 pour 10%).
    :return: Nouvelle coloration avec quelques conflits introduits.
    """
    print(f"Forçage progressif de conflits sur {proportion*100:.1f}% des sommets.")
    sommets = list(coloration.keys())
    nombre_a_modifier = max(1, int(len(sommets) * proportion))  # Nombre de sommets à perturber
    sommets_a_modifier = random.sample(sommets, nombre_a_modifier)

    for sommet in sommets_a_modifier:
        ancienne_couleur = coloration[sommet]
        nouvelle_couleur = random.randint(0, max_couleurs - 1)
        while nouvelle_couleur == ancienne_couleur:  # Évite de réassigner la même couleur
            nouvelle_couleur = random.randint(0, max_couleurs - 1)
        coloration[sommet] = nouvelle_couleur
        print(f"Sommet {sommet} : couleur modifiée de {ancienne_couleur} à {nouvelle_couleur}")

    return coloration


# Hill Climbing avec initialisation Welsh Powell
def hill_climbing_opti(graphe, max_iterations=1000, perturbation_prob=0.1, max_couleurs=3):
    """
    Résoudre le problème de coloration de graphe avec Hill Climbing en initialisant la solution avec Welsh-Powell et en ajoutant une perturbation initiale.

    :param graphe : Dictionnaire représentant le graphe.
    :param max_iterations : Nombre maximum d'itérations autorisées.
    :param perturbation_prob : Probabilité de perturbation aléatoire.
    :param max_couleurs : Nombre maximum de couleurs à utiliser.
    :return : Dictionnaire contenant la coloration finale, les conflits restants, le nombre d'itérations, le temps d'exécution et le nombre de couleurs utilisées.
    """
    print("Démarrage de l'algorithme de Hill Climbing...")
    coloration, temps_initialisation = wp.welsh_Powell(graphe)

    # Forçage progressif pour créer une pente modérée
    coloration = forcer_conflits_progressif(coloration, max_couleurs, proportion=0.1)
    conflits = compter_conflits(graphe, coloration)
    print("Conflits initiaux après forçage progressif :", conflits , "\n")

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
                coloration[sommet] = random.randint(0, max_couleurs - 1)
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