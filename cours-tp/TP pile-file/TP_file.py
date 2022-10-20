#1er class
class File1:
    def __init__(self):
        self.file = []
        
    def est_vide(self):
        return self.file == []
    
    def enfile(self, nombre):
        #self.pile += [nombre]
        self.file = [nombre] + self.file
        
    def top(self):
        return self.file[0]
    
    def taille(self):
        return len(self.file)
    
    def defile(self):
        if len(self.pile) != 0:
            return self.file.pop()
        else:
            return None
            #self.pile = self.pile[:len(self.pile)-1]
    def vide_file(self):
        for i in self.file:
            self.defile(i)
        
    def __repr__(self):
        long = len(self.file)-1
        s = ""
        while long >= 0:
            s+= str(self.file[long])+'\n'
            long -=1
        return s
    def ajout_elem(self, nombre):
        if self.taille() >= 7:
            return "Sorry"
        else:
            self.enfile(nombre)
            
    
"""
pour la 1er class
f = File()
f.enfile(7)
f.enfile(5)
print(f)
"""

class File2:
    def __init__(self, element, suivant = None):
        self.element = element
        self.suivant = suivant
    def enfile(self, element):
        self.suivant = File(self.element, self.queue)
        self.element = element
    def est_vide(self):
        if self.element == None:
            if self.suivant != None:
                return True and self.suivant.est_vide()
            else:
                return True
        else:
            return False
    def defile(self):
        if self.est_vide():
            return False
        elif self.suivant.suivant == None:
            val = self.suivant.element
            self.suivant = None
            return val
        elif self.suivant == None:
            val = self.element
            self.element = None
            return val
        else:
            self.suivant.defile()
    def top(self):
        if self.suivant != None:
            return self.suivant.top()
        else:
            return self.element
    def taille(self):
        if self.suivant == None:
            return 1
        else:
            return 1 + self.suivant.taille()
            
            





