#Martin Couture
import pygame, random, math
from images import asteroide, collision, AbstractObjetJeuAnime, fusee, message

pygame.init() #Initialisation de Pygame
#Définition des variables de l'écran
HAUTEUR_FENETRE = 800
LARGEUR_FENETRE = 1200
COULEUR_FOND = (0,0,0)
pygame.display.set_caption("Jeu de la fusée") #Titre de la fenêtre
ECRAN = pygame.display.set_mode((LARGEUR_FENETRE, HAUTEUR_FENETRE))
fond = pygame.Surface(ECRAN.get_size())
fond.fill(COULEUR_FOND) #Définition du fond d'écran en noir
ECRAN.blit(fond, (0,0))
horloge = pygame.time.Clock() # Pour contrôler la fréquence


vitesse_max = 1




freezeGame = False
NOMBRE_ASTEROIDES_MAX = 30;
nombreAsteroide= 1
AbstractObjetJeuAnime.ObjetJeuAnime.setEcran(ECRAN) #initialisation de l'écran dans la méthode static dont hérite les objets animés
#Respecter l'ordre d'affichage
fusees = pygame.sprite.Group()
fusee = fusee.Fusee(ECRAN.get_width() / 2, ECRAN.get_height() - 100, 5)
fusees.add(fusee)
collisions = pygame.sprite.Group()
asteroides = pygame.sprite.Group()

point = 0
def ajoutAsteroide():
    global point
    asteroides.add(asteroide.Asteroide(random.randint(0, 1100), 0, random.randint(1, vitesse_max)))
    point +=1

arretJeu = False
while not arretJeu:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
               arretJeu = True
        else:
            if len(asteroides.sprites())< nombreAsteroide:
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
                        collisions.add(collision.Collision(a1.rect.x, a1.rect.y, 0,  10))
                        collisions.add(collision.Collision(a2.rect.x, a1.rect.y, 0, 10))
                        a1.kill()
                        a2.kill()

            # Détection des collisions avec la fusée
            if pygame.sprite.groupcollide(fusees, asteroides, True, False):
                collisions.add(collision.Collision(fusee.rect.x-35, fusee.rect.y, 0,  50))

                #Arrêt de l'animation lorsque collision.
                freezeGame = True

            if not freezeGame:
                asteroides.update()
                fusees.update()
                mSeconde = pygame.time.get_ticks()
                vitesse_max = math.floor(mSeconde / 10000)+1
                if nombreAsteroide < NOMBRE_ASTEROIDES_MAX:
                    nombreAsteroide = nombreAsteroide + 0.01

                pygame.display.set_caption(f"Jeu de la fusée: Niveau {vitesse_max}: Score {point}")



            collisions.draw(ECRAN)
            asteroides.draw(ECRAN)
            collisions.update()
            fusees.draw(ECRAN)
            pygame.display.flip()
            horloge.tick(60)


pygame.quit()