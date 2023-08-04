import pygame
import random


# CLASSE COMET
class Comet(pygame.sprite.Sprite):
    def __init__(self, comet_event):
        super().__init__()
        self.image = pygame.image.load('asset/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)
        print("Boule supp")
    def fall(self):
        self.rect.y += self.velocity
        # NE TOMBE PAS SUR LE SOL
        if self.rect.y >= 500:
            print("Sol")
            #SUPP LA BOULE DE FEU
            self.remove()
        #VERIFE  SI TOUCHE LE JOUEUR
        if self.comet_event.game.check_collision(self, self.comet_event.game.all_players): #BOULE DE FEU ET JOUEUR EN PARAMETRE
            print("Touché")
            #RETIRE LA BOULE DE FEU
            self.remove()
            #SUBIT DES DEGATS
            self.comet_event.game.player.damage(20)
