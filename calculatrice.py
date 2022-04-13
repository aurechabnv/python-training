nombre1 = input("Entrez un premier nombre : ")
if (nombre1.isdigit() == False):
    print("Veuillez indiquer un chiffre valide.")
    nombre1 = input("Entrez un premier nombre : ")

nombre2 = input("Entrez un deuxième nombre : ")

if (nombre2.isdigit() == False):
    print("Veuillez indiquer un chiffre valide.")
    nombre2 = input("Entrez un deuxième nombre : ")

print(f"Le résultat de l'addition du nombre {nombre1} avec le nombre {nombre2} est égal à {int(nombre1) + int(nombre2)}")