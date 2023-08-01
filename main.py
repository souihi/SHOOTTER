import math

import game as game
import pygame

from game import Game

pygame.init()
# CHARGEMENT DU JEU
game = Game()
# GENERER LA FENETRE DE JEU
pygame.display.set_caption("SHOOTER")
screen = pygame.display.set_mode((1080, 720))
# IMPORT BACKGROUND
background = pygame.image.load('asset/bg.jpg')
#IMPORT DE LA BANNIERE ET BOUTON PLAY
banner = pygame.image.load('asset/banner.png')
banner = pygame.transform.scale(banner, (500,500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil( screen.get_width() /4)

play_button = pygame.image.load('asset/button.png')
play_button = pygame.transform.scale(play_button, (400, 200))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)
# BOUCLE FENETRE
running = True
while running:
    # BACKGROUND JEU
    screen.blit(background, (0, -200))

    #VERIFICATION SI LE JEU EST LANCEE
    if game.is_playing :
        #DECLANCHE LES INSTRUCTIONS DE LA PARTIE
        game.update(screen)
        #VERIFICATION SI JEUX N'A PAS COMMENCEE
    else:

        # BOUTTON JEU
        screen.blit(play_button, play_button_rect) #BLIT DEMANDE 2 ARGUMENTS (IMAGE, POSITION EN X ET Y)
        # BANNER JEU
        screen.blit(banner, banner_rect)

    # MAJ SCREEN
    pygame.display.flip()
    # FERMETURE FENETRE
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print('Fermeture de la fenêtre')
        # EVENEMENT TOUCHE
        # DETECTION SI TOUCHE UTILISE
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            # TOUCHE ESPACE
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
        elif event.type == pygame.KEYUP:
            game.player.rect.y = 500
            game.pressed[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #VERIFICATION SI LA SOURIS EST EN COLLISION AVEC LE BOUTTON JOUER
            if play_button_rect.collidepoint(event.pos):
                #JEUX EN MODE LANCEE
                game.start()