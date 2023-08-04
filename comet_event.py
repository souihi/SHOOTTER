import pygame
from comet import Comet


# CLASSE COMET

class CometFallEvent:
    def __init__(self, game):
        super().__init__()
        # CREATION D\'UN COMPTEUR LORS DU CHARGEMENT
        self.percent = 0
        self.percent_speed = 0.1
        self.game = game
        self.fall_mode = False

        # GROUPE DE SPRITE POUR STOCKER LES COMETES
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
            for i in range(1,20):
                # APPARITION BOULE DE FEU
                self.all_comets.add(Comet(self))

    def attempt_fall(self):
        # LA JAUGE D\'EVENEMENT EST TOTALEMENT CHARGE ET LE GROUPE DE MONSTRE = 0
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            self.meteor_fall()
            # print("Pluie de comet")

            self.fall_mode = True #ACTIVER L\'EVENEMENT

    def update_bar(self, surface):
        # AJOUT DU POURCENTAGE A LA BARRE
        self.add_percent()

        # COULEUR DE LA BARRE  (ROUGE)
        bar_color = (187, 11, 10)
        # COULEUR BAR BACKGROUND (NOIR)
        back_bar_color = (0, 0, 0)
        # POSITION DE LA BARRE PAR RAPPORT AU SOL
        bar_position = [0, surface.get_height() - 20, (surface.get_width() / 100) * self.percent,
                        10]  # [x, y, longueur, largeur]
        # POSOTION DE LA BAR BACKGROUND
        back_bar_position = [0, surface.get_height() - 20, surface.get_width(), 10]  # [x, y, longeur, largeur]
        # DESSIN DE LA BARRE BACKGROUND
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        # DESSIN DE LA BARRE DE VIE
        pygame.draw.rect(surface, bar_color, bar_position)
