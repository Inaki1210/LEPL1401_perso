#Programme créé par Iñaki Salomé-Parra et Louise Nuyens, Groupe 11.97

"""
Classes fournies pour la mission 9; à compléter par les étudiants.
@author Kim Mens
@version 4 novembre 2021
"""

###############
### ARTICLE ###
###############

"""
Cette classe représente un Article de facture simple,
comprenant un descriptif et un prix.
   
@author Kim Mens
@version 4 novembre 2021
"""
class Article :

    def __init__(self,d,p):
        """
        @pre:  d un string décrivant l'article
               p un float représentant le prix HTVA en EURO d'un exemplaire de cet article 
        @post: Un article avec description d et prix p a été créé.
        Exemple: Article("carte graphique", 119.49)
        """
        self.__description = d
        self.__prix = p
        
    def description(self) :
        """
        @post: retourne la description textuelle décrivant l'article.
        """
        return self.__description

    def prix(self) :
        """
        @post: retourne le prix d'un exemplaire de cet article, hors TVA.
        """
        return self.__prix
        
    def taux_tva(self):
        """
        @post: retourne le taux de TVA (même valeur pour chaque article)
        """    
        return 0.21   # TVA a 21%

    def tva(self):
        """
        @post: retourne la TVA sur cet article
        """    
        return self.prix() * self.taux_tva()
 
    def prix_tvac(self):
        """
        @post: retourne le prix d'un exemplaire de cet article, TVA compris.
        """
        return self.prix() + self.tva()

    def __str__(self):
        """
        @post: retourne un string decrivant cet article, au format: "{description}: {prix}"
        """
        return "{0}: {1:.2f} EUR".format(self.description(), self.prix())

###############
### FACTURE ###
###############

"""
Cette classe représente une Facture, sous forme d'une liste d'articles.
   
@author Kim Mens
@version 4 novembre 2021
"""

class Facture :

    def __init__(self, d, a_list):
        """
        @pre  d est un string court décrivant la facture;
              a_list est une liste d'objets de type Article.
        @post Une facture avec une description d et un liste d'articles a_list été crée.
        Exemple: Facture("PC Store - 22 novembre", [ Article("carte graphique", 119.49) ])
        """
        self.__description = d
        self.__articles = a_list
        self.__num = 0
        self.__num+=1
        
    def description(self) :
        """
        @post: retourne la description de cette facture.
        """
        return self.__description
    
    def __str__(self):
        """
        @post: retourne la représentation string d'une facture, à imprimer avec la méthode print().
        (Consultez l'énoncé pour un exemple de la représentation string attendue.)
        """
        s = self.entete_str()
        totalPrix = 0.0
        totalTVA = 0.0
        for art in self.__articles :
            s += self.article_str(art)
            totalPrix = totalPrix + art.prix()
            totalTVA = totalTVA + art.tva()
        s += self.totaux_str(totalPrix, totalTVA)
        return s

    def entete_str(self):
        """
        @post: retourne une représentation string de l'entête de la facture, comprenant le descriptif
               et les entêtes des colonnes.
        """
        return "Facture " + "No " + str(self.__num) + ' ' + self.__description + "\n" \
               + self.barre_str() \
               + "| {0:<40} | {1:>10} | {2:>10} | {3:>10} |\n".format("Description","prix HTVA","TVA","prix TVAC") \
               + self.barre_str()

    def barre_str(self):
        """
        @post: retourne un string représentant une barre horizontale sur la largeur de la facture
        """
        barre_longeur = 83
        return "="*barre_longeur + "\n"

    def article_str(self, art):
        """
        @pre:  art une instance de la classe Article
        @post: retourne un string correspondant à une ligne de facture pour l'article art
        """
        return "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format(art.description(), art.prix(), art.tva(), art.prix_tvac())

    def totaux_str(self, prix, tva):
        """
        @pre:  prix un float représentant le prix total de la facture en EURO
               tva un float représentant le TVA total de la facture en EURO
        @post: retourne un string représentant une ligne de facture avec les totaux prix et tva,
               à imprimer en bas de la facture
        """
        return self.barre_str() \
               + "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format("T O T A L", prix, tva, prix+tva) \
               + self.barre_str()
           
    def nombre(self, pce) :
        """
        @pre:  pce une instance de la classe Piece
        @post: retourne le nombre d'articles de type ArticlePiece dans la facture,
               faisant référence à une pièce qui est égale à pce,
               en totalisant sur tous les articles qui contiennent une telle pièce.
        """
        compteur = 0
        for art in self.__articles:
            if type(art) == type(pce):
                if art == pce:
                    compteur+=1
        return compteur

    def print_livraison(self):
        """
        
        """
        total_art = 0
        total_pce = 0
        total_poids = 0.000
        fragile_fin = False

        print("Livraison" + " - "+ "Facture " + "No " + str(self.__num) + ' ' + self.__description + "\n" \
               + self.barre_str() \
               + "| {0:<40} | {1:>10} | {2:>10} | {3:>10} |\n".format("Description", "poids/pce", "nombre", "poids") \
               + self.barre_str() , end='')
        
        for art in self.__articles:
            if isinstance(art, ArticlePiece):
                total_art+= 1
                piece = art.piece()
                nombre = art.nombre()
                total_pce+= nombre
                poids_pce = piece.poids()
                poids_pces = str(format(float(piece.poids().split("kg")[0])*nombre,".3f"))+"kg"
                total_poids+= float(piece.poids().split("kg")[0])*nombre
                
            if piece.fragile():
                descr = piece.description()+" (!)"
                fragile_fin = True
            else:
                descr = piece.description()

            print("| {0:<40} | {1:>10} | {2:>10} | {3:>10} |".format(descr, poids_pce, nombre, poids_pces))

        print(self.barre_str(), end='')
        print("| {0:<40} | {1:>10} | {2:>10} | {3:>10} |".format(str(total_art)+" Articles", " ", total_pce, str(format(total_poids, ".3f"))+"kg"))
        print(self.barre_str(), end='')

        if fragile_fin:
            print("(!) *** livraison fragile ***", end='')
        
    def livraison_str(self):
        """
        Cette méthode est une méthode auxiliaire pour la méthode printLivraison
        """
        pass

