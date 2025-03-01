class ObjetJeu():
    "Classe générique pour afficher des objets à l'écran"

    def __init__(self, coordXDepart, coordYDepart ):#, fichierSon):
        self._coordXDepart = coordXDepart
        self._coordYDepart = coordYDepart
        #self._fichierSon = pygame.mixer.Sound(fichierSon)

    def update(self):
        pass

    @staticmethod
    def setEcran(ecran):
       ObjetJeu._ecran = ecran
'''
    def emettre_son(self):
        self.son.play()
'''