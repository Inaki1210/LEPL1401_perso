#calcul des racines d'une équation du type x**a + y**b = z**c
#ATTENTION, on ne doit prendre que les racines qui sont des nmbres premiers !!!
max_x = int(input("Valeur maximale de x ?"))
max_y = int(input("Valeur maximale de y ?"))
max_z = int(input("Valeur maximale de z ?"))
a = int(input("Valeur de l'exposant de x ?"))
b = int(input("Valeur de l'exposant de y ?"))
c = int(input("Valeur de l'exposant de z ?"))
div_commun=0
    
for x in range(1,max_x):
    for y in range(1,max_y):
        for z in range(1,max_z):
            if x**a + y**b == z**c:
                for div in range(2,min(x,y,z)+1):
                    if x%div == 0 and y%div == 0 or x%div == 0 and z%div == 0 or y%div == 0 and z%div == 0:
                        div_commun+=1
                if div_commun == 0:
                    print("Voici une solution sans diviseurs communs :", x,y,z)
                else:
                    print("Voici une solution avec diviseurs communs :",x,y,z)