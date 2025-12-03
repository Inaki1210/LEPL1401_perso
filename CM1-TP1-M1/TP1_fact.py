x = 5 #définition de la factorielle a étudier
fact = 1 #factorielle de 1 qui va "grimper" jusque x
for n in range(x): #boucle for qui va "chercher" la factorielle a étudier
    fact = fact*(n+1) #caclul de la plus grande factorielle calculée
print(fact)
    