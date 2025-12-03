#Programme créé par Iñaki Salomé-Parra et Louise Nuyens, Groupe 11.97

"""
Tests fournis pour la mission 9; à compléter par les étudiants.
@author Kim Mens
@version 4 novembre 2021
"""

from mission9 import Article, Facture, ArticleReparation, Piece, ArticlePiece # type: ignore

"""
Test initial pour la classe Article.
@author Kim Mens
@version 4 novembre 2021
"""
articles = [ Article("laptop 15\" 8GB RAM", 743.79),
             Article("installation windows", 66.11),
             Article("installation wifi", 45.22),
             Article("carte graphique", 119.49)
             ]

def test_articles(a_list) :
    for art in a_list :
        print(art)

"""
Test initial pour la classe Facture.
@author Kim Mens
@version 4 novembre 2020
"""
facture = Facture("PC Store - 22 novembre", articles)

def test_facture(f) :
    print(f)

#####################################
### Section faite pour la mission ###
#####################################


"""
Test pour la classe ArticleReparation.
"""
reparation = ArticleReparation('réparation','0.75')

def test_reparation(r):
    print(r)

"""
Test pour la classe Piece.
"""
piece1 = Piece("souris bluetooth",'15.99','0.176')
piece2 = Piece("Java in a Nutshell",'24.00','0.321',False,True)

def test_piece(p):
    print(p)

"""
Test pour la classe ArticlePiece.
"""
articles.append(ArticlePiece(3,piece1))
articles.append(ArticlePiece(2,piece2))

def test_articlepiece(ap):
    print(ap)

"""
Test pour le borderaux de livraison.
"""
articles_livraison = [ArticlePiece(1, Piece("disque dur 350 GB", 50.00, "0.355", fragile=True)),
                    ArticlePiece(3, Piece("souris bluetooth", 15.99, "0.176", fragile=False)),
                    ArticlePiece(5, Piece("adaptateur DVI - VGA", 5.00, "0.000", fragile=False)),
                    ArticlePiece(2, Piece("Java in a Nutshell", 24.00, "0.321", fragile=True))
                    ]

livraison_facture = Facture("PC Store - 22 novembre", articles_livraison)

def test_livraison(l):
    l.print_livraison()
"""
Faire exécuter les différents tests.
"""

if __name__ == "__main__":

    print("\n*** TEST DE LA CLASSE Article ***\n")
    test_articles(articles)

    print("\n*** TEST DE LA CLASSE Facture ***\n")
    test_facture(facture)

    print("\n*** TEST DE LA CLASSE ArticleReparation***\n")
    test_reparation(reparation)
    print("\n TEST EN CONDITION Facture \n")
    articles.append(ArticleReparation('Réparation','0.75'))
    test_facture(facture)

    print("\n*** TEST DE LA CLASS Piece***\n")
    test_piece(piece1)
    test_piece(piece2)

    print("\n***TEST DE LA CLASSS ArticlePiece***\n")
    test_articlepiece(piece1)
    test_articlepiece(piece2)
    print("\n TEST EN CONDITION Facture \n")
    test_facture(facture)

    print("\n***TEST DU BORDERAUX DE LIVRAISON***\n")
    test_livraison(livraison_facture)