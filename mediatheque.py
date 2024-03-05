import unittest

# classe d'un medium avec ses attributs privés
class Medium(object):
    def __init__(self,titre,auteur,date):
        self.__titre = titre
        self.__auteur = auteur
        self.__date = date
        self._pret = ""

    @property
    def titre(self):
        return self.__titre
    @property
    def auteur(self):
        return self.__auteur
    @property
    def date(self):
        return self.__date
    @property
    def pret(self):
        return self._pret
    @pret.setter
    def pret(self,nom):
        self._pret = nom
    
# classe Livre à partie d'un medium, avec des attributs en plus
class Livre(Medium):
    def __init__(self,titre,auteur,date,pages,editeur):
        super().__init__(titre,auteur,date)
        self.__pages = pages
        self.__editeur = editeur

    @property
    def pages(self):
        return self.__pages
    @property
    def editeur(self):
        return self.__editeur
    
# medium de type CD
class CD(Medium):
    def __init__(self,titre,auteur,date,duree,morceaux):
        super().__init__(titre,auteur,date)
        self.__duree = duree
        self.__morceaux = morceaux

    @property
    def duree(self):
        return self.__duree
    @property
    def morceaux(self):
        return self.__morceaux

# medium de type DVD
class DVD(Medium):
    def __init__(self,titre,auteur,date,duree):
        super().__init__(titre,auteur,date)
        self.__duree = duree

    @property
    def duree(self):
        return self.__duree

# medium de type Article de Magazine
class ArticleDeMagazine(Medium):
    def __init__(self,titre,auteur,date,magazine,numero,pages):
        super().__init__(titre,auteur,date)
        self.__magazine = magazine
        self.__numero = numero
        self.__pages = pages

    @property
    def magazine(self):
        return self.__magazine
    @property
    def numero(self):
        return self.__numero
    @property
    def pages(self):
        return self.__pages

# creation d'un interface interactive avec l'utilisateur afin de remplir un mediatheque
class Mediatheque(object):
    def __init__(self):
        self.__base_de_donnee = []

    # ajouter un medium dans la mediatheque
    def ajouter_medium(self):
        type_medium = input("Entrez le type de medium (Livre, CD, DVD, ArticleDeMagazine) : ").strip().lower()
        titre = input("Entrez le titre du medium : ")
        auteur = input("Entrez l'auteur du medium : ")
        date = input("Entrez la date du medium : ")

        if type_medium == "livre":
            pages = input("Entrez le nombre de pages du livre : ")
            editeur = input("Entrez l'éditeur du livre : ")
            medium = Livre(titre, auteur, date, pages, editeur)
        elif type_medium == "cd":
            duree = input("Entrez la durée du CD : ")
            morceaux = input("Entrez les morceaux du CD (séparés par des virgules) : ").split(",")
            medium = CD(titre, auteur, date, duree, morceaux)
        elif type_medium == "dvd":
            duree = input("Entrez la durée du DVD : ")
            medium = DVD(titre, auteur, date, duree)
        elif type_medium == "article de magazine":
            magazine = input("Entrez le nom du magazine : ")
            numero = input("Entrez le numéro du magazine : ")
            pages = input("Entrez les pages de l'article (séparées par des virgules) : ").split(",")
            medium = ArticleDeMagazine(titre, auteur, date, magazine, numero, pages)
        else:
            print("Type de medium non reconnu.")
            return

        self.__base_de_donnee.append(medium)

    # pouvoir lister tous les medias de la mediatheque d'un auteur 
    def lister_medias(self,auteur):
        liste = []
        for i in range(0,len(self.__base_de_donnee)):
            if self.__base_de_donnee[i].auteur == auteur:
                liste.append(self.__base_de_donnee[i].titre)
        return liste

    # supprimer un medium à partir de l'autre et du titre
    def supp_medium(self,auteur,titre):
        liste = self.__base_de_donnee[:]
        for i in liste:
            if i.auteur == auteur:
                if i.titre == titre:
                    self.__base_de_donnee.remove(i)
    
    # suppression de plusieurs medias à partir de l'auteur
    def supp_medias(self, auteur):
        liste = self.__base_de_donnee[:]
        for i in liste:
            if i.auteur == auteur:
                self.__base_de_donnee.remove(i)
    
    # enregistrer les prets effectués
    def preter(self, titre,nom):
        for i in range(0,len(self.__base_de_donnee)):
            if self.__base_de_donnee[i].titre == titre:
                self.__base_de_donnee[i].pret = f"{titre} a été prêté à {nom}"

    # pouvoir compter tous les prêts faits
    def compter_prets(self):
        pret = 0
        for i in range(0,len(self.__base_de_donnee)):
            if self.__base_de_donnee[i].pret != "":
                pret = pret + 1
        return pret
    
    # afficher tous les medias de la mediatheque
    def afficher(self):
        print("Voici la liste des medias:")
        for i in range(0,len(self.__base_de_donnee)):
            print(f"titre: {self.__base_de_donnee[i].titre}, auteur: {self.__base_de_donnee[i].auteur}")
        

