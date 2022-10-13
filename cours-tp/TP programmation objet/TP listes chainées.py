class Liste:
    def __init__(self, conte, point_suiv=None):
        """
        Fonction qui initialise la class Liste, pour créer une liste chainnes
        param: conte (int/str)
        param: point_suiv (var)
        """
        self.contenu = conte
        self.suivant = point_suiv
    
    def est_vide(self):
        """
        Renvoie Vrai si la liste est vide.

        :return: (bool) Vrai si la liste est vide, Faux sinon.
        :CU: aucune

        Exemple:
        >>> l1 = Liste()
        >>> l1.est_vide()
        True
        >>> l2 = Liste([1,2,3])
        >>> l2.est_vide()
        False
        """
        if self.contenu == None:
            if self.suivant != None:
                return True and self.suivant.est_vide()
            else:
                return True
        else:
            return False

    def ajoute_element_queue(self, contenu):
        if self.suivant == None:
            self.suivant = Liste(contenu)
        else:
            self.suivant.ajoute_element_queue(contenu)
    def fonc_len(self):
        if self.suivant == None: 
            return 1
        else:
            return 1+self.suivant.fonc_len()
    def extrait_element(self, element):
        if self.contenu == element:
            return 0
        else:
            if self.suivant == None:
                return 1  
            else:
                return 1 + self.suivant.extrait_element(element)
    def __repr__(self):
        s = "["
        s += str(self.contenu)
        suivant = self.suivant
        while suivant != None:
            s += ', '
            s += str(suivant.contenu)
            suivant = suivant.suivant
        return s + ']' 
    def __add__(self, other):
        self.ajoute_element_queue(other.contenu)
        suivant = other.suivant
        while suivant != None:
            self.ajoute_element_queue(suivant.contenu)
            suivant = suivant.suivant
            


m3 = Liste(3)
m2 = Liste(2, m3)
m1 = Liste(1, m2)
print(m1)

m6 = Liste(6)
m5 = Liste(5, m6)
m4 = Liste(4, m5)
m1 + m4

print(m1)
        
        
        
        
        