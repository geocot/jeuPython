#Martin Couture mars 2025
#https://github.com/geocot/jeuPython
import pygame
from images import AbstractObjetJeuAnime

#Classe pour afficher les collisions
class Message(AbstractObjetJeuAnime.ObjetJeuAnime):
    "Permet la création d'un message"
    #Constructeur
    def __init__(self, coordXDepart, coordYDepart, vitesse, texte  ):
        self._couleur = (255,0,0) #Couleur rouge
        self._texte = texte
        self.font = pygame.font.SysFont("Arial", 30, 1, 1)
        #Initialise la classe parente
        AbstractObjetJeuAnime.ObjetJeuAnime.__init__(self, coordXDepart, coordYDepart, vitesse)#, fichierSon)

    #Pour dessiner le message
    def dessine(self):
        #Pour le draw, il doit y avoir un self.image et un self.rect
        self.image = pygame.Surface((AbstractObjetJeuAnime.ObjetJeuAnime._ecran.get_width(), 300))
        self.rect = self.image.get_rect()
        self.image.fill((0, 0, 0))
        texte = self.font.render(self._texte, True, self._couleur)
        self.image.blit(texte, (self._coordXDepart, self._coordYDepart))


    #Pour l'animation de la collision
    def update(self):
        texte = self.font.render(self._texte, True, self._couleur)
        self.image.blit(texte, (self._coordXDepart, self._coordYDepart))

