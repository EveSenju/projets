class Auteur:
    def __init__(self, nom_aut, annee_naiss, annee_mort):
        self.nom = nom_aut
        self.naissance = annee_naiss
        self.mort = annee_mort
        if self.mort == '':
            self.vivant = True
        else:
            self.vivant = self.mort
    def __repr__(self):
        return self.nom
    

class Livre:
    def __init__(self, titre_livre, genre_livre, auteur_livre):
        self.titre = titre_livre
        self.genre = genre_livre
        self.auteur = auteur_livre
    def __repr__(self):
        return self.titre
        
class Biblio:
    def __init__(self, rayon_biblio):
        self.rayon = rayon_biblio
        self.livres = []
    def __repr__(self):
        return self.livres

    def disponible(self, nom_livre):
        for livre in self.livres:
            if livre.titre == nom_livre:
                return True
        return False
    
    def ajout(self, livre):
        if livre.genre == self.rayon:
            self.livres.append(livre)
            return self.livres
        else:
            return False
        
    def prete_livre(self, livre):
        if livre.genre == self.rayon:
            if self.disponible(livre.titre) == True:
                num_element = 0
                while num_element < len(self.livres):
                    if self.livres[num_element].titre == livre.titre :
                        l = self.livres.pop(num_element)
                        return l
                    num_element += 1    
        else:
            return False
        
aut = Auteur("Bob Lennon", 1987, "")
aut2 = Auteur("Natoo", 1985, "")
aut3 = Auteur("Fuze", 1998,"")
aut4 = Auteur("Siphano", 1992,"")

livr = Livre("Les aventures de Billie et Bob","Fantastique","Bob Lennon")
livr2 = Livre("icônne","Fantastique","Natoo")
livr3 = Livre("Fuze et Didier","Aventure","Fuze")
livr4 = Livre("Siphaventure","Aventure","Siphano")

bibli = Biblio("Fantastique")
bibli2 = Biblio("Aventure")

bibli.ajout(livr)
bibli.ajout(livr2)

bibli2.ajout(livr3)
bibli2.ajout(livr4)




            
        
    
        











        
        
        