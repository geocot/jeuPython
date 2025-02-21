#Martin Couture
import pygame
import Asteroide

pygame.init()

HAUTEUR_FENETRE = 800
LARGEUR_FENETRE = 1200
COULEUR_FOND = (0,0,0)
ECRAN = pygame.display.set_mode((LARGEUR_FENETRE, HAUTEUR_FENETRE))

ECRAN.fill(COULEUR_FOND)
a1 = Asteroide.Asteroide(2,2)
a1.afficher(ECRAN)
pygame.display.flip()

arretJeu = False
while not arretJeu:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
            if event.key == pygame.K_ESCAPE:
                arretJeu = True