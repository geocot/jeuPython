import pygame.draw
from images import abstractObjetJeu


class Fusee(abstractObjetJeu.ObjetJeu):
    "Affiche la position du joueur"

    def __init__(self, coordXDepart, coordYDepart):
        self._rouge = (252, 50, 50)
        self._couleurFusee = (191 , 191, 0)
        self._grisPale = (220,220,220)
        # Animation fusée
        self._xMinCarre = -10
        self._xMinPos = -5
        #Initialisation de la classe parent.
        abstractObjetJeu.ObjetJeu.__init__(self, coordXDepart, coordYDepart)

    def dessine(self):
        self.image = pygame.Surface((30, 100))
        self.image.set_colorkey((0, 0, 0))  # Fond transparent
        self.rect = self.image.get_rect()
        # Position de départ de la surface
        self.rect.x = self._coordXDepart
        self.rect.y = self._coordYDepart
        #Affichage des composants de la fusée
        # Affiche pattes
        pygame.draw.polygon(self.image, self._rouge, ((0, 100), (5, 100), (15, 70), (10, 70))) #Gauche
        pygame.draw.polygon(self.image, self._rouge, ((25, 100), (30, 100), (20, 70), (15, 70))) #Droite
        #Affiche le body
        pygame.draw.ellipse(self.image, self._couleurFusee, (0, 10, 30, 75))
        #Affiche le bout
        pygame.draw.circle(self.image, self._rouge, (15,8), 5 )
        #Affiche fenêtres
        pygame.draw.rect(self.image, self._grisPale, (0,40,48,20) )
        pygame.draw.rect(self.image, self._rouge, (self._xMinPos, 40, 10, 20))

    def update(self):
        pygame.draw.rect(self.image, self._grisPale, (0, 40, 48, 20))
        self._xMinPos = self._xMinPos + 1
        pygame.draw.rect(self.image, self._rouge, (self._xMinPos, 40, 10, 20))
        if (self._xMinPos == 40):
            self._xMinPos = self._xMinCarre