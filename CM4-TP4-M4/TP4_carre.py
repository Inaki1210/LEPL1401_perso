#TP4, carré

def carre(n):
    l=[]
    for i in range(n):
        l.append([])
        for j in range(n):
            k = i*n+j
            l[i].append(k)
    return l