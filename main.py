import pygame
import math
from game import Game
pygame.init()

# Définir une clock
clock = pygame.time.Clock()
FPS = 120


# Générer la fenêtre de notre jeu
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080, 720))

# Importer de charger l'arrière plan de notre jeu
background = pygame.image.load('assets/bg.jpg')

# Importer notre bannière
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# Importer notre bouton pour lancer la partie
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() /2)

# Charger notre jeu
game = Game()


running = True

# Boucle tant que cette condition est vraie
while running:

    # Aplliquer l'arrière plan de notre jeu
    screen.blit(background, (0, -200))

    # Vérifier si notre jeu a commencé ou non
    if game.is_playing:
        # Déclancher les instructions de la partie
        game.update(screen)
    # Vérifier si notre jeu n'a pas commencé
    else:
        # Ajouter mon écran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)


    # Mettre à jour l'ecran
    pygame.display.flip()

    # Si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # Que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeux")
        # Détecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # Détecter si la touche espace est enclenchée pour lancer notre projectile
            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player.launch_projectile()


        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Vérification pour savoir si la souris est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                # Mettre le jeu en mode "lancé"
                game.start()

    # Fixer le nombre de FPS sur ma clock
    clock.tick(FPS)
