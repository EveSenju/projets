from random import *

class Personnage:
    def __init__(self, pseudo, genre, classe, niveau = 1, PV = 1, PM = 0, article = None ):
        self.pseudo = pseudo
        self.genre = genre
        self.classe = classe
        self.level = niveau
        self.PV = PV
        self.PM = PM
        if self.genre == "H":
            self.article = "le"
        elif self.genre == "F":
            self.article = "la"
        else:
            self.genre = input("Vous avez mal écrit votre genre, réécrivez le (H/F):")
        
    def classes(self):
        if self.classe == "Guerrier" or self.classe == "Guerrière" :
            self.arme_principale = "épée"
            self.arme_secondaire = "bouclier"
            self.PV = 250
            self.PM = 100
            return self.classe
        elif self.classe == "Archer" or self.classe == "Archère" :
            self.arme_principale = "Arc"
            self.arme_secondaire = "Dague"
            self.PV = 150
            self.PM = 100
            return self.classe
        elif self.classe == "Mage" :
            self.arme_principale = "Baguette magique"
            self.arme_secondaire = "Livre"
            self.PV = 100
            self.PM = 300
            return self.classe
        else :
            print("Classe non disponible ou mal écrite")
            self.classe = input("Choisissez une autre classe (Guerrier/Guerrière , Archer/Archère ou Mage) ? :")
            return self.classe
            
    def __repr__(self):
        return "\nSTATS:\n\nPseudo : "+self.pseudo+"\nGenre : "+self.genre+"\nClasse : "+self.classes()+"\nNiveau : "+str(self.level)+"\nPV : "+str(self.PV)+"\nPM : "+str(self.PM)

class Squelettes:
    def __init__(self, perso, PV, PM):
        self.niveau = randint(1,perso.level)
        self.PV = PV
        self.PM = PM
        





def Starto():
    Start = input("Voulez vous commencer l'Aventure ? (O/N) : ")
    if Start == "O" :
        pseudo = input("Quel est ton nom ?:")
        genre = input("Quel est ton genre ? (H/F):")
        classe = input("Quelle classe choisis-tu (Guerrier/Guerrière, Archer/Archère ou Mage) ?:")
        perso = Personnage(pseudo,genre, classe)
        print(perso)
        Aventure()
    elif Start == "N" :
        print("Tant pis, c'est la fin de la partie !")

def Aventure():
    Choix = input("Voulez vous commencer l'Aventure dans le Manoir ou dans la Forêt ? (M/F) : ")
    if Choix == 'M' :
        Manoir()
    elif Choix == 'F' :
        Foret()
    
def Manoir():
    print("Vous apparaissez dans un Manoir")

def Foret():
    print("Vous apparaissez dans une Forêt")





            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    