#Martin Couture
import pygame
import Asteroide
import random

pygame.init()

HAUTEUR_FENETRE = 800
LARGEUR_FENETRE = 1200
COULEUR_FOND = (0,0,0)
ECRAN = pygame.display.set_mode((LARGEUR_FENETRE, HAUTEUR_FENETRE))
fond = pygame.Surface(ECRAN.get_size())
fond.fill(COULEUR_FOND)
ECRAN.blit(fond, (0,0))
horloge = pygame.time.Clock() # Pour contrôler la fréquence


a1 = Asteroide.Asteroide(random.randint(0,1100),random.randint(1,2)) #Remplacer le maximum de random en rapport avec la largeur de la fenêtre.
a2 = Asteroide.Asteroide(random.randint(0,1100),random.randint(1,2)) #Remplacer le maximum de random en rapport avec la largeur de la fenêtre.
asteroides = pygame.sprite.Group()
asteroides.add(a1)
asteroides.add(a2)

arretJeu = False
while not arretJeu:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
               arretJeu = True
        else:
            asteroides.clear(ECRAN, fond )
            #a1.deplacer(ECRAN)
            asteroides.update()
            asteroides.draw(ECRAN)
            pygame.display.flip()
            horloge.tick(60)

pygame.quit()