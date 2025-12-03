def equals(l,d):
    """
    Indique si un élément d'une liste est présent dans un dictionnaire

    Args :
    l, une liste à comparer
    d, un dictionaire, base de la comparaison

    Returns:
    True si toutes les valeurs de l sont dans d
    """
    countl = 0
    for i in range(len(l)):
        for j in range(len(l[i])):
            countl+=1
    countd = 0
    for m in range(len(d)):
        countd+=1
    
    if countl == countd:
        return False
    
    ok = False
    for k in d:
        if d[k] == l[k[0]][k[1]]:
            ok = True
        print(l[k[1]])
print(equals([[0,2,4],[4,1,0]],{(0,1):2,(0,2):4,(1,0):4,(1,1):1}))