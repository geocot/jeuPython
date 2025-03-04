#Martin Couture. mars 2025
#https://github.com/geocot/jeuPython
import random
import pygame
from images import AbstractObjetJeuAnime

#Classe pour afficher les collisions
class Collision(AbstractObjetJeuAnime.ObjetJeuAnime):
    "Permet la création d'un astéroide"
    #Constructeur
    def __init__(self, coordXDepart, coordYDepart, vitesse,  rayon): # , fichierSon):
        self._couleur = (150,150,150) #Couleur grise des collisions
        if rayon <=50:
            self._rayon = rayon #Rayon des collisions.
        else:
            self._rayon = 10
        #Initialise la classe parente
        AbstractObjetJeuAnime.ObjetJeuAnime.__init__(self, coordXDepart, coordYDepart, vitesse)#, fichierSon)

    #Pour dessiner les collisions
    def dessine(self):
        self.image = pygame.Surface((100, 100)) #Définition d'une surface pour l'affichage
        self.image.set_colorkey((0, 0, 0))  # Fond transparent
        self.rect = self.image.get_rect() #Extraction de l'enveloppe de la surface
        # Position de départ de la surface
        self.rect.x = self._coordXDepart
        self.rect.y = self._coordYDepart
        #Affiche le cercle de collision.
        pygame.draw.circle(self.image, (223, 243, 31), (50, 50), self._rayon)

    #Pour l'animation de la collision
    def update(self):
        #Fait plusieurs cercles en réduisant la luminosité.
        pygame.draw.circle(self.image, self._couleur,(50, 50), random.randint(10,15))
        self._couleur = (self._couleur[0]-10, self._couleur[0]-10, self._couleur[0]-10)
        if self._couleur[0] < 10:
            self.kill() #Efface le cercle lorsque le minimum de luminosité est atteint.

