def count(cordonnees,i,j):
    t=(i,j)
    a = 0
    for k in range(len(cordonnees)):
            if cordonnees[k] == t:
                a+=1
    return a

print(count([(0,1),(2,3),(0,1),(4,5),(1,2),(0,1),(1,1),(0,2),(1,1)], 0,1))