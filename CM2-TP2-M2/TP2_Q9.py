n = 31
sum = 0
for i in range((n+1)*2): #Le *2 permet de prendre deux fois plus de termes pour avoir n termes pairs
    if i%2 == 0: #sélection des n termes pairs
        sum+=i #ajout du terme pair itéré a la somme
print(sum)