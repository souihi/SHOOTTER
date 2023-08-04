import pygame
import random

# CLASSE MONSTRE
class Monster(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = random.uniform(0.1,0.3)
        self.image = pygame.image.load("asset/mummy.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
        self.velocity = random.uniform(0.5,0.9)

    def damage(self, amount): #DEGATS SUBIT
        self.health -= amount

        #VERIFICATION PTS DE VIE
        if self.health <= 0 :
            #REAPARITON DU MONSTRE
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 3)
            self.health = self.max_health
        #VERIFICATION DE LA BARRE COMETE EST PLEINE
        if self.game.comet_event.is_full_loaded():
            #RETIRER DU JEU
            self.game.all_monsters.remove(self)
            # APPEL DE LA METHODE DECLANCHEMENT DE LA PLUIE DE COMET
            self.game.comet_event.attempt_fall()



    def update_health_bar(self, surface):
        # COULEUR DE LA BARRE DE VIE (VERT)
        bar_color = (111, 210, 46)
        #COULEUR BAR BACKGROUND (NOIR)
        back_bar_color = (0,0,0)
        # POSITION DE LA BARRE PAR RAPPORT AUX MONSTRES
        bar_position = [self.rect.x + 10, self.rect.y - 20, self.health, 5]  # [x, y, longueur, largeur]
        #POSOTION DE LA BAR BACKGROUND
        back_bar_position = [self.rect.x + 10, self.rect.y - 20, self.max_health, 5]  # [x, y, longueur, largeur]
        # DESSIN DE LA BARRE BACKGROUND
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        # DESSIN DE LA BARRE DE VIE
        pygame.draw.rect(surface, bar_color, bar_position)


    def forward(self):
        # DEPLACEMENT OK SI PAS DE COLLISON AVEC UN GROUPE JOUEUR
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # SI MONSTRE EST COLLISION ALORS DEGATS
        else:
            #INFLIGE DES DEGATS (AU JOUEUR)
            self.game.player.damage(self.attack)
