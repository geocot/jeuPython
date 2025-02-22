#Martin Couture
import pygame
import Asteroide
import random

pygame.init()

HAUTEUR_FENETRE = 800
LARGEUR_FENETRE = 1200
COULEUR_FOND = (0,0,0)
ECRAN = pygame.display.set_mode((LARGEUR_FENETRE, HAUTEUR_FENETRE))
horloge = pygame.time.Clock() # Pour contrôler la fréquence


a1 = Asteroide.Asteroide(random.randint(0,1100),2) #Remplacer le maximum de random en rapport avec la largeur de la fenêtre.


arretJeu = False
while not arretJeu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
               arretJeu = True
        else:
            ECRAN.fill(COULEUR_FOND)
            a1.deplacer(ECRAN)
            pygame.display.flip()
            horloge.tick(60)

pygame.quit()