#Nombre de diviseurs de chaque entiers entre 1 et n

n = 6
solutions = 0
for i in range(1,n+1):
    for j in range(2,n+1):
        if i%j == 0:
            solutions+=1
    print(i,":",solutions)
    solutions = 0
