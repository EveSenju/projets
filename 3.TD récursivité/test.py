def somme(a,b):
    if b > 0:
        return 1 + somme(a,b-1)
    else:
        return a

a = 5
b = 4

print(somme(a,b))