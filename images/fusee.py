import pygame.draw
import objetJeu

class Fusee(objetJeu.ObjetJeu):
    "Affiche la position du joueur"

    def __init__(self, coordXDepart, coordYDepart):
        #Initialisation de la classe parent.
        objetJeu.ObjetJeu.__init__(self, coordXDepart, coordYDepart)
        # Initialisation Sprite.
        pygame.sprite.Sprite.__init__(self)

