import random

ACTION_ATTACK = 1
ACTION_HEAL = 2
AVAILABLE_ACTIONS = [ACTION_ATTACK, ACTION_HEAL]

enemy_health = 50
player_health = 50
player_potions = 3
player_healed = False

while True:
    # ACTION JOUEUR
    if player_healed:
        print("Vous passez votre tour...")
        player_healed = False
    else:
        player_action = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")

        if not player_action.isdigit() or int(player_action) not in AVAILABLE_ACTIONS:
            continue
        elif int(player_action) == ACTION_ATTACK:
            damage = random.randint(5, 10)
            enemy_health -= damage
            print(f"Vous avez infligé {damage} points de dégâts à l'ennemi.")
        elif int(player_action) == ACTION_HEAL and player_potions > 0:
            healing = random.randint(15, 50)
            player_health += healing
            player_potions -= 1            
            player_healed = True
            print(f"Vous avez regagné {healing} points de vie ({player_potions} potion{'s' if player_potions > 1 else ''} restante{'s' if player_potions > 1 else ''}).")
        else:
            print("Vous n'avez plus de potions...")
            continue
    
    # ACTION ENNEMI
    if enemy_health > 0:
        damage = random.randint(5, 15)
        player_health -= damage
        print(f"L'ennemi vous a infligé {damage} points de dégâts.")
    else:
        print("Vous avez gagné !")
        break
    
    if player_health <= 0:
        print("Vous n'avez plus de points de vie. Vous avez perdu !")
        break

    print(f"""Il vous reste {player_health} points de vie.
Il reste {enemy_health} points de vie à l'ennemi.""")
    print("-" * 30)

print("Fin du jeu.")