def longueur(tab):
    """
    fonction qui prend en entrée une liste/ un tableau, et
    qui renvoit le nombre d'éléments dans la liste/ le tableau
    :param: tab (list)
    
    Exemple:
    >>>longueur(tab[1, 2, 3, 4])
    >>> 4 
    """
    if len(tab) == 0:
        return "Tableau vide"
    else:
        if len(tab) == 1:
            return 1
    return 1 + longueur(tab[1:])
        
        
tab = [1, 2, 3, 4, 5]
#print(longueur(tab))


class Voiture:
    def __init__(self, pui, coul, jeun = None):
        self.puissance = pui
        self.couleur = coul
        self.jeune_conducteur = jeun
        if self.puissance <= 100:
            self.jeune_conducteur = True 
        else:
            self.jeune_conducteur = False
    
    def reprogrammation(self, nouvelle_puissance):
        self.puissance = nouvelle_puissance
        if self.puissance <= 100:
            self.jeune_conducteur = True 
        else:
            self.jeune_conducteur = False
    
    def __repr__(self):
        print(self.puissance)
        print(self.jeune_conducteur)
        
        
        
        
    
    
v = Voiture(50, 'jaune')
#v.reprogrammation(101)









