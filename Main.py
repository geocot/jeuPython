#Martin Couture
import pygame, random, math
from images import asteroide, collision, AbstractObjetJeuAnime, fusee, message

pygame.init() #Initialisation de Pygame
pygame.display.set_caption("Jeu de la fusée") #Titre de la fenêtre
#Définition des variables de l'écran et création de l'écran
HAUTEUR_FENETRE = 800
LARGEUR_FENETRE = 1200
COULEUR_FOND = (0,0,0)
ECRAN = pygame.display.set_mode((LARGEUR_FENETRE, HAUTEUR_FENETRE))
FOND = pygame.Surface(ECRAN.get_size())
FOND.fill(COULEUR_FOND) #Définition du fond d'écran en noir
ECRAN.blit(FOND, (0, 0))
HORLOGE = pygame.time.Clock() # Pour contrôler la fréquence
AbstractObjetJeuAnime.ObjetJeuAnime.setEcran(ECRAN) #initialisation de l'écran dans la méthode static dont hérite les objets animés

#Constantes du jeu
NOMBRE_ASTEROIDES_MAX = 30; #Constante pour le nombre d'astéroïdes max à afficher.
#Respecter l'ordre d'affichage
FUSEES = pygame.sprite.Group()
COLLISIONS = pygame.sprite.Group()
ASTEROIDES = pygame.sprite.Group()

fusee = fusee.Fusee(ECRAN.get_width() / 2, ECRAN.get_height() - 100, 5)
FUSEES.add(fusee)
asteroideVitesseMax = 1 #Vitesse maximum des astéroides
freezeGame = False #Arrêt des mouvements du jeu et non du jeu
nombreAsteroideCourant= 1


point = 0
def ajoutAsteroide():
    global point
    ASTEROIDES.add(asteroide.Asteroide(random.randint(0, 1100), 0, random.randint(1, asteroideVitesseMax)))
    point +=1

arretJeu = False
while not arretJeu:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
               arretJeu = True
        else:
            if len(ASTEROIDES.sprites())< nombreAsteroideCourant:
                ajoutAsteroide()

            ASTEROIDES.clear(ECRAN, FOND)
            COLLISIONS.clear(ECRAN, FOND)
            FUSEES.clear(ECRAN, FOND)

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
            asteroidesList = ASTEROIDES.sprites()
            for i, a1 in enumerate(asteroidesList):
                for a2 in asteroidesList[i + 1:]:
                    if pygame.sprite.collide_mask(a1, a2):
                        COLLISIONS.add(collision.Collision(a1.rect.x, a1.rect.y, 0, 10))
                        COLLISIONS.add(collision.Collision(a2.rect.x, a1.rect.y, 0, 10))
                        a1.kill()
                        a2.kill()

            # Détection des collisions avec la fusée
            if pygame.sprite.groupcollide(FUSEES, ASTEROIDES, True, False):
                COLLISIONS.add(collision.Collision(fusee.rect.x - 35, fusee.rect.y, 0, 50))

                #Arrêt de l'animation lorsque collision.
                freezeGame = True

            if not freezeGame:
                ASTEROIDES.update()
                FUSEES.update()
                mSeconde = pygame.time.get_ticks()
                asteroideVitesseMax = math.floor(mSeconde / 10000) + 1
                if nombreAsteroideCourant < NOMBRE_ASTEROIDES_MAX:
                    nombreAsteroideCourant = nombreAsteroideCourant + 0.01

                pygame.display.set_caption(f"Jeu de la fusée: Niveau {asteroideVitesseMax}: Score {point}")



            COLLISIONS.draw(ECRAN)
            ASTEROIDES.draw(ECRAN)
            COLLISIONS.update()
            FUSEES.draw(ECRAN)
            pygame.display.flip()
            HORLOGE.tick(60)


pygame.quit()