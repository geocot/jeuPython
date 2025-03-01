import pygame.draw
from images import abstractObjetJeu


class Fusee(abstractObjetJeu.ObjetJeu):
    "Affiche la position du joueur"

    def __init__(self, coordXDepart, coordYDepart):
        #Initialisation de la classe parent.
        abstractObjetJeu.ObjetJeu.__init__(self, coordXDepart, coordYDepart)

