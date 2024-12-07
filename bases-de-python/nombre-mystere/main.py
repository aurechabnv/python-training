# JEU DU NOMBRE MYSTERE
# L'ordinateur va choisir un nombre entre 1 et 100
# Notre objectif va être de le trouver avec un nombre limité d'essais : 5

import random

NOMBRE_MYSTERE = random.randint(1, 100)
NB_ESSAIS_MAX = 5
nb_essais = 0

print("~*~ Nombre Mystère ~*~")

# Début de la boucle
while nb_essais < NB_ESSAIS_MAX:
    nombre = input(f"""Il te reste {NB_ESSAIS_MAX - nb_essais} essai{"s" if NB_ESSAIS_MAX - nb_essais > 1 else ""}.
Devine le nombre : """)

    if not nombre.isdigit():
        print("Veuillez entrer un nombre valide.")
        continue
    else:
        nb_essais += 1

    nombre = int(nombre)
    if nombre == NOMBRE_MYSTERE:
        print(f"""Bravo ! Le nombre mystère était bien {NOMBRE_MYSTERE}.
Tu as trouvé en {nb_essais} essai{"s" if nb_essais > 1 else ""}.""")
        break
    elif nombre < NOMBRE_MYSTERE:
        print(f"Le nombre mystère est plus grand que {nombre}.")
    elif nombre > NOMBRE_MYSTERE:
        print(f"Le nombre mystère est plus petit que {nombre}.")

# Boucle finie, nombre d'essais max atteint
else:
    print(f"Dommage ! Le nombre mystère était {NOMBRE_MYSTERE}.")

print("Fin du jeu.")