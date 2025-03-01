import random

import pygame
from images import objetJeuAnime

class Collision(pygame.sprite.Sprite, objetJeuAnime.ObjetJeuAnime):
    "Permet la création d'un astéroide"

    def __init__(self, coordXDepart, coordYDepart, vitesse): # , fichierSon):
        objetJeuAnime.ObjetJeuAnime.__init__(self, coordXDepart, coordYDepart, vitesse)#, fichierSon)
        self._rayon = 10
        #Initialisation Sprite
        pygame.sprite.Sprite.__init__(self)
        #Avec l'héritage de Sprite, Il faut absolument avoir une propriété image et rect. Pas d'autres nom.

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.set_colorkey((0, 0, 0)) #Fond transparent
        self._couleur = (150, 150, 150)
        pygame.draw.circle(self.image, (223,243,31), (25, 25), self._rayon)
        self.rect = self.image.get_rect()
        #Position de départ de la surface
        self.rect.x = self._coordXDepart
        self.rect.y = self._coordYDepart


    def update(self):
        pygame.draw.circle(self.image, self._couleur,(25, 25), random.randint(10,15))
        self._couleur = (self._couleur[0]-10, self._couleur[0]-10, self._couleur[0]-10)
        if self._couleur[0] < 10:
            self.kill()
