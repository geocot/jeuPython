from abc import ABC, abstractmethod
import pygame
#Classe abstraite de laquelle les classes d'éléments animés vont hériter.
class ObjetJeuAnime(ABC, pygame.sprite.Sprite):
    "Permet d'être la base des objets animés"

    #Constructeur
    def __init__(self, coordXDepart, coordYDepart,vitesse ):
        self._coordXDepart = coordXDepart
        self._coordYDepart = coordYDepart
        self._vitesse = vitesse
        #self._fichierSon = pygame.mixer.Sound(fichierSon)
        #Initialisation Sprite
        pygame.sprite.Sprite.__init__(self)
        #Avec l'héritage de Sprite, Il faut absolument avoir une propriété image et rect. Pas d'autres nom
        self.dessine()

    #Méthode abstraite pour la mise à jour de l'affichage
    @abstractmethod
    def update(self):
        ...

    # Méthode abstraite pour dessiner l'élément
    @abstractmethod
    def dessine(self):
        ...

    #Méthode statique pour intégrer la fenêtre de départ pour les éléments à dessiner et à animer
    @staticmethod
    def setEcran(ecran):
       ObjetJeuAnime._ecran = ecran




