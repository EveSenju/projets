def IHM():
    print(phrase())
    print(division())
    print(phrases())


def phrase():
    chaine = input("Ecrire une phrase: ")
    return("Cette phrase à été écrite par l'utilisateur:"+' '+chaine)

def division():
    nombre = int(input("Donne un nombre: "))
    nombre_carre = nombre**2
    if nombre_carre % 2 == 0:
        return ("Le nombre écrit élevé au carré est divisible par 2")
    else:
        return ("Le nombre écrit élevé au carré n'est pas divisible par 2")


def phrases():
    chaine_caract = input("Ecrivez une phrase:")
    if len(chaine_caract) <= 30:
        chaine_caract2 = input("Ecrivez une 2e phrase:")
        chaine_carac = chaine_caract + chaine_caract2
        if len(chaine_caract) < 30:
            return "Malgré 2 tentatives la phrase est trop courte"
        else:
            return "Après 2 tentatives l'utilisateur a écrit une phrase d'au moins 30 caractères"
    else:
        return "L'utilisateur à écrit une phrase de 30 caractères en une seue tentative"
 
IHM()
                 
    
    
    
    

    
    