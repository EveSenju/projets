import turtle
"""
def courbe_koch(n, cote):
    if n == 0:
        turtle.forward(cote)
    else:
        turtle.forward(cote)
        turtle.left(60)
        turtle.forward(cote)
        turtle.right(120)
        turtle.forward(cote)
        turtle.left(60)
        turtle.forward(cote)
        if n%2 == 1:
            turtle.left(60)
            courbe_koch(n-1, cote)
        else:
            turtle.right(120)
            courbe_koch(n-1, cote)

n = 15
cote = 40

courbe_koch(n, cote)

def courbe_koch_2(n, cote):
    if n != 0:
        courbe_koch_2(n-1, cote/3)
        turtle.left(60)
        courbe_koch_2(n-1, cote/3)
        turtle.right(120)
        courbe_koch_2(n-1, cote/3)
        turtle.left(60)
        courbe_koch_2(n-1, cote/3)
    else:
        turtle.forward(cote)

#courbe_koch_2(3, 300)

def flocon(n, l, i=3):
    if i != 0:
        courbe_koch_2(n, l)
        turtle.left(-120)
        flocon(n, l, i-1)

flocon(2, 400)


def coef(n, p):
    if p == 0 or n == p:
        return 1
    else:
        return coef(n-1, p-1) + coef(n-1, p)

def triangle_pascal():
    for i in range(6):
        for j in range(i+1):
            print(coef(i, j), end=" ")
        print()

triangle_pascal()
      

def recherche_dichotomique(t, v):
    fin = len(t)-1
    debut = 0
    if debut <= fin:
        milieu = (debut + fin) //2
        if t[milieu] == v:
            return True
        elif t[milieu] > v:
            return recherche_dichotomique(t[:milieu], v)
        elif t[milieu] < v:
            return recherche_dichotomique(t[milieu+1:], v)
    return False

t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
v = 12
print(recherche_dichotomique(t, v))

def recherche_recur(t, v):
    if len(t) == 1:
        return t[0] == v
    else:
        milieu = len(t)//2
        if t[milieu] > v:
            return recherche_recur(t[:milieu], v)
        else:
            return recherche_recur(t[milieu:], v)

print(recherche_recur(t, v))
"""

def combine_tableau(tab1, tab2):
    if len(tab1) == 0 and len(tab2) == 0:
        return []
    elif len(tab1) == 0:
        return tab2
    elif len(tab2) == 0:
        return tab1
    else:
        if tab1[0] > tab2[0]:
            return [tab2[0]] + combine_tableau(tab1, tab2[1:])
        elif tab1[0] < tab2[0]:
            return [tab1[0]] + combine_tableau(tab1[1:], tab2)
        
  


tab1 = [2, 3, 5]
tab2 = [1, 4]
print(combine_tableau(tab1, tab2))






        


