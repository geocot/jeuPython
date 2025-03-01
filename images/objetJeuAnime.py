from images import objetJeu
class ObjetJeuAnime(objetJeu.ObjetJeu):
    "Permet d'être la base des objets animés autre que le joueur"

    def __init__(self, coordXDepart, coordYDepart, vitesse ):#, fichierSon):
        super().__init__(coordXDepart,coordYDepart)
        self._vitesse = vitesse



