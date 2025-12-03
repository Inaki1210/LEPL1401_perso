#calcul des racines d'une équation du type x**a + y**b = z**c

max_x = int(input("Valeur maximale de x ?"))
max_y = int(input("Valeur maximale de y ?"))
max_z = int(input("Valeur maximale de z ?"))
a = int(input("Valeur de l'exposant de x ?"))
b = int(input("Valeur de l'exposant de y ?"))
c = int(input("Valeur de l'exposant de z ?"))
solutions = 0
    
for x in range(1,max_x):
    for y in range(1,max_y):
        for z in range(1,max_z):
            if x**a + y**b == z**c:
                print("x=",x,"y=",y,"z=",z)
                solutions+=1
if solutions !=0:
    print("solutions trouvés")
else:
    print("pas de solutions")