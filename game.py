import pygame

from player import Player
from monster import Monster, Mummy, Alien
from comet_event import CometFallEvent

# Créer une seconde classe qui va représenter notre jeu



class Game:

    def __init__(self):
        # définir si notre jeu a commencé ou non
        self.is_playing = False
        # Générer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # Générer l'évenement
        self.comet_event = CometFallEvent(self)
        # groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        # Mettre le score à 0
        self.font = pygame.font.Font("assets/police.ttf", 25)
        self.score = 0
        self.pressed = {}


    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

    def add_score(self, points=10):
        self.score += points


    def game_over(self):
        # Remettre de jeu à neuf, retirer les monstres, remettre le joueur à 100 de vie, jeu en attente
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False
        self.score = 0


    def update(self, screen):
        # Afficher le score sur l'écran
        score_text = self.font.render(f"Score: {self.score}", 1, (0, 0, 0))
        screen.blit(score_text, (20, 20))

        # Appliquer l'image de mon joueur
        screen.blit(self.player.image, self.player.rect)

        # Actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)

        # Actualiser la barre d'évenement du jeu
        self.comet_event.update_bar(screen)

        # Actualiser l'animation du joueur
        self.player.update_animation()

        # Récuperer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # Récuperer les monstres de notre jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        # Récuperer  les comets de notre jeu
        for comet in self.comet_event.all_comets:
            comet.fall()

        # Appliquer l'ensemble des images de mon groupe de projectiles
        self.player.all_projectiles.draw(screen)

        # Appliquer l'ensemble des images de mon groupe e de monstre
        self.all_monsters.draw(screen)

        # Appliquer l'ensemble des images de mon groupe de cometes
        self.comet_event.all_comets.draw(screen)

        # Vérifier si le joueur souhaite aller a gauche ou a droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
           self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
           self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self, monster_class_name):
        self.all_monsters.add(monster_class_name.__call__(self))
