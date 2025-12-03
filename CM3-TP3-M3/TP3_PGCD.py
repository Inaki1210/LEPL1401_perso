#PGCD

def greatest_divisor(a):
    """
    pré :  a est un entier
    post : retourne le PGCD de a, none si a = 0 ou a = 1
    """
    if a == 0 or a == 1:
        return None
    else:
        PGCD  = 0
        for i in range(1,a+1):
            if a%i == 0:
                PGCD = i
        return PGCD