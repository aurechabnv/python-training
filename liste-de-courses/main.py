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
    print(instructions)
    action = input("\u261b Votre choix : ")

    if not action.isdigit():
        print("Veuillez entrer un chiffre valide !")
        continue

    # Si 5 - QUITTER
    if int(action) == 5:
        sys.exit()

    # Si 1 - AJOUTER
    elif int(action) == 1:
        element = input("Entrez le nom de l'élément à ajouter : ")
        liste_de_courses.append(element)
        print(f"L'élément {element} a bien été ajouté à la liste de courses.")
        continue

    # Si 2 - RETIRER
    elif int(action) == 2:
        element = input("Entrez le nom de l'élément à retirer : ")
        if element in liste_de_courses:
            liste_de_courses.remove(element)
            print(f"L'élément {element} a bien été retiré de la liste de courses.")
            continue
        else:
            print(f"L'élément {element} ne fait pas partie de la liste de courses.")
            continue

    # Si 3 - AFFICHER
    elif int(action) == 3:
        if len(liste_de_courses) > 0:
            for i, element in enumerate(liste_de_courses):
                print(f"{i+1}. {element}")
            continue
        else:
            print("La liste de courses ne contient aucun élément.")
            continue

    # Si 4 - VIDER
    elif int(action) == 4:
        if len(liste_de_courses) > 0:
            liste_de_courses.clear()
            print("La liste de courses a bien été vidée.")
            continue
        else:
            print("La liste de courses est déjà vide.")
            continue
    
    # Si un autre chiffre
    else:
        print("Cette option n'est pas disponible.")
        continue