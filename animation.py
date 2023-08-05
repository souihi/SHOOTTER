
import pygame
import random


# CLASSE ANIMATION
class AnimateSprite(pygame.sprite.Sprite):
    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f'asset/{sprite_name}.png')
        self.curent_image = 0  # COMMENCE A L'IMAGE 0
        self.images = annimation.get(sprite_name)
        self.animation = False

    # METHODE POUR DEMARRER L'ANIMATION
    def start_animation(self):
        self.animation = True

    # METHODE ANIMATION SPRITE
    def animate(self, loop= False):
        if self.animation:
            # PASSER A L'IMAGE SUIVANTE
            self.curent_image += random.randint(0, 1)
            # VERIFICATION SI FIN ANIMATION
            if self.curent_image >= len(self.images):
                # REMETTRE A 0
                self.curent_image = 0
                # VERIFIER SI L'ANIMATION N'EST PAS EN MODE BOUCLE
                if loop is False:
                    # DESACTIVE L'ANIMATION
                    self.animation = False
            # MODIFIER L'IMAGE PRECEDENT PAR LA SUIVANTE
            self.image = self.images[self.curent_image]


# FONCTION POUR CHARGER DES IMAGES

def load_animation_images(sprite_name):
    # CHARGEMENT DE TOUTES LES IMAGES
    image = []
    # RECUPERATION DU CHEMIN D'ACCES DU DOSSIER
    path = f'asset/{sprite_name}/{sprite_name}'
    # BOUCLE SUR CHAQUE IMAGES
    for num in range(1, 24):
        image_path = path + str(num) + '.png'
        image.append(pygame.image.load(image_path))
    # RETOURNE LA LISTE IMG
    return image


# DICTIONNAIRE QUI VA CONTENIR LES IMAGES CHARGEES DE CHAQUE DOSSIERS
annimation = {
    'mummy': load_animation_images('mummy'),
    'player': load_animation_images('player'),
    'alien': load_animation_images('alien')
}