def main():
    # Création d'une instance de Mediatheque
    mediatheque = Mediatheque()

    while True:
        # Affichage du menu
        print("\nMenu:")
        print("1. Ajouter un média")
        print("2. Lister les médias d'un auteur")
        print("3. Supprimer un média")
        print("4. Supprimer tous les médias d'un auteur")
        print("5. Preter un média")
        print("6. Afficher tous les médias")
        print("7. Compter les médias prêtés")
        print("8. Quitter")

        # Demande à l'utilisateur de choisir une option
        choix = input("Choisissez une option (1-8) : ")

        # Exécution de l'option choisie
        if choix == "1":
            mediatheque.ajouter_medium()
        elif choix == "2":
            auteur = input("Entrez le nom de l'auteur : ")
            liste_medias = mediatheque.lister_medias(auteur)
            print(f"Liste des médias de {auteur} : {liste_medias}")
        elif choix == "3":
            auteur = input("Entrez le nom de l'auteur du média à supprimer : ")
            titre = input("Entrez le titre du média à supprimer : ")
            mediatheque.supp_medium(auteur, titre)
            print("Le média a été supprimé.")
        elif choix == "4":
            auteur = input("Entrez le nom de l'auteur des médias à supprimer : ")
            mediatheque.supp_medias(auteur)
            print("Les médias de cet auteur ont été supprimés.")
        elif choix == "5":
            titre = input("Entrez le titre du média à prêter : ")
            nom_emprunteur = input("Entrez le nom de la personne à qui le média est prêté : ")
            mediatheque.preter(titre, nom_emprunteur)
            print(f"{titre} a été prêté à {nom_emprunteur}.")
        elif choix == "6":
            mediatheque.afficher()
        elif choix == "7":
            nb_prets = mediatheque.compter_prets()
            print(f"Il y a {nb_prets} médias prêtés.")
        elif choix == "8":
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez choisir une option valide (1-8).")

# execution du programme
if __name__ == "__main__":
    main()



# PARTIE TEST
class TestMedium(unittest.TestCase):
    def test_Livre(self):
        SAO = Livre("SAO","Lea",2010,400,"Poches")
        self.assertEqual(SAO.titre,"SAO")
        self.assertEqual(SAO.editeur,"Poches")

    def test_CD(self):
        Milet = CD("Like","Milet",2016,25,4)
        self.assertEqual(Milet.morceaux,4)

    def test_DVD(self):
        Pokemon = DVD("Pokemon","Lala",2001,120)
        self.assertEqual(Pokemon.duree,120)

class TestMediatheque(unittest.TestCase):
    def setUp(self):
        self.mediatheque = Mediatheque()

    def test_ajouter_medium(self):
        print("Test: test_ajouter_medium")
        livre = Livre("Titre", "Auteur", "2022-01-01", 200, "Éditeur")
        self.mediatheque.ajouter_medium(livre)
        self.assertEqual(len(self.mediatheque._Mediatheque__base_de_donnee), 1)

    def test_lister_medias(self):
        print("Test: test_lister_medias")
        livre = Livre("Titre", "Auteur", "2022-01-01", 200, "Éditeur")
        self.mediatheque.ajouter_medium()
        liste = self.mediatheque.lister_medias("Auteur")
        self.assertEqual(liste, ["Titre"])

    def test_supp_medium(self):
        livre = Livre("Titre", "Auteur", "2022-01-01", 200, "Éditeur")
        self.mediatheque.ajouter_medium(livre)
        self.mediatheque.supp_medium("Auteur", "Titre")
        self.assertEqual(len(self.mediatheque._Mediatheque__base_de_donnee), 0)

    def test_supp_medias(self):
        livre1 = Livre("Titre 1", "Auteur", "2022-01-01", 200, "Éditeur")
        livre2 = Livre("Titre 2", "Auteur", "2022-01-01", 200, "Éditeur")
        self.mediatheque.ajouter_medium(livre1)
        self.mediatheque.ajouter_medium(livre2)
        self.mediatheque.supp_medias("Auteur")
        self.assertEqual(len(self.mediatheque._Mediatheque__base_de_donnee), 0)

    def test_preter(self):
        livre = Livre("Titre", "Auteur", "2022-01-01", 200, "Éditeur")
        self.mediatheque.ajouter_medium(livre)
        self.mediatheque.preter("Titre", "Emprunteur")
        self.assertEqual(livre.pret, "Titre a été prêté à Emprunteur")

    def test_compter_prets(self):
        livre1 = Livre("Titre 1", "Auteur", "2022-01-01", 200, "Éditeur")
        self.mediatheque.ajouter_medium(livre1)
        livre2 = Livre("Titre 2", "Auteur", "2022-01-01", 200, "Éditeur")
        self.mediatheque.ajouter_medium(livre2)
        self.mediatheque.preter("Titre 2", "Emprunteur")
        self.assertEqual(self.mediatheque.compter_prets(), 1)
