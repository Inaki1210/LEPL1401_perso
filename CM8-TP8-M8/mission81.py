class Duree :
    def __init__(self,h,m,s):
        """
        @pre: h, m et s sont des entiers positifs (ou zéro), m et s sont < 60
        @post: Crée une nouvelle durée en heures, minutes et secondes.
        """
        self.heure = h
        self.minute = 0
        self.seconde = 0

        if 0<=s and s<60:
            self.seconde+= s
        else:
            m+= s//60
            self.seconde+= s%60

        if 0<=m and m<60:
            self.minute+= m
        else:
            self.heure+= m//60
            self.minute+= m%60

    def to_secondes(self):
        """
        @pre:  -
        @post: Retourne le nombre total de secondes de cette instance de Duree (self).
        Par exemple, une durée de 8h 41m 25s compte 31285 secondes.
        """
        min_to_sec = self.minute * 60
        h_to_sec = self.heure * 3600
        total = self.seconde + min_to_sec + h_to_sec
        return total
    
    def delta(self,d) :
        """
        @pre:  d est une instance de la classe Duree
        @post: Retourne la différence en secondes entre cette durée (self)
               et la durée d passée en paramètre.
               Cette valeur renovoyée est positif si cette durée (self)
               est plus grand que la durée d, négatif sinon.
        Par exemple, si cette durée (self) est 8h 41m 25s (donc 31285 secondes)
        et la durée d est 0h 1m 25s, la valeur retournée est 31200.
        Inversement, si cette durée (self) est 0h 1m 25s et la durée
        d est 8h 41m 25s, alors la valeur retournée est -31200.
        """
        d = d.to_secondes()
        delta = self.to_secondes() - d
        return delta

    def apres(self,d):
        """
        @pre:  d est une instance de la classe Duree
        @post: Retourne True si cette durée (self) est plus grand que la durée
            d passée en paramètre; retourne False sinon.
        """
        if self.delta(d) >= 0:
            return True
        else :
            return False

    def ajouter(self,d):
        """
        @pre:  d est une instance de la classe Duree
        @post: Ajoute une autre durée d à cette durée (self),
            corrigée de manière à ce que les minutes et les secondes soient
            dans l'intervalle [0..60[, en reportant au besoin les valeurs
            hors limites sur les unités supérieures
            (60 secondes = 1 minute, 60 minutes = 1 heure).
            Ne retourne pas une nouvelle durée mais modifié la durée self.
        """
        d = d.to_secondes()
        duree = self.to_secondes()
        total_s = d + duree
        h = d//3600
        m = (d - h*3600)//60
        s = d - (h*3600) - (m *60)
        self.heure += m
        if 0 <= m and m<= 60:
            self.minute += m 
        if 0 <= s and s<= 60:
            self.seconde +=s

    

    def __str__(self):
        """
        @pre: -
        @post: Retourne cette durée sous la forme de texte "heures:minutes:secondes".
        Astuce: l'expression "{:02}:{:02}:{:02}".format(heures, minutes, secondes)
        retourne le string désiré avec les nombres en deux chiffres en ajoutant
        les zéros nécessaires.
        """
        return "{:02}:{:02}:{:02}".format(self.heure,self.minute, self.seconde)

d1 = Duree(10,20,59)
print(d1)
d2 = Duree(10,20,64)
print(d2)
d3 = Duree(10,59,61)
print(d3)
###

class Chanson :
    def __init__(self,t,a,d):
        """
        @pre:  t et a sont des string, d est une instance de la classe Duree
        @post: Crée une nouvelle chanson, caractérisée par un titre t,
            un auteur a et une durée d.
        """
        self.titre = t
        self.auteur = a
        self.duree = d

    def __str__(self):
        """
        @pre:  -
        @post: Retourne un string décrivant cette chanson sous le format
            "TITRE - AUTEUR - DUREE".
            Par exemple: "Let's_Dance - David_Bowie - 00:04:05"
        """
        return "{} - {} - {}".format(self.titre, self.auteur, self.duree)

class Album :
    def __init__(self, numero):
        """
        @pre:  numero est un entier identifiant de facon unique cet album
        @post: Crée un nouvel album, avec comme identifiant le numero,
            et avec une liste de chansons vide.
        """
        self.numero = numero
        self.album = []
        self.num_chanson = 0
        self.duree_al = Duree(0,0,0)
    
    def add(self,chanson):

        if self.num_chanson < 100:
            self.num_chanson+=1
            chanson_decompo = chanson.split(' ')

            titre = Chanson(chanson_decompo[0],chanson_decompo[1],duree)
            ligne = "{}: {}".format(self.num_chanson, titre)
            if self.duree_al.to_secondes() + duree.to_secondes() < 4500:
                self.album.append(ligne)
            else:
                return False
    def __str__(self):
        num = 0
        r = "Album" +" "+ self.numero + "(" +self.num_chanson + " chansons, " self.duree_al + ")" +"\n"
        for i in self.album:
            num +=1
            r+= "0"+ num + ": " + i +"\n"
        return r
if __name__ == "__main__":
    # Grâce à la ligne ci-dessus, le code ci-dessous ne sera exécuté que si on n'exécute ce fichier directement.
    # Ceci nous permet d'éviter que le code ci-dessous sera exécuté lorsqu'on fait un import de ce fichier,
    # par exemple dans notre fichier test.py
    pass
    # A COMPLETER PAR LES ETUDIANTS
    # (mettez ici votre code pour créer les albums à partir de la lecture du fichier 'music-db.txt')