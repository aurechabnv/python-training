# v2
# Gestion de liste de courses
# avec sauvegarde sur le disque dur

import json
import os
import sys

CUR_DIR = os.path.dirname(__file__)
CHEMIN_LISTE = os.path.join(CUR_DIR, "liste.json")
AJOUTER, RETIRER, AFFICHER, VIDER, QUITTER = 1, 2, 3, 4, 5

INSTRUCTIONS = f"""Choisissez parmi les 5 options suivantes :
{AJOUTER}: Ajouter un élément à la liste
{RETIRER}: Retirer un élément à la liste
{AFFICHER}: Afficher la liste
{VIDER}: Vider la liste
{QUITTER}: Quitter
\u261b Votre choix : """

if os.path.exists(CHEMIN_LISTE):
    with open(CHEMIN_LISTE, "r") as f:
        liste_de_courses = json.load(f)
else:
    liste_de_courses = []

print("~o~" * 5 + " Ma liste de courses " + "~o~" * 5)

while True:
    action = input(INSTRUCTIONS)

    if not action.isdigit():
        print("Veuillez entrer un chiffre valide !")

    elif int(action) == AJOUTER:
        element = input("Entrez le nom de l'élément à ajouter : ")
        liste_de_courses.append(element)
        print(f"L'élément {element} a bien été ajouté à la liste de courses.")

    elif int(action) == RETIRER:
        element = input("Entrez le nom de l'élément à retirer : ")
        if element in liste_de_courses:
            liste_de_courses.remove(element)
            print(f"L'élément {element} a bien été retiré de la liste de courses.")
        else:
            print(f"L'élément {element} ne fait pas partie de la liste de courses.")

    elif int(action) == AFFICHER:
        if len(liste_de_courses) > 0:
            for i, element in enumerate(liste_de_courses):
                print(f"{i+1}. {element}")
        else:
            print("La liste de courses ne contient aucun élément.")

    elif int(action) == VIDER:
        if len(liste_de_courses) > 0:
            liste_de_courses.clear()
            print("La liste de courses a bien été vidée.")
        else:
            print("La liste de courses est déjà vide.")

    elif int(action) == QUITTER:
        with open(CHEMIN_LISTE, "w") as f:
            json.dump(liste_de_courses, f)
        print("A bientôt !")
        sys.exit()
    
    else:
        print("Cette option n'est pas disponible.")
    
    print("-" * 40)