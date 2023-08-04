#CLASS PLAYER
import pygame
from projectile import Projectile

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 20
        self.velocity = 2
        self.all_projectile = pygame.sprite.Group()
        self.image = pygame.image.load('asset/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def damage(self, amount):
        if self.health - amount > amount : #SI SANTE - DEGAT > DEGAT
            self.health -= amount
        else:
            #S\'IL N'A PLUS DE POINT DE VIE
            self.game.game_over()
    def update_health_bar(self, surface):
        # COULEUR DE LA BARRE DE VIE (VERT)
        bar_color = (236, 255, 0 )
        #COULEUR BAR BACKGROUND (NOIR)
        back_bar_color = (0,0,0)
        # POSITION DE LA BARRE PAR RAPPORT AUX MONSTRES
        bar_position = [self.rect.x + 50, self.rect.y + 20, self.health, 10]  # [x, y, longueur, largeur]
        #POSOTION DE LA BAR BACKGROUND
        back_bar_position = [self.rect.x + 50, self.rect.y + 20, self.max_health, 10]  # [x, y, longueur, largeur]
        # DESSIN DE LA BARRE BACKGROUND
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        # DESSIN DE LA BARRE DE VIE
        pygame.draw.rect(surface, bar_color, bar_position)

    #INSTANCE PROJECTILE
    def launch_projectile(self):
        self.all_projectile.add(Projectile(self))

    #METHODE DEPLACEMENT JOUEUR
    def move_right(self):
        #VERIFICATION SI JOUEUR EST EN COLLISION AVEC UN MONSTRE
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    #def move_up(self):
        # VERIFICATION SI JOUEUR EST EN COLLISION AVEC UN MONSTRE
    #    if not self.game.check_collision(self, self.game.all_monsters):
     #       self.rect.y -= self.velocity
