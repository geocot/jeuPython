import pygame.draw
import random

from pygame.event import set_keyboard_grab


class Asteroide:
    "Permet la création d'un astéroide"

    def __init__(self, alignementXDepart, vitesse):
        self._vitesse = vitesse
        self._couleursChoix = [(200, 200, 200), (150, 150, 150), (100, 200, 200), (200, 100, 200), (200, 200, 100), (250, 250, 250)]
        self._formesChoix = [[[29,0],[39,18],[55,23],[40,40],[19,36],[0,35]],  #En [X,Y]
                        [[17, 0], [43, 1], [43, 23], [28, 40], [3, 36], [0, 18]],
                        [[0, 26], [7, 4], [30, 0], [38, 11], [22, 33], [0, 23] ]
                        ]
        self._forme = random.choice(self._formesChoix)
        self._couleur = random.choice(self._couleursChoix)
        self._alignementXDepart = alignementXDepart
        self._calculRectangle() #Initialise l'enveloppe du rectangle de la forme choisie.

    #Détermine l'enveloppe de l'astéroïde au départ
    def _calculRectangle(self):
        largeur = 0
        hauteur = 0
        xMin = self._alignementXDepart
        yMin = 0
        for coordonnee in self._forme:
            if coordonnee[0] > largeur:
                largeur = coordonnee[0]
            if coordonnee[1] > hauteur:
                hauteur = coordonnee[1]

        self._rectangle = pygame.Rect((xMin,yMin),(largeur,hauteur))

    def deplacer(self, fenetre):
        formeTempo = []
        for coordonnee in self._forme:
            formeTempo.append([coordonnee[0] + self._rectangle.left,coordonnee[1]+ self._rectangle.top])

        self._rectangle = self._rectangle.move(0,self._vitesse)
        pygame.draw.polygon(fenetre, self._couleur, formeTempo)