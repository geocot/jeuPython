from abc import ABC, abstractmethod
import pygame

class ObjetJeu(ABC, pygame.sprite.Sprite):
    "Classe générique pour afficher des objets à l'écran"

    def __init__(self, coordXDepart, coordYDepart ):
        self._coordXDepart = coordXDepart
        self._coordYDepart = coordYDepart
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
       ObjetJeu._ecran = ecran
