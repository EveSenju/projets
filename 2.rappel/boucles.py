def puissance(nombre, n):
    acc = 1
    if n == 0:
        return 1
    elif n == 1:
        return nombre
    else:
        for i in range(1, n+1):
            acc = nombre * acc
        return acc

#print(puissance(5, 3))

def livret_epargne(somme, nb_annee):
    for i in range(1, nb_annee+1):
        somme = somme + (somme * 1.015)
    return round(somme)

#print(livret_epargne(1600, 10))

def voyelle(chaine):
    voyelles = ["a", "e", "i", "o", "u", "y"]
    voy = ""
    for i in voyelles:
        for j in chaine:
            if j == i:
                voy = chaine
    return voy


chaine = "coucou"
print(voyelle(chaine))
    
    
    
