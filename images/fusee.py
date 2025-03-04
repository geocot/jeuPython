#Martin Couture
#Mars 2025
#https://github.com/geocot/jeuPython
import random
import pygame.draw
from images import AbstractObjetJeuAnime

#Classe pour l'affichage de la fusée
class Fusee(AbstractObjetJeuAnime.ObjetJeuAnime):
    "Affiche la position du joueur"

    def __init__(self, coordXDepart, coordYDepart, vitesse):
        #Définition des variables de base
        #Définition des couleurs
        self._rouge = (252, 50, 50)
        self._couleurFusee = (252, 50, 50)
        self._grisPale = (220,220,220)
        self._vertFlamme = 240 #Composante verte de la couleur de la flamme de la fusée
        # Animation fusée
        self._xMinCarre = -10
        self._xMinPos = -5
        self._mouvement = 0
        self._dectectionDepart = False
        #Initialisation de la classe parent.
        AbstractObjetJeuAnime.ObjetJeuAnime.__init__(self, coordXDepart, coordYDepart, vitesse)

    #Affichage de la fusée
    def dessine(self):
        self.image = pygame.Surface((30, 100))
        self.image.set_colorkey((0, 0, 0))  # Fond transparent
        self.rect = self.image.get_rect()
        # Position de départ de la surface
        self.rect.x = self._coordXDepart
        self.rect.y = self._coordYDepart
        #Affichage des composantes de la fusée
        #Affiche le body
        pygame.draw.ellipse(self.image, self._couleurFusee, (0, 10, 30, 75))
        #Affiche le bout
        pygame.draw.polygon(self.image, self._grisPale, ((10,10),(15,0),(20,10)) )
        #Affiche ceinture
        pygame.draw.rect(self.image, self._grisPale, (0,40,48,20) )
        pygame.draw.rect(self.image, self._rouge, (self._xMinPos, 40, 10, 20))
        # Affiche pattes
        pygame.draw.polygon(self.image, self._rouge, ((0, 100), (5, 100), (15, 80), (10, 80)))  # Gauche
        pygame.draw.polygon(self.image, self._rouge, ((25, 100), (30, 100), (20, 80), (15, 80)))  # Droite
        #Flamme
        pygame.draw.polygon(self.image, (226, self._vertFlamme, 15), ((20, 82), (10, 82), (15, 100)))
    #Pour bouger la fusée
    def controle(self, mouvement):
        self._mouvement = mouvement

    #Animation de la fusée
    def update(self):
        #Animation flamme
        self._vertFlamme = random.randint(50, 240)
        pygame.draw.polygon(self.image, (226, self._vertFlamme, 15), ((20, 82), (10, 82), (15, 100)))

        #Élimine les pattes au décollage
        if self._dectectionDepart:
            #Affiche pattes en noir
            pygame.draw.polygon(self.image, (0,0,0), ((0, 100), (5, 100), (15, 80), (10, 80))) #Gauche
            pygame.draw.polygon(self.image, (0,0,0), ((25, 100), (30, 100), (20, 80), (15, 80))) #Droite

        #Animation de la ceinture de la fusée
        pygame.draw.rect(self.image, self._grisPale, (0, 40, 48, 20))
        self._xMinPos = self._xMinPos + 1
        pygame.draw.rect(self.image, self._rouge, (self._xMinPos, 40, 10, 20))
        if (self._xMinPos == 40):
            self._xMinPos = self._xMinCarre

        #*************************************
        #******Animation du mouvement*********
        # *************************************
        if self._mouvement == "g":
            #Limite le mouvement gauche
            if self.rect.x < 10:
                self.rect.x = 10
            else:
                self.rect.x -= self._vitesse

        elif self._mouvement == "d":
            #Limite le mouvement droit
            if self.rect.x > AbstractObjetJeuAnime.ObjetJeuAnime._ecran.get_rect().right -40:
                self.rect.x = AbstractObjetJeuAnime.ObjetJeuAnime._ecran.get_rect().right -40
            else:
                self.rect.x += self._vitesse
        elif self._mouvement == "h":
            self._dectectionDepart = True
            # Limite le mouvement haut
            if self.rect.y < 10:
                self.rect.y = 10
            self.rect.y -= self._vitesse
        elif self._mouvement == "b":
            # Limite le mouvement bas
            if self.rect.y > AbstractObjetJeuAnime.ObjetJeuAnime._ecran.get_rect().bottom - 110:
                self.rect.y = AbstractObjetJeuAnime.ObjetJeuAnime._ecran.get_rect().bottom - 110
            self.rect.y += self._vitesse

        #Stop la fusée après un déplacement
        self._mouvement = ""