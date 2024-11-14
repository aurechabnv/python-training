import random

ACTION_ATTACK = 1
ACTION_HEAL = 2
AVAILABLE_ACTIONS = [ACTION_ATTACK, ACTION_HEAL]

# passer tout en constantes
MAX_HEALTH = 50
PLAYER_DAMAGE_MIN = 5
PLAYER_DAMAGE_MAX = 10
ENEMY_DAMAGE_MIN = 5
ENEMY_DAMAGE_MAX = 15
HEALING_MIN = 15
HEALING_MAX = 50

enemy_health = MAX_HEALTH
player_health = MAX_HEALTH
player_potions = 3
player_healed = False

while True:
    # ACTION JOUEUR
    if player_healed:
        print("Vous passez votre tour...")
        player_healed = False
    else:
        player_action = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")

        if not player_action.isdigit():
            print("Veuillez entrer un nombre valide")
            continue

        player_action = int(player_action) # enregistrer le int pour éviter le répéter
        if player_action not in AVAILABLE_ACTIONS:
            print("Action non valide")
            continue

        if player_action_int == ACTION_ATTACK:
            damage = random.randint(PLAYER_DAMAGE_MIN, PLAYER_DAMAGE_MAX)
            enemy_health -= damage
            print(f"Vous avez infligé {damage} points de dégâts à l'ennemi.")
        
        elif player_action_int == ACTION_HEAL:
            if player_potions > 0:
                healing = random.randint(HEALING_MIN, HEALING_MAX)
                player_health = min(player_health + healing, MAX_HEALTH) # éviter de guérir au delà de la vie max
                player_potions -= 1            
                player_healed = True
                print(f"Vous avez regagné {healing} points de vie ({player_potions} potion{'s' if player_potions > 1 else ''} restante{'s' if player_potions > 1 else ''}).")
            else:
                print("Vous n'avez plus de potions...")
                continue
    
    # ACTION ENNEMI
    if enemy_health > 0:
        damage = random.randint(ENEMY_DAMAGE_MIN, ENEMY_DAMAGE_MAX)
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