class Pile:
    def __init__(self):
        self.pile = []
        
    def est_vide(self):
        return self.pile == []
    
    def empile(self, nombre):
        #self.pile += [nombre]
        self.pile.append(nombre)
        
    def top(self):
        return self.pile[-1]
    
    def taille(self):
        return len(self.pile)
    
    def depile(self):
        if len(self.pile) != 0:
            return self.pile.pop()
        else:
            return None
            #self.pile = self.pile[:len(self.pile)-1]
        
    def __repr__(self):
        long = len(self.pile)-1
        s = ""
        while long >= 0:
            s+= str(self.pile[long])+'\n'
            long -=1
        return s

def bon_parent(chaine_de_characteres):
    parent = Pile()
    for i in chaine_de_characteres:
        if i == "(" or i == "[":
            parent.empile(i)
        elif i == ")" or i == "]":
            these = parent.depile()
            if these == False:
                return False
            else:
                if i == ")":
                    if these != "(":
                        return False
                else:
                    if these != "[":
                        return False
        else:
            pass
    return parent.est_vide()
                        
 
def calculatrice(chaine_nombres):
    p = Pile()
    v = 0
    while v <= len(chaine_nombres)-1:
        if chaine_nombres[v] in "0123456789":
            var = ""
            while chaine_nombres[v] != " ":
                var += chaine_nombres[v]
                v += 1
            p.empile(var)
        elif chaine_nombres[v] == "+":
            nb1 = p.depile()
            nb2 = p.depile()
            res = int(nb2) + int(nb1)
            p.empile(str(res))
        elif chaine_nombres[v] == "*":
            nb1 = p.depile()
            nb2 = p.depile()
            res = int(nb2) * int(nb1)
            p.empile(str(res))
        elif chaine_nombres[v] == "-":
            nb1 = p.depile()
            nb2 = p.depile()
            res = int(nb2) - int(nb1)
            p.empile(str(res))
        else:
            pass
        v += 1
    return p.depile()

#b = "14 2 *"
#calculatrice(b)           
       
def trie_pile(pile):
    pile_trier = Pile()
    pile_temp = Pile()
    pile_trier.empile(pile.depile())
    while pile.est_vide() == False:
        if pile.top() > pile_trier.top():
            while pile_trier.est_vide() == False and pile.top() > pile_trier.top():
                pile_temp.empile(pile_trier.depile())
            pile_trier.empile(pile.depile())
            while pile_temp.est_vide != False:
                pile_trier.empile(pile_temp.depile())
        else:
            pile_trier.empile(pile.depile())
    while pile_trier.est_vide() == False:
        pile_temp.empile(pile_trier.depile())
    while pile_temp.est_vide() == False:
        pile.empile(pile_temp.depile())
    
    


pil = Pile()
pil.empile(5)
pil.empile(14)
pil.empile(8)
pil.empile(27)
pil.empile(2)
pil.empile(7)
print(trie_pile(pil))

    
        
        
"""       
p = Pile()
p.empile(5)
p.empile(8)
p.empile(14)
p.empile(7)
"""



        