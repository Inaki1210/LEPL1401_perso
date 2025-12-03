README mission 8, créé par Iñaki Salomé-Parra et Louise Nuyens

Le programme mission 8 est fonctionnel. Les test effectués dans le programme même sont corrects.
Dans le fichier de tests, nous ne comprenons pas comment faire les tests des trois classes ensembles.
Pour le __main__, nous avons du utiliser ChatGPT parce que nous ne comprenions pas ce qui devait être fait.

Une erreur est survenue dans inginious. Voici l'erreur

Failed test:
============

'03:01:34' != '01:04:54'
- 03:01:34
+ 01:04:54
 : La méthode ajouter de votre classe Duree ne semble pas tenir compte du fait qu'il y a un nombre limité de secondes et de minutes possible.

----------------------------------------------------------------------
Ran 9 tests in 0.000s

FAILED (failures=1)


Le problème est résolut dans la dernière tentative. Le problème venait de la fonction ajouter de la Class Duree qui posait problème.