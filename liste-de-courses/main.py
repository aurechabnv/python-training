# v1
# Version simple de la liste de courses
# Création d'une liste en mémoire avec ajout/retrait d'éléments
# Pas de sauvegarde sur le disque

import sys

liste_de_courses = []
instructions = """------------------------------------------
Choisissez parmi les 5 options suivantes :
1: Ajouter un élément à la liste
2: Retirer un élément à la liste
3: Afficher la liste
4: Vider la liste
5: Quitter"""

print("""------------------------------------------
----------- Ma liste de courses ----------""")

while True:
    # Afficher l'énoncé en multi-lignes
    print(instructions)

    # Demander à l'utilisateur d'entrer un chiffre
    action = input("\u261b Votre choix : ")

    # Si pas un chiffre
    if not action.isdigit():
        # Afficher un message d'erreur
        print("Veuillez entrer un chiffre valide !")
        # Revenir au début
        continue

    # Si 5 - QUITTER
    if int(action) == 5:
        # Quitter le programme
        sys.exit()

    # Si 1 - AJOUTER
    elif int(action) == 1:
        # Demander l'élément à ajouter
        element = input("Entrez le nom de l'élément à ajouter : ")
        # Ajouter l'élément
        liste_de_courses.append(element)
        # Afficher un message
        print(f"L'élément {element} a bien été ajouté à la liste de courses.")
        # Revenir au début
        continue

    # Si 2 - RETIRER
    elif int(action) == 2:
        # Demander l'élément à retirer
        element = input("Entrez le nom de l'élément à retirer : ")
        # SI l'élément existe dans la liste
        if element in liste_de_courses:
            # Retirer l'élément
            liste_de_courses.remove(element)
            # Afficher un message
            print(f"L'élément {element} a bien été retiré de la liste de courses.")
            # Revenir au début
            continue
        # SI n'existe pas
        else:
            # Afficher un message
            print(f"L'élément {element} ne fait pas partie de la liste de courses.")
            # Revenir au début
            continue

    # Si 3 - AFFICHER
    elif int(action) == 3:
        # Si la liste n'est pas vide
        if len(liste_de_courses) > 0:
            # Enumérer le contenu de la liste en démarrant à 1
            for i, element in enumerate(liste_de_courses):
                print(f"{i+1}. {element}")
            # Revenir au début
            continue
        # Sinon
        else:
            # Afficher un message
            print("La liste de courses ne contient aucun élément.")
            # Revenir au début
            continue

    # Si 4 - VIDER
    elif int(action) == 4:
        # Si la liste n'est pas vide
        if len(liste_de_courses) > 0:
            # Vider la liste
            liste_de_courses.clear()
            # Afficher un message
            print("La liste de courses a bien été vidée.")
            # Revenir au début
            continue
        # Sinon
        else:
            # Afficher un message
            print("La liste de courses est déjà vide.")
            # Revenir au début
            continue
    
    # Si un autre chiffre
    else:
        # Afficher un message
        print("Cette option n'est pas disponible.")
        # Revenir au début
        continue