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
        #VERIFICATION SI LE NOMBRE DE COMET EST DE  0
        if len(self.comet_event.all_comets)== 0 :
            print("L'évenement est fini ")
            #REMETTRE LA BARRE A 0
            self.comet_event.reset_percent()
            #FAIRE APPARAITRE LES MONSTRES
            self.comet_event.game.spawn_Monster()
            self.comet_event.game.spawn_Monster()
            self.comet_event.game.spawn_Monster()
    def fall(self):
        self.rect.y += self.velocity
        # NE TOMBE PAS SUR LE SOL
        if self.rect.y >= 500:
            print("Sol")
            #SUPP LA BOULE DE FEU
            self.remove()
            #VERIFIER SI PLUS DE BOULE DE FEU DANS LE JEU
            if len(self.comet_event.all_comets) == 0 :
                print("L\'évenement est fini")
                #Remettre la jauge de vie au départ
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

        #VERIFE  SI TOUCHE LE JOUEUR
        if self.comet_event.game.check_collision(self, self.comet_event.game.all_players): #BOULE DE FEU ET JOUEUR EN PARAMETRE
            print("Touché")
            #RETIRE LA BOULE DE FEU
            self.remove()

            #SUBIT DES DEGATS
            self.comet_event.game.player.damage(20)
