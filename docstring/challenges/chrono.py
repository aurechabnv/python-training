from time import time

from pynput import keyboard


class Chrono:
    def __init__(self, start_prompt: bool = False):
        """
        Initialise un chronomètre.

        :param start_prompt: Permet de contrôler le chronomètre via le clavier. Par défaut à `False`.
        """
        self._started = False
        self._start_time = 0.0
        self._time_lapse = 0.0

        if start_prompt:
            self.start_prompt()

    @property
    def time_lapse(self) -> float:
        """
        La valeur courante du chronomètre arrondie à deux décimales
        """
        return round(self._time_lapse, 2)

    def start(self):
        """
        Démarre le chronomètre en enregistrant le timestamp de départ
        """
        self._started = True
        self._start_time = time()

    def stop(self):
        """
        Arrête le chronomètre et calcule le temps écoulé
        """
        if self._started:
            self._started = False
            self._time_lapse += time() - self._start_time

    def reset(self):
        """
        Reset le chronomètre en vidant le temps écoulé calculé jusqu'à présent
        """
        self._time_lapse = 0.0

    def start_prompt(self):
        """
        Lance le mode de contrôle au clavier
        (démarrage du listener)
        """
        print("Bienvenue sur votre chronomètre !")
        print("ESPACE pour lancer/arrêter, SUPPR pour reset, ESC pour quitter")
        with keyboard.Listener(on_press=self._on_key_press) as listener:
            listener.join()

    def _on_key_press(self, key) -> bool | None:
        """
        Contrôle le chronomètre selon la touche pressée :
            - ESPACE pour lancer/arrêter
            - SUPPR pour reset
            - ESC pour quitter le mode

        :param key:
        :return: Retourne `False` pour sortir du contrôle au clavier (arrêt du listener)
        """
        if key == keyboard.Key.space:
            if not self._started:
                self.start()
                print("Démarrage du chrono...")
            else:
                self.stop()
                print(f"Arrêt du chrono : {self.time_lapse}")

        elif key == keyboard.Key.delete:
            self.reset()
            print(f"Reset du chrono : {self.time_lapse}")

        elif key == keyboard.Key.esc:
            return False
