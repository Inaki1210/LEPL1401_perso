def triangle(n):
    l  = []
    for i in range(0,n+1):
        l.append([])
        for j in range(0,i+1):
            l[i].append(j)
    return(l)
