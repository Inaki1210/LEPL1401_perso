#Décompte à partir de 5.
#marque un message de fin.
#CM1

i = 5 					#mise en mémoire de 5 dans la variable i
while i >= 0 :  		#boucle sous condition : tant que i est supérieur ou égal à 0
    if i != 0 : 		#dans la boucle, si i est différent de 0, alors 
        print(i) 		#donne la valeur de i
    else : 				#si la condition if est fausse, alors :
        print("Décollage") #imprime Décollage
    i = i - 1 			#diminue la valeur de i de 1 pour la prochaine boucle
print("Réussi") 		#imprime réussi lorsque la boucle est finie (fin du programme)