#table de multiplication de 123 ? Boucle while et 123 stocké en mémoire.
#variable de calcul n qui augmente a chaque itération. Itérations limitées à 10

a = 123
n = 1
while n <=10:
    print(a, 'x', n, "\t" ,a*n) #ajout en print du calcul (a, 'x', n) et de la réponse séparée par la tabulation.
    n+=1