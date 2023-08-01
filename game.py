#CLASS GAME
import pygame.sprite

from player import Player
from monster import Monster

class Game:
    def __init__(self):
        #COMMENCEMENT DU JEU OU NON
        self.is_playing = False
        #GENERE UN JOUEUR
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        #GROUPE DE MONSTRE
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}


    def start(self):
        self.is_playing = True
        self.spawn_Monster()
        self.spawn_Monster()

    def game_over(self):
        #JEU A ZEROS
        self.all_monsters =  pygame.sprite.Group() #J\'ECRASE LE GROUPE DE MONSTRE
        self.player.health = self.player.max_health #RECHARGE LA VIE DU JOUEUR
        self.is_playing = False #REMETTRE LE JEU EN ATTENTE
    def update(self, screen):
        # RECUPERATION DES PROJECTILES DU JOUEUR
        for projectile in self.player.all_projectile:
            projectile.move()
        # RECUPERATION DES MONSTRES
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
        # IMG PLAYER
        screen.blit(self.player.image, self.player.rect)
        # ACTUALISER BAR DE VIE
        self.player.update_health_bar(screen)

        # IMG PROJECTILE
        self.player.all_projectile.draw(screen)
        # IMG MONSTRE
        self.all_monsters.draw(screen)
        # VERIFICATION DE LA DIRECTION DU JOUEUR
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
        # elif game.pressed.get(pygame.K_UP) and game.player.rect.y + game.player.rect.height >550 :
        #   game.player.move_up()

        # print(game.player.rect.y)


    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_Monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)