from dataclasses import dataclass
from typing import ClassVar

@dataclass
class Voiture:
    marque: str
    vitesse: int
    prix: int
    essence: float = 100.0
    total: ClassVar[int] = 0

    def __post_init__(self):
        Voiture.total += 1
    
    def __str__(self):
        return f"Voiture de marque {self.marque} avec une vitesse maximale de {self.vitesse}"
    
    @classmethod
    def lamborghini(cls):
        return cls(marque="Lamborghini", vitesse=240, prix=200_000)
    
    @classmethod
    def porsche(cls):
        return cls(marque="Porsche", vitesse=200, prix=180_000)
    
    @staticmethod
    def afficher_nombre_voitures():
        print(f"Vous avez {Voiture.total} voitures dans votre garage")

    def afficher_reservoir(self):
        if self.essence <= 0:
            print("Vous n'avez plus d'essence, faites le plein !")
        else:
            if self.essence < 10:
                print("Vous n'avez bientôt plus d'essence !")
            print(f"La voiture contient {self.essence} litres d’essence")

    def roule(self, km):
        if self.essence > 0:
            self.essence -= (km * 5) / 100
        self.afficher_reservoir()

    def faire_plein(self):
        self.essence = 100
        print("Vous pouvez repartir !")

voiture1 = Voiture.lamborghini()
voiture2 = Voiture.porsche()
print(voiture1)
print(voiture2)
Voiture.afficher_nombre_voitures()