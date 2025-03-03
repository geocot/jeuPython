import random
import pygame
from images import AbstractObjetJeuAnime

class Collision(AbstractObjetJeuAnime.ObjetJeuAnime):
    "Permet la création d'un astéroide"

    def __init__(self, coordXDepart, coordYDepart, vitesse,  rayon): # , fichierSon):
        self._couleur = (150,150,150)
        self._rayon = rayon
        AbstractObjetJeuAnime.ObjetJeuAnime.__init__(self, coordXDepart, coordYDepart, vitesse)#, fichierSon)

    def dessine(self):
        self.image = pygame.Surface((100, 100))
        self.image.set_colorkey((0, 0, 0))  # Fond transparent
        self.rect = self.image.get_rect()
        # Position de départ de la surface
        self.rect.x = self._coordXDepart
        self.rect.y = self._coordYDepart
        pygame.draw.circle(self.image, (223, 243, 31), (50, 50), self._rayon)

    def update(self):
        pygame.draw.circle(self.image, self._couleur,(50, 50), random.randint(10,15))
        self._couleur = (self._couleur[0]-10, self._couleur[0]-10, self._couleur[0]-10)
        if self._couleur[0] < 10:
            self.kill()