#########################
### ARTICLEREPARATION ###
#########################

class ArticleReparation(Article):
    def __init__(self,descr,duree = 0):
        if isinstance(duree, (int, float)) and duree > 0:
            super().__init__(descr, 0)
            self.__duree = float(duree) #si la durée est renseignée
        else:
            super().__init__(descr, 0)
            self.__duree = 0 # Si la durée n'est pas renseignée ou négative

    def description(self):
        return "{} ({})".format(super().description(),str(self.__duree)+'heure')
    
    def prix(self):
        return 20+35*self.__duree

#############
### PIECE ###
#############

class Piece:
    def __init__(self,descr,eur_u,p_u = "0.000",fragile = False,TVA_min = False):
        self.__description = descr
        self.__prix = eur_u
        self.__poids = p_u
        self.__fragile = fragile
        self.__tva_reduit = TVA_min

    def description(self):
        return self.__description
    
    def prix(self):
        return float(self.__prix)
    
    def poids(self):
        if self.__poids == "0.000":
            return self.__poids
        else:
            return "{}".format(str(self.__poids)+'kg')
    
    def fragile(self):
        return self.__fragile
    
    def tva_reduit(self):
        return self.__tva_reduit
    
    def __eq__(self,other):
        if type(other) != type(self):
            return False
        else:
            if self.description() == other.description() and self.prix() == other.prix():
                return True
            else:
                return False
        
    def __str__(self):
        return "{0}: {1:.2f} EUR : {2} : {3} : {4}".format(self.description(), self.prix(), self.poids(), self.fragile(), self.tva_reduit())

####################
### ARTICLEPIECE ###
####################

class ArticlePiece(Article):
    def __init__(self,nb,piece):
        if isinstance(piece, Piece): # Si la pièce est dans la Classe Piece
            super().__init__(piece.description(), piece.prix()) 
            self.__piece = piece
            self.__nombre = nb
        else: # Si la pièce n'est pas dans la classe, alors on créé un objet vide
            self.__piece = None
            self.__nombre = 0

    def piece(self):
        return self.__piece
    
    def nombre(self):
        return self.__nombre
    
    def description(self):
        return str(self.__nombre)+' * '+str(super().description())+' @ ' + str(super().prix())

    def prix(self):
        return self.__nombre * self.piece().prix()
    
    def taux_tva(self):
        if self.piece().tva_reduit():
            return 0.06
        else:
            return 0.21 

########################
### RUNNING THE CODE ###
########################

articles_livraison = [ArticlePiece(1, Piece("disque dur 350 GB", 49.99, "0.355", fragile=True)),
                    ArticlePiece(3, Piece("souris bluetooth", 15.99, "0.176", fragile=False)),
                    ArticlePiece(5, Piece("adaptateur DVI - VGA", 12.00, "0.000", fragile=False)),
                    ArticlePiece(2, Piece("Java in a Nutshell", 24.00, "0.321", fragile=False)),
                    ArticlePiece(5, Piece("souris bluetooth", 15.99, "0.176", fragile=False))
                    ]

livraison_facture = Facture("PC Store - 22 novembre", articles_livraison)

def livraison(l):
    l.print_livraison()

livraison(livraison_facture)