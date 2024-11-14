projets = ["pr_GoT", "HarryPotter", "pr_Avengers"]

class Utilisateur:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
    def __str__(self):
        return f"Utilisateur {self.nom} {self.prenom}"
    
    def afficher_projets(self):
        for projet in projets:
            print(projet)

class Junior(Utilisateur):
    def __init__(self, nom, prenom):
        # Utilisateur.__init__(self, nom, prenom)
        super().__init__(nom, prenom)
    
    def afficher_projets(self):
        for projet in projets:
            if not projet.startswith("pr_"):
                print(projet)

paul = Junior("Paul", "Durand")
print(paul)
paul.afficher_projets()


# EN UTILISANT DATACLASS
from dataclasses import dataclass

@dataclass
class User:
    nom: str
    prenom: str

    def __str__(self):
        return f"User {self.nom} {self.prenom}"
    
    def afficher_projets(self):
        for projet in projets:
            print(projet)

@dataclass
class JuniorDev(User):
    def afficher_projets(self):
        for projet in projets:
            if not projet.startswith("pr_"):
                print(projet)

pierre = JuniorDev("Pierre", "Durand")
print(pierre)
pierre.afficher_projets()
