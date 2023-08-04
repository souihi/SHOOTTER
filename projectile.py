import pygame


# CLASSE PROJECTILE

class Projectile(pygame.sprite.Sprite):
    # CONSTRUCTEUR
    def __init__(self, player):
        super().__init__()
        self.velocity = 1
        self.player = player
        self.image = pygame.image.load("asset/projectile.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 125
        self.rect.y = player.rect.y + 90
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        self.angle += 30
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        # ROTATATION DU PROJECTILE PAR RAPPORT AU CENTRE DE L'IMAGE
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectile.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()
        # VERIFICATION SI PROJECTLES ENTRE EN COLLISION AVEC lE MONSTRE
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            # SUPPRIMER LE PROJECTILE
            self.remove()
            # DEGATS INFLIGER
            monster.damage(self.player.attack)
        # SUPPRIME LES PROJECTILES EN DEHORS DE L'ECRAN
        if self.rect.x >= 1080:
            self.remove()
