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
        if self.est_vide() == True:
            return None
        else:
            return self.pile.pop()
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
    for i in chaine_nombres:
        if i == ' ':
            pass
        elif i == "1" or i == "2"  or i == "3" or i == "4" or i == "5" or i == "6"  or i == "7" or i == "8" or i == "9":
            p.empile(i)
        elif i == "+":
            nb1 = p.depile()
            nb2 = p.depile()
            res = int(nb2) + int(nb1)
            p.empile(str(res))
        elif i == "*":
            nb1 = p.depile()
            nb2 = p.depile()
            res = int(nb2) * int(nb1)
            p.empile(str(res))
        elif i == "-":
            nb1 = p.depile()
            nb2 = p.depile()
            res = int(nb2) - int(nb1)
            p.empile(str(res))
        elif i == "/":
            nb1 = p.depile()
            nb2 = p.depile()
            res = int(nb2) / int(nb1)
            p.empile(str(res))
    else:
        return p
            
b = "1 3 + 5 *"
print(calculatrice(b))           
        
        

    
        
        
"""       
p = Pile()
p.empile(5)
p.empile(8)
p.empile(14)
p.empile(7)
"""



        