import logging
import json
from pathlib import Path

from constants import DATA_DIR

LOGGER = logging.getLogger()
logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s: %(message)s')

class Liste(list): # hérite de list
    def __init__(self, nom):
        self.nom = nom
        self.chemin = DATA_DIR / Path(f"{self.nom}.json")
        if Path(self.chemin).exists():
            with open(self.chemin, "r") as f:
                self.extend(json.load(f))
            LOGGER.debug(f"Liste chargée depuis le fichier {self.chemin}")
    
    def ajouter(self, element):
        if not isinstance(element, str):
            LOGGER.error("Vous ne pouvez ajouter que des chaînes de caractères.")
            return False
        
        if element in self:
            LOGGER.warning(f"'{element}' est déjà dans la liste.")
            return False
        
        self.append(element)
        LOGGER.info(f"'{element}' a été ajouté à la liste.")
        return True

    def enlever(self, element):
        if element not in self:
            LOGGER.warning(f"'{element}' n'existe pas.")
            return False
        self.remove(element)
        LOGGER.info(f"'{element}' a été retiré de la liste.")
        return True
    
    def afficher(self):
        result = f"Ma liste de {self.nom} :"
        for element in self:
            result += f"\n - {element}"
        if len(self) == 0:
            result += "\n C'est vide..."
        print(result)
    
    def sauvegarder(self):
        Path(DATA_DIR).mkdir(exist_ok=True)
        with open(self.chemin, "w") as f:
            json.dump(self, f, indent=4, ensure_ascii=False)
        
        LOGGER.info(f"La liste de {self.nom} a été sauvegardée.")
        return True

    def vider(self):
        self.clear()
        LOGGER.info(f"La liste de {self.nom} a été vidée.")
        return True

if __name__ == "__main__":
    liste0 = Liste("taches")
    liste0.vider()
    liste0.afficher()
"""
     liste = Liste("courses")
    liste.vider()
    liste.ajouter(123)
    liste.ajouter("Lait")
    liste.enlever("Oranges")
    liste.ajouter("Sopalin")
    liste.afficher()
    print(liste)
    liste.sauvegarder()

    liste2 = Liste("taches")
    liste2.vider()
    liste2.ajouter("Cuisiner")
    liste2.ajouter("Faire des câlins")
    liste2.enlever("Faire le ménage")
    liste2.afficher()
    liste2.sauvegarder() """