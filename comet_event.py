import pygame
from comet import Comet

# Créer une classe pour gérer cet évenement
class CometFallEvent:

    # Lors du chargement -> créer un compteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 10
        self.game = game
        self.fall_mode = False

       # Définir un groupe de sprite pour stocker nos cometes
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        # Boucle pour les valeurs entre 1 et 10
        for i in range(1, 10):
            # Apparaitre 1 première boule de feu
            self.all_comets.add(Comet(self))


    def attempt_fall(self):
        # La jauge d'évenement est totalement chargée
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            print("Pluie de cometes !!")
            self.meteor_fall()
            self.fall_mode = True # activer l'évenement

    def update_bar(self, surface):
        # Ajouter  du pourcentage à la bar
        self.add_percent()



        # Barre noir (en arrière plan)
        pygame.draw.rect(surface, (0, 0, 0), [
            0,  # L'axe des x
            surface.get_height() - 20,  # L'axe des y
            surface.get_width(),  # Longueur de la fenêtre
            10  # Épaisseur de la barre
        ])
        # Barre rouge (jauge d'event)
        pygame.draw.rect(surface, (187, 11, 11), [
            0,  # L'axe des x
            surface.get_height() - 20,  # L'axe des y
            (surface.get_width() / 100) * self.percent,  # Longueur de la fenêtre
            10  # Épaisseur de la barre
        ])
