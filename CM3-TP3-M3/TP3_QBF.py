n = 0

while True:
    n = int(input("Entrez un nombre (-1 pour arrêter) : "))
    def compteur(n):
        if n <=0:
            return 0
        if n == 1:
            return 1
        for i in range(n):
            if 10**i > n:
                return i
    
    def chiffres_pairs(n):
        if n <= 0:
            return False
        if compteur(n)%2 == 0:
            return True
        else:
            return False
    
    if n < 0:
        break
    if chiffres_pairs(n):
        print(n, " a un nombre pair de chiffres dans sa représentation décimale")
    else:
        print(n, " a un nombre impair de chiffres dans sa représentation décimale")