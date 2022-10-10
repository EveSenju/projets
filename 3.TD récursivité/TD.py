def factorielle(n):
    if n == 1:
        return n
    else:
        return n * factorielle(n-1)
#print(factorielle(4))

def mystere(i,k):
    if i<=k :
        print(i)
        mystere(i+1,k)
#mystere(0,10)

def nb_chiffre(n):
    if n < 10:
        return 1
    else:
        return 1 + nb_chiffre(n//10)
    
    
    

#print(nb_chiffre(50))
    
def maximum(t):
    if len(t) == 1:
        return t[0]
    elif len(t) == 0:
        return "tableau vide"
    else:
        return max(t[0], maximum(t[1:]))
        
   
#t = [0, 1, 2, 75000, 14, 50]
#print(maximum(t))    
    
def dentiste(texte):
    voyelles = ["a","e","i","o","u","y"]
    if len(texte) == 1:
        if texte[0] in voyelles:
            return texte[0]
    else:
        if texte[0] in voyelles:
            return texte[0] + dentiste(texte[1:])
        else:
            return dentiste(texte[1:])

#texte = "j'ai mal"
#print(dentiste(texte))

def syracuse(u):
    if u == 0:
        return ("le nombre doit être supérieur à 1")
    elif u == 1:
        return ("le nombre doit être supérieur à 1")
    else:
        if u % 2 == 1:
            print(u)
            return syracuse(3*u+1)
        else:
            print(u)
            return syracuse(u//2)
syracuse(5)


    
    
    
    
    
    
    
    
    
    