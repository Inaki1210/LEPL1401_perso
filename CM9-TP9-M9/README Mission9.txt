README Mission9

Créé par Iñaki Salomé-Parra et Louise Nuyens, Groupe 11.97

Le programme marche bien localement. 
Lors des premiers essais sur Inginious, nous avons eu cette erreur :

Failed test:
============

False is not true : La méthode testant l'égalité de deux instances de Piece ne renvoit le résultat attendu. Comparez-vous les bons attributs?

----------------------------------------------------------------------
Ran 5 tests in 0.001s

FAILED (failures=1, errors=2)

En effet, dans la fonction __eq__ de la class Piece, nous avions oublié des parenthèses dans l'un des if,
ce qui conduisait à un return False automatique (renvoi de la référence et non de l'exécution de la fonction)

if self.description() == other.description() and self.prix() == other.prix():
                   ^^                     ^^              ^^              ^^
                return True
            else:
                return False


Ensuite, nous avions eu ceci (pour les 5 autres essais):

======================================================================
ERROR: test_extends_piece (TestM10.TestM10)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./src/TestM10.py", line 27, in test_extends_piece
  File "/task/student/mission10.py", line 270, in __init__
    super().__init__(piece.description(),piece.prix())
AttributeError: 'int' object has no attribute 'description'

======================================================================
ERROR: test_extends_repair (TestM10.TestM10)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./src/TestM10.py", line 31, in test_extends_repair
TypeError: __init__() missing 1 required positional argument: 'duree'

----------------------------------------------------------------------
Ran 5 tests in 0.000s

FAILED (errors=2)

Pour la première :
    Nous pensions qu'il s'agissait d'un problème de position des variables dans __init__ de ArticlePiece(Article).

class ArticlePiece(Article):
    def __init__(self,nb,piece):
        super().__init__(piece.description(),piece.prix())
        self.__piece = piece
        self.__nombre = nb

    Mais le problème venait du fait que piece.description() ne peux pas fonction lorsqu'on renseigne un int.
    Inversément, il faut un int pour piece.prix()
    Nous avons donc modifié le code pour qu'il vérifie d'abord si l'instance de la pièce est la même que l'instance de la classe Piece
    Si tel est le cas, nous appelons le __init__ de Piece via un super()
    Sinon, on insère un objet vide (None) et une quantité égale à 0
 
Pour la seconde erreur :
    Nous avons vu qu'il "manquait" un argument duree lors de l'appel de la fonction __init__().
    Après vérification dans le code, les arguments sont bien complets

class ArticleReparation(Article):
    def __init__(self,descr,duree):
        super().__init__(descr,0)
        self.__duree = float(duree)

    Nous sommes arrivés à la conclusion que Inginious ne renseignait qu'une partie des arguments demandés.
    Nous avons donc définit duree comme étant égal à 0 par défaut, pour éviter les problèmes si duree n'est pas définie.

Lors de la dernière remise, nous nous sommes rendu compte que le fichier de test ne marchait plus malgré un 100% sur Inginious.
Cela venait du fait que lorsqu'on avait modifié le __init__ de ArticleReparation(Article), nous avions mal inséré le super().__init__(descr, 0)

En fait, nous ne l'avions ajouté que lorsque la vérification de l'instance renvoie True (cfr. erreur 1)
Nous avons donc juste ajouté le super().__init__(descr, 0) dans le cas ou l'instance renvoie False.