#calcul des racines d'une équation du type x**a + y**b = z**c
#ATTENTION, on ne doit prendre que les racines qui sont des nmbres premiers !!!
#Fait en coopération avec Antonin Vanderhasten.
max_x = int(input("Valeur maximale de x ?"))
max_y = int(input("Valeur maximale de y ?"))
max_z = int(input("Valeur maximale de z ?"))
a = int(input("Valeur de l'exposant de x ?"))
b = int(input("Valeur de l'exposant de y ?"))
c = int(input("Valeur de l'exposant de z ?"))
solutions = 0
div_commun = 0
solutions_sd = 0

print("Programme créé par Iñaki Salomé-Parra et Antonin Vanderhasten")
print("Attentions, les solutions ne seront comprisent que entre", max_x, "pour x", max_y,"pour y et",max_z,"pour z.")
for x in range(1,max_x+1):
    for y in range(1,max_y+1):
        for z in range(1,max_z+1):
            if x**a + y**b == z**c:
                for div in range(2,min(x,y,z)+1):
                    if x%div == 0 and y%div == 0 or x%div == 0 and z%div == 0 or y%div == 0 and z%div == 0:
                        div_commun+=1
                if div_commun == 0:
                    print("Voici une solution sans diviseurs communs :", x,y,z)
                    solutions_sd+=1
                else:
                    print("Voici une solution avec diviseurs communs :",x,y,z)
                solutions+=1

print("Il y a", solutions, "solution(s), dont", solutions_sd, "solutions sans diviseurs communs.")