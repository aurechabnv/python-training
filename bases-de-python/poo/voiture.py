from dataclasses import dataclass

@dataclass
class Voiture:
    essence: float = 100.0

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