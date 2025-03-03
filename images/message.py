from abc import ABC, abstractmethod
import pygame
from images import AbstractObjetJeuAnime
class Pointage(AbstractObjetJeuAnime.ObjetJeuAnime):
    "Pour l'affichage des informations sur le jeu"

    def __init__(self, coordXDepart, coordYDepart, vitesse):  # , fichierSon):
        AbstractObjetJeuAnime.ObjetJeuAnime.__init__(self, coordXDepart, coordYDepart, vitesse)  # , fichierSon)

    def dessine(self):
        self.image = pygame.Surface((200, 200))
        #self.image.set_colorkey((0, 0, 0))  # Fond transparent
        #self.rect = self.image.get_rect()
        # Position de départ de la surface
        #self.rect.x = self._coordXDepart
        #self.rect.y = self._coordYDepart
        #Texte
        self._font = pygame.font.SysFont("Arial", 20, 1, 1)
        #self.image.fill((0,0,0))
        titre = self._font.render("Jeu de la fusée", 0, (255,255,255))
        AbstractObjetJeuAnime.ObjetJeuAnime._ecran.blit(titre , (10,10))

    def update(self):
        pass


