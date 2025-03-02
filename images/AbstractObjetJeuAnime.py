from abc import ABC, abstractmethod
import pygame
class ObjetJeuAnime(ABC, pygame.sprite.Sprite):
    "Permet d'être la base des objets animés"

    "Classe générique pour afficher des objets à l'écran"

    def __init__(self, coordXDepart, coordYDepart,vitesse ):
        self._coordXDepart = coordXDepart
        self._coordYDepart = coordYDepart
        self._vitesse = vitesse
        #self._fichierSon = pygame.mixer.Sound(fichierSon)
        #Initialisation Sprite
        pygame.sprite.Sprite.__init__(self)
        #Avec l'héritage de Sprite, Il faut absolument avoir une propriété image et rect. Pas d'autres nom.
        self.dessine()

    @abstractmethod
    def update(self):
        ...

    @abstractmethod
    def dessine(self):
        ...

    @staticmethod
    def setEcran(ecran):
       ObjetJeuAnime._ecran = ecran




