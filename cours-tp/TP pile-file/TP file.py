class File:
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
            
    
    
f = File()
f.enfile(7)
f.enfile(5)