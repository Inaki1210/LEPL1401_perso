#recherche

def recherche(m,v):
    a = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == v:
                a+=1
    if a !=0:
        return True
    else:
        return False
print(recherche([ [  0,  3,  2,  8 ],
  [  6,  5,  2,  1 ],
  [  7,  0,  3,  2 ] ],0))