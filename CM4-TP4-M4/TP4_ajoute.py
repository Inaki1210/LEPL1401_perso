#ajoute
l = [ 3, 1, 5, 4 ]

def ajoute(l,v):
    j = 1
    for i in range(len(l)):
        if l[i] == v:
            j = 0
    if j !=0:
        l.append(v)
    print(l)