#Martin Couture
#Mars 2025
#https://github.com/geocot/jeuPython
#Sound Effect by irinairinafomicheva from Pixabay
import pygame, random, math

from images import asteroide, collision, AbstractObjetJeuAnime, fusee, message

pygame.init() #Initialisation de Pygame
#Sons
pygame.mixer.init() #Initialisation du son
SON_BOUM = pygame.mixer.Sound("boum.mp3") #Constante pour le son boum de la fusée
SON_BIP = pygame.mixer.Sound("bip.mp3")#Constante pour le son d'arrivé d'un astéroïde
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
MESSAGES = pygame.sprite.Group()
FUSEES = pygame.sprite.Group()
COLLISIONS = pygame.sprite.Group()
ASTEROIDES = pygame.sprite.Group()


#Autres définitions des variables globales du jeu
fusee = fusee.Fusee(ECRAN.get_width() / 2, ECRAN.get_height() - 100, 5) #Création de la fusée
FUSEES.add(fusee) #Ajout de la fusée au groupe de sprites
asteroideVitesseMax = 1 #Vitesse maximum des astéroides
freezeGame = False #Arrêt des mouvements du jeu et non du jeu
nombreAsteroideCourant= 1 #Nombre d'astéroïde courant pour le jeu
pointage = 0  #Pointage de base du joueur

def ajoutAsteroide(): #Pour ajouter des astéroïdes
    global pointage #Variable globale pour les points. Les points sont calculés en rapport au nombre d'astéroïdes qui ont passé sur l'écran
    a = asteroide.Asteroide(random.randint(0, 1100), 0, random.randint(1, asteroideVitesseMax))
    a.image = a.image.copy().convert_alpha()
    ASTEROIDES.add(a)
    pointage +=1
    SON_BIP.play()


#********************
#***Départ du jeu****
#********************
arretJeu = False
while not arretJeu: #Tant que l'usager n'a pas cliquer sur le x de la fenêtre
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
               arretJeu = True
        else:
            if len(ASTEROIDES.sprites())< nombreAsteroideCourant: #Ajout des astéroïdes tout au long du jeu
                ajoutAsteroide()
            #Gestion de l'animation, on efface d'abord
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
                        a1.kill() #Supprime les astéroïdes qui se collisionnent
                        a2.kill() #Supprime les astéroïdes qui se collisionnent

            # Détection des collisions avec la fusée. Ici pour affichage par dessus les astéroïdes
            if pygame.sprite.groupcollide(FUSEES, ASTEROIDES, True, False):
                COLLISIONS.add(collision.Collision(fusee.rect.x - 35, fusee.rect.y, 0, 50))
                SON_BOUM.play()
                m = message.Message(LARGEUR_FENETRE/3,HAUTEUR_FENETRE/3,0, f"Oups c'est terminé, votre score {pointage}")
                MESSAGES.add(m)
                #Arrêt de l'animation lorsque collision entre la fusée et un astéroïde.
                freezeGame = True

            #Affiche le message de fin si le jeu est terminé
            if freezeGame:
                nombreAsteroideCourant = 0 #Arrêt des astéroïdes
                #afficheMessageFin()
                MESSAGES.draw(ECRAN)
                MESSAGES.update()

            ASTEROIDES.update() #Mise à jour des sprites des astéroïdes
            FUSEES.update() #Mise à jour de la fusée
            #Ajustement de la difficulté du jeu
            mSeconde = pygame.time.get_ticks() #Combien de temps s'est passé depuis le début du jeu
            asteroideVitesseMax = math.floor(mSeconde / 10000) + 1 #Augmente graduellement la vitesse des astéroïdes
            if nombreAsteroideCourant < NOMBRE_ASTEROIDES_MAX: #Augment graduellement le nombre d'astéroïde
                nombreAsteroideCourant = nombreAsteroideCourant + 0.01

            #Affiche le niveau et le score dans la barre de la fenêtre du jeu
            pygame.display.set_caption(f"Jeu de la fusée: Niveau {asteroideVitesseMax}: Score {pointage}")
            ASTEROIDES.draw(ECRAN)  # Dessine les astérïdes via le groupe de sprites

            COLLISIONS.draw(ECRAN) #Dessine les collisions via le groupe de sprites
            COLLISIONS.update() #Mise à jour des collisions via le groupe de sprites
            FUSEES.draw(ECRAN) #Affiche la fusée via le groupe de sprites
            pygame.display.flip() #Anime
            HORLOGE.tick(60) #60 image seconde




pygame.quit() #Termine le jeu