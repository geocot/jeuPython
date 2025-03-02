#Martin Couture
import pygame, random
from images import asteroide, collision, AbstractObjetJeuAnime, fusee

pygame.init()

HAUTEUR_FENETRE = 800
LARGEUR_FENETRE = 1200
COULEUR_FOND = (0,0,0)
VITESSE_MAX = 2
NOMBRE_ASTEROIDES_MAX = 20
ECRAN = pygame.display.set_mode((LARGEUR_FENETRE, HAUTEUR_FENETRE))
fond = pygame.Surface(ECRAN.get_size())
fond.fill(COULEUR_FOND)
ECRAN.blit(fond, (0,0))
horloge = pygame.time.Clock() # Pour contrôler la fréquence

AbstractObjetJeuAnime.ObjetJeuAnime.setEcran(ECRAN) #initialisation de l'écran dans la méthode static dont hérite les objets animés
collisions = pygame.sprite.Group()
asteroides = pygame.sprite.Group()
fusees = pygame.sprite.Group()
fusee = fusee.Fusee(ECRAN.get_width()/2 ,ECRAN.get_height() -100, 5)
fusees.add(fusee)

def ajoutAsteroide():
    asteroides.add(asteroide.Asteroide(random.randint(0, 1100), 0, random.randint(1, VITESSE_MAX)))


arretJeu = False
while not arretJeu:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
               arretJeu = True
        else:
            if len(asteroides.sprites())< NOMBRE_ASTEROIDES_MAX:
                ajoutAsteroide()
            asteroides.clear(ECRAN, fond )
            collisions.clear(ECRAN, fond)
            fusees.clear(ECRAN,fond)

            #Détection des flèches gauches et droites pour le mouvement de la fusée.
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                fusee.controle("g")
            if keys[pygame.K_RIGHT]:
                fusee.controle("d")
            if keys[pygame.K_UP]:
                fusee.controle("h")
            if keys[pygame.K_DOWN]:
                fusee.controle("b")

            #Détection des collisions entre astéroïde
            asteroidesList = asteroides.sprites()
            for i, a1 in enumerate(asteroidesList):
                for a2 in asteroidesList[i + 1:]:
                    if pygame.sprite.collide_mask(a1, a2):
                        collisions.add(collision.Collision(a1.rect.x, a1.rect.y, 0))
                        collisions.add(collision.Collision(a2.rect.x, a1.rect.y, 0))
                        a1.kill()
                        a2.kill()


            collisions.draw(ECRAN)
            asteroides.update()
            asteroides.draw(ECRAN)
            collisions.update()
            fusees.draw(ECRAN)
            fusees.update()
            pygame.display.flip()
            horloge.tick(60)

pygame.quit()