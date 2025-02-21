import pygame.draw
import random


class Asteroide:
    "Permet la création d'un astéroide"

    def __init__(self, rectangle, vitesse):
        self._vitesse = vitesse
        self._couleursChoix = [(200, 200, 200), (150, 150, 150), (100, 200, 200), (200, 100, 200), (200, 200, 100), (250, 250, 250)]
        self._formesChoix = [[[58,28],[68,46],[84,51],[69,68],[48,64],[29,63],[58,28]],
                        [[58, 28], [84, 29], [84, 51], [69, 68], [44, 64], [41, 46], [58, 28]],
                        [[28, 39], [35, 17], [58, 13], [66, 24], [50, 46], [28, 36], [28, 39]]
        ]
        self._forme = random.choice(self._formesChoix)
        self._couleur = random.choice(self._couleursChoix)
        self._rectangle = rectangle #Selon la forme choisie.

    def _calculRectangle(self):
        pass
    def afficher(self, fenetre):

        pygame.draw.polygon(fenetre, self._couleur, self._forme)