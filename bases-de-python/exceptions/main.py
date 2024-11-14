fichier = input("Entrez le chemin d'un fichier à ouvrir : ")

try:
    f = open(fichier, "r")
    print(f.read())
except FileNotFoundError:
    print("Le fichier est introuvable.")
except UnicodeDecodeError:
    print("Impossible d'ouvrir le fichier.")
else:
    f.close()