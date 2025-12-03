#diviseurs entier de variable n.
#les diviseurs ne peuvent être plus grands que n.
n = 2048 #définition de la variable n
i = 1 #définition du 1er diviseur. 0 ne peut être le premier.
while i <= n: #Boucle fonctionnant tant que le diviseur est inférieur ou égal a n. Voir l2 pour raison.µ
    if n % i == 0 :
        print(i)
    i+=1