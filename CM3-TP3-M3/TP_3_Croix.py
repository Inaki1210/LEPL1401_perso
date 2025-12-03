    hauteur = int(input("Hauteur de la croix: "))

    def croix(str,int):
        milieu = hauteur//2
        for i in range(hauteur):
            if i == milieu:
                print('X'*hauteur)
            else:
                print(" "*milieu + 'X')
        
