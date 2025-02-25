import pygame
class ObjetAnime():
    "Permet d'être la base des objets animés"

    def __init__(self, coordXDepart, coordYDepart, vitesse ):#, fichierSon):
        self._vitesse = vitesse
        self._coordXDepart = coordXDepart
        self._coordYDepart = coordYDepart
        #self._fichierSon = pygame.mixer.Sound(fichierSon)

    def update(self):
        pass

    @staticmethod
    def setEcran(ecran):
       ObjetAnime._ecran = ecran
'''
    def emettre_son(self):
        self.son.play()
'''
