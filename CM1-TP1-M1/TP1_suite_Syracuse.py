#suite de Syracuse
a = 22 #introduction du premier terme de la suite

print(a)
while a>1:  #définition de la boucle tant que a > 1
    if a %2 ==0: #cas ou a est pair (donc le reste de la division par 2 est égal à 0)
        a = a//2 #calcul du prochain terme
        print(a)
    else: #autre cas ou a est impair
        a = 3*a + 1 #calcul du prochain terme
        print(a)