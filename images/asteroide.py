import pygame.draw
import random
from images import AbstractObjetJeuAnime


class Asteroide(AbstractObjetJeuAnime.ObjetJeuAnime):
    "Permet la création d'un astéroide"

    def __init__(self, coordXDepart, coordYDepart, vitesse): # , fichierSon):
        #Initialise la classe mère
        AbstractObjetJeuAnime.ObjetJeuAnime.__init__(self, coordXDepart, coordYDepart, vitesse)#, fichierSon)

    def dessine(self):
        #Les astéroïdes ont plusieurs formes et couleurs.
        self._couleursChoix = [(200, 200, 200), (100, 100, 100), (175, 200, 200), (200, 175, 200), (200, 200, 175), (250, 250, 250)]
        self._formesChoix = [[[29,0],[39,18],[55,23],[40,40],[19,36],[0,35]],  #En [X,Y]
                        [[17, 0], [43, 1], [43, 23], [28, 40], [3, 36], [0, 18]],
                        [[0, 26], [7, 4], [30, 0], [38, 11], [22, 33], [0, 23] ]
                        ]
        #Stockage de la forme et de la couleur
        self._forme = random.choice(self._formesChoix)
        self._couleur = random.choice(self._couleursChoix)
        self._calculRectangle() #Initialise l'enveloppe du rectangle de la forme choisie.
        self.image = pygame.Surface((self._rectangle.width, self._rectangle.height))
        self.image.set_colorkey([0,0,0])
        pygame.draw.polygon(self.image, self._couleur, self._forme) #Affiche la forme

        self.image = pygame.transform.rotate(self.image, random.randint(0,360))  # Rotation aléatoire
        self.rect = self.image.get_rect()
        #Position de départ de la surface
        self.rect.x = self._coordXDepart
        self.rect.y = 0



    #Détermine l'enveloppe de l'astéroïde au départ
    #Comme les formes sont différentes, la méthode calcule le rectangle le plus près de la forme.
    def _calculRectangle(self):
        largeur = 0
        hauteur = 0
        xMin = self._coordXDepart
        yMin = 0
        for coordonnee in self._forme:
            if coordonnee[0] > largeur:
                largeur = coordonnee[0]
            if coordonnee[1] > hauteur:
                hauteur = coordonnee[1]
        #Mise en variable de l'information calculée
        self._rectangle = pygame.Rect((xMin,yMin),(largeur,hauteur))

    #Pour la mise à jour du sprite
    def update(self):
        self.rect.y += self._vitesse
        self.rect.x = self._coordXDepart
        #Si l'astéroïde dépasse le cadre de la fenêtre, l'objet est supprimé
        if not AbstractObjetJeuAnime.ObjetJeuAnime._ecran.get_rect().contains(self.rect):
            self.kill()

