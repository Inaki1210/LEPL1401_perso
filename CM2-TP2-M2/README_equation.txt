Développement du programme equation.py :
Fait par Antonin Vanderhasten et Iñaki Salomé-Parra

La première étape est de déterminer les valeurs maximales des variables x, y et z.
C'est aussi le moment de déterminer la valeur des exposants a,b et c (des variables x, y et z)
Ces nombres sont définis dans la console pr l'utilisateur grâce à la fonction input (ces valeurs sont transformés en int).
Nous déterminons aussi trois variables optionnelles :
    solutions qui donnera le nombre de solutions totales
    div_commun qui détermine le nombre de diviseurs communs dans un jeu de solutions
    solutions_sd qui donne le nombre de solutions sans diviseurs communsµ

Au début, un print annonce que les solutions seront bornées par les valeurs maximales renseignées

Ensuite, nous évaluons chaque couple de solutions via 3 boucles for, une pour chaque variables.
Ensuite, nous vérifions l'égalité de l'équation.
Si elle est confirmée, nous vérifions ensuite la présence de diviseurs communs.
    Pour cela, nous regardons les modulos des potentiels diviseurs (créés par une boucle for).
    Si le modulo de deux variables est égal a 0, alors il y a un diviseur commun et la variable div_commun augmente de 1.

PourPour montrer les solutions sans diviseurs communs, une condition if est ajoutée.
    Si div_commun est égal a 0, il n'y a pas de diviseurs commun et le programme affiche le résultat en mentionnant l'absence de diviseurs communs.
    En plus de cela, la variable solutions_sd augmente de 1.
    
    Dans le cas ou div_commun est différent de 0, le programme affiche la solution en mentionnant le fait qu'il y a des diviseurs communs.
    
    Pour montrer que le programme a finit, il marque le nombre de réponses totales et sans diviseurs communs (stockés dans les variables solutions_sd et solutions)
    
    
    La partie avec les diviveurs communs n'a pas été facile. Il aura fallu plusieurs tentatives pour y parvenir.
    Lors des premiers essais, certains jeu de solutions étaient mal cataloguées ou apparaissaient en double.
    D'autres essais ne donnaient que les jeux avec diviseurs et supprimaient les jeux premiers entre eux.
    Au final, le problème a été décomposée et la question des diviseurs communs a été étudiée dans un autre programme pour être inséré par après pour ne pas endommager le code déjà fonctionnel et ne pas se tromper dans la forme.