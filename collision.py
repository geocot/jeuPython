import random

import pygame
import objetAnime

class Collision(pygame.sprite.Sprite, objetAnime.ObjetAnime):
    "Permet la création d'un astéroide"

    def __init__(self, coordXDepart, coordYDepart, vitesse): # , fichierSon):
        objetAnime.ObjetAnime.__init__(self,coordXDepart, coordYDepart, vitesse)#, fichierSon)
        self._rayon = 10
        #Initialisation Sprite
        pygame.sprite.Sprite.__init__(self)
        #Avec l'héritage de Sprite, Il faut absolument avoir une propriété image et rect. Pas d'autres nom.

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.set_colorkey((0, 0, 0)) #Fond transparent
        pygame.draw.circle(self.image, (255, 0, 0), (25, 25), self._rayon)
        self.rect = self.image.get_rect()
        #Position de départ de la surface
        self.rect.x = self._coordXDepart
        self.rect.y = self._coordYDepart
        self._rouge = 200

    def update(self):
        pygame.draw.circle(self.image, (self._rouge,0,0),(25, 25), random.randint(10,15))
        self._rouge = self._rouge -10
        if self._rouge < 10:
            self.kill()
