# Créer un vérificateur d'adresses IP
def ip_checker(ip_address):
    ip_chunks = ip_address.split(".")
    if len(ip_chunks) != 4:
        return False
    for chunk in ip_chunks:
        if not (chunk.isdigit() and int(chunk) in range(0, 256)):
            return False
    return True
"""
print(ip_checker("0.0.0.0"))
print(ip_checker("192.168.0.1"))
print(ip_checker("255.255.255.255"))
print(ip_checker("928.394.201.293"))
print(ip_checker("-392.255.193.2"))
print(ip_checker("192.4.3"))
print(ip_checker("coucou"))
print(ip_checker("abc.def.gfi.jkl"))
"""

# Ordonner une chaîne de caractère
chaine = "Pierre, Julien, Anne, Marie, Lucien"
chaine_liste = chaine.split(", ")
chaine_liste.sort()
chaine_en_ordre = ", ".join(chaine_liste)
# print(chaine)


# Vérificateur de palindrome
mot = "Un roc cornu"
mot_lower = mot.lower().replace(" ", "")

if mot_lower == mot_lower[::-1]:
	resultat = True
else:
	resultat = False
"""
palindrome = mot.replace(" ","").lower()
palindrome_liste = []
for c in palindrome:
    palindrome_liste.append(c)
palindrome_liste.reverse()
palindrome_inverse = "".join(palindrome_liste)
resultat = palindrome == palindrome_inverse
"""

# Vérifier si une phrase est un pangramme
import string
phrase = "Joyeux, ivre, fatigué, le nez qui pique, Clown Hary skie dans l’ombre"
phrase_lower = phrase.lower()
alphabet = list(string.ascii_lowercase)
for c in phrase_lower:
    for c in alphabet:
        alphabet.remove(c)
if alphabet:
    resultat = "La phrase n'est pas un Pangramme"
else:
    resultat = "La phrase est un Pangramme"
"""
pangramme = []
for c in phrase_lower:
    if c in string.ascii_lowercase and c not in pangramme:
        pangramme.append(c)
if len(pangramme) == len(string.ascii_lowercase):
    resultat = "La phrase est un Pangramme"
else:
    resultat = "La phrase n'est pas un Pangramme"
# print(resultat)
"""

# Compter l'occurrence de chaque lettre de l'alphabet dans un texte
lorem = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
		   Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
		   Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
		   Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
alphabet = string.ascii_lowercase
resultat = dict.fromkeys(alphabet, 0)
for c in lorem.lower():
    if c in alphabet:
        resultat[c] += 1
# print(resultat)


# Recréer la méthode isdigit
def isdigit(digit):
    for c in digit:
        try:
            int(digit)
        except:
            return False
    return True
""" 
def isdigit(digit):
    for c in digit:
        if c not in [str(n) for n in range(10)]:
            return False
    return True
"""
resultat = isdigit("1854274")


# Générer un octet aléatoire
import random
octet = [str(random.choice(range(2))) for n in range(8)]
octet = "".join(octet)
# print(type(octet), octet)


# Recréer la méthode split
def separateur(variable, separateur):
    word = ""
    resultat = []
    for c in variable:
        if c != separateur:
            word += c
            continue
        resultat.append(word)
        word = ""
    if word:
        resultat.append(word)
    return resultat
resultat = separateur("bonjour-tout-le-monde", "-")


# Recréer la méthode join
def join(separateur, *args):
    resultat = ""
    for w in args:
        if resultat:
            resultat += separateur
        resultat += w
    return resultat

resultat = join(":", "Bonjour", "tout", "le", "monde")


extensions = ['.py', '.txt', '.jpg', '.txt', '.docx']
resultat = any('py' in ext for ext in extensions)
print(resultat)

