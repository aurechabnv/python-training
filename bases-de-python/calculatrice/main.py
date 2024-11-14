a = b = ""

while not (a.isdigit() and b.isdigit()):
    a = input("Entrez un premier nombre : ")
    b = input("Entrez un deuxième nombre : ")

    if not (a.isdigit() and b.isdigit()):
        print("Veuillez entrer des chiffres valides.")

print(f"Le résultat de l'addition du nombre {a} avec le nombre {b} est égal à {int(a) + int(b)}")