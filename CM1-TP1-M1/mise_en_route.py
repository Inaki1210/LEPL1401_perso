# fonction print pour les nombres de 1 à 10, leurs carrés et la somme de leurs carrés

a = 1 #nombre a mettre au carré
b = 0 

while a<=10: 
    i = a**2 #nombre mis au carré et en mémoire dans i (pour print plus facile)
    b+=i #somme des n premiers carrés (à partir du carré en mémoire i)
    c = (a*(a+1)*(2*a+1))//6 #autre méthode de calcul de somme, mis en mémoire c
    print(a, "\t", i,"\t", b, "\t", c)
    a+=1
