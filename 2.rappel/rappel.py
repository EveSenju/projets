import doctest
from math import sqrt

"""
            1. Syntaxe python
1) Quel mot clé permet de définir une fonction?

le mot clef pour définir une fonction est 'def'

2) Quels sont les deux types de boucles? Comment les différencier ?

les 2 types de boucles sont les boucles 'for' (définis) et 'while' (indéfinis)

3) Que signifie le mot clé return ?

le mot clef 'return' sert à renvoyer le résultat d'une fonction sans l'afficher

4) Que signifie la fonction print( )

la fonction 'print()' sert à afficher le résultat

2. Rappel 1 ère :

2. 1. Plus grand que :

Ecrire un prédicat plus_grand_que(a,b) qui prend en paramètre a et b et renvoie True si a est supérieur à b.
"""
"""
def IHM():
    a = int(input('donne un 1er nombre:'))
    b = int(input('donne un 2e nombre:'))
    cote1 = int(input('donne la taille du 1e côté:'))
    cote2 = int(input('donne la taille du 2e côté:'))
    hypothenuse = int(input("donne la taille de l'hypothenuse:"))
    t = [5, 9, 3, 1, 7]
    return(plus_grand_que(a,b), Pythagore(cote1, cote2, hypothenuse), somme(t))
"""
t = [5, 9, 3, 1, 7]
a = 5
b = 4

def plus_grand_que(a,b):
    """
    Renvoye True si a est plus grand que b et False si b est plus grand que a
    
    :param a: (int) un entier
    :param b: (int) un entier
    :return: (booléen) True ou False
    :CU: type(a) == (int) && type(b) == (int)
    
    example:
    >>> plus_grand_que(1,4)
    False
    """
    if a > b:
        return(True)
    else:
        return(False)




#2. 2. Pythagore :
#Ecrire une fonction Pythagore(cote1,cote2,hypothenuse) qui renvoie un booléen si les trois côtés forment un triangle rectangle


def Pythagore(cote1, cote2, hypothenuse):
    """
    dis si un triangle est rectangle
    :param cote1: (int) un entier
    :param cote2: (int) un entier
    :param hypothenus: (int) un entier
    :return: (str) renvoit le triangle est rectangle ou le triangle n'est pas rectangle
    :CU: type(cote1) == (int) && type(cote2) == (int) && type(hypothenuse) == (int)
    
    example:
    >>> Pythagore(3, 4, 5)
    'Le triangle est rectangle'
    """
    cote_carre = cote1**2
    cote_carre_deux = cote2**2
    hypothenuse_carre = hypothenuse**2
    cote_add = cote_carre + cote_carre_deux
    if cote_add == hypothenuse_carre:
        return('Le triangle est rectangle')
    else:
        return("Le triangle n'est pas rectangle")


#2. 3. Tableaux :
#Ecrire une fonction somme(t) qui additionne tous les éléments d'un tableau.


def somme(t):
    """
    Additionne tout les nombres dans une liste
    :param t: (list) valeur
    :return: (int) le résultat
    
    example:
    >>> somme(t)
    121
    """
    r = 0
    for i in t:
        r += i
    return(r)


#2. 4. Fonction de tri :
#Expliquez le tri par sélection et le tri par insertion avec des exemples.


def insertion(t):
    ti = []
    for i in t:
        ti.append(i)
    return(t, ti)

#print(IHM())



#9,7,10,4,2,6
#2,9,7,10,4,6
#2,4,10,7,9,6
#2,4,6,7,9,10



t = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
v = 13

def recherche_dichotomique(t, v):
    """
    Fonction qui applique la recherche dichotomique dans un tableau
    param tableau : Tableau où l'on va rechercher une valeur
    param valeur : valeur à retrouver
    return : Renvoie l'indice de la position de val, -1 si val n'est pas dans le tableau
    
    example:
    >>> recherche_dichotomique(t,v)
    6
    """

    debut = 0
    fin = len(t)-1
    while debut != fin :
        milieu = (debut + fin)//2
        if t[milieu] > v :
            fin = milieu-1
        elif t[milieu] < v :
            debut = milieu+1
        elif t[milieu] == v :
            return milieu
    return "-1"



print(recherche_dichotomique(t, v))
"""
def dentiste(texte):
    voyelle = ["a", "e", "i", "o", "u", "y"]
    phrase = ''
    for i in texte:# 2.for i in range(len(texte)):
        for j in voyelle:# 1.if i in voyelle: 
            if i == j: #2.if texte[i] in voyelle
                phrase += i #2.phrase += texte[i]
    return phrase

"""
def dentiste_while(texte):
    voyelle = ["a", "e", "i", "o", "u", "y"]
    phrase = ''
    i = 0
    while i <= (len(texte)-1):
        if texte[i] in voyelle:
            phrase += texte[i]
        i += 1
    return phrase

texte = "il fait chaud"

#print(dentiste(texte))

if __name__ == '__main__':
    doctest.testmod(verbose=True)








