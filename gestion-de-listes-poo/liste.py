import logging
import json
import os

from constants import DATA_DIR

LOGGER = logging.getLogger()

class Liste(list): # hérite de list
    def __init__(self, nom):
        self.nom = nom
        self.chemin = os.path.join(DATA_DIR, f"{self.nom}.json")
        if os.path.exists(self.chemin):
            with open(self.chemin, "r") as f:
                self.extend(json.load(f))
    
    def ajouter(self, element):
        if not isinstance(element, str):
            raise ValueError("Vous ne pouvez ajouter que des chaînes de caractères.")
        
        if element in self:
            LOGGER.error(f"{element} est déjà dans la liste.")
            return False
        
        self.append(element)
        LOGGER.info(f"{element} a été ajouté à la liste.")
        return True

    def enlever(self, element):
        if element in self:
            self.remove(element)
            LOGGER.info(f"{element} a été retiré de la liste.")
            return True
        LOGGER.info(f"{element} n'existe pas.")
        return False
    
    def afficher(self):
        print(f"Ma liste de {self.nom} :")
        for element in self:
            print(f" - {element}")
    
    def sauvegarder(self):
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)

        with open(self.chemin, "w") as f:
            json.dump(self, f, indent=4)
        
        LOGGER.info(f"La liste de {self.nom} a été sauvegardée.")
        return True

if __name__ == "__main__":
    liste = Liste("courses")
    resultat = liste.ajouter("Pommes")
    resultat = liste.ajouter("Poires")
    resultat = liste.ajouter("Citrons")
    liste.afficher()
    liste.sauvegarder()