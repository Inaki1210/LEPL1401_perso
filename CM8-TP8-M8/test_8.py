#tests de la mission 8 par Louise Nuyens et Iñaki Salomé-parra

# D'abord on doit importer les classe à tester
from mission8 import Duree, Chanson, Album

# CREATION DE QUELQUES OBJETS DE LA CLASSE Duree A TESTER
d0 = Duree(0,0,0)
d1 = Duree(10,20,59)
d2 = Duree( 8,41,25)
d3 = Duree(0,20,1)
d4 = Duree(1,19,45)
d5 = Duree(1,59,61)

# FONCTION POUT TESTER LA METHODE __str__ DE LA CLASSE Duree
def test_Duree_str() :
    assert d1.__str__() == "10:20:59", "Test 1 Duree __str__"
    assert d2.__str__() == "08:41:25", "Test 2 Duree __str__"
    assert d3.__str__() == "00:20:01", "Test 3 Duree __str__"
    assert d5.__str__() == "2:00:00"

    
# FONCTION POUR TESTER LA METHODE toSecondes DE LA CLASSE Duree
def test_Duree_to_secondes() :
    assert d1.to_secondes() == 37259, "Test 1 Duree toSecondes"
    assert d2.to_secondes() == 31285, "Test 2 Duree toSecondes"
    assert d3.to_secondes() == 1201, "Test 3 Duree toSecondes"

# FONCTION POUR TESTER LA METHODE delta DE LA CLASSE Duree
def test_Duree_delta():
    assert d1.delta(d0) == 37259, "test 1 Duree delta"
    assert d2.delta(d1) == -5974, "test 2 Duree delta"
    assert d1.delta(d2) == 5974, "test 3 Duree delta"

# FONCTION POUR TESTER  LA METHODE apres DE LA CLASSE Duree
def test_Duree_apres():
    assert d1.apres(d2),     "Test 1 Duree apres"
    assert not d0.apres(d1), "Test 2 Duree apres"
    assert d3.apres(d0) == True, "Test 3 Duree apres"

# FONCTION POUR TESTER LA METHODE ajouter DE LA CLASSE Duree
def test_Duree_ajouter():
    #cas 1
    d2.ajouter(d4)
    assert d2.heure == 10 and d2.minute == 1 and d2.seconde == 10, "test 1 Duree ajouter"

# APPEL DES DIFFERENTES FONCTIONS TEST
test_Duree_str()
test_Duree_to_secondes()
test_Duree_delta()
test_Duree_apres()
test_Duree_ajouter()

################################
# Tests pour la classe Chanson #
################################

# CREATION DE QUELQUES OBJETS DE LA CLASSE Chanson A TESTER
c = Chanson("Let's Dance", "David Bowie", Duree(0,4,5))

# FONCTION POUR TESTER LA METHODE __str__ DE LA CLASSE Chanson
def test_Chanson_str(chanson) :
    assert chanson.__str__() == "Let's Dance - David Bowie - 00:04:05"


# APPEL DES DIFFERENTES FONCTIONS TEST
test_Chanson_str(c)

##############################
# Tests pour la classe Album #
##############################

# CREATION D'UN OBJET DE LA CLASSE Album A TESTER
a1 = Album(21)
chanson_1 = Chanson("Let's_Dance", "David_Bowie",Duree(0,4,9))
chanson_2 = Chanson ("chanson_trop_longue", "personne",Duree(2,0,0))

# FONCTION POUR TESTER LA METHODE __str__ DE LA CLASSE Album
def test_Album__str__():
    assert a1.__str__() == "Album 21 (0 chansons, 00:00:00)", "test 1 Album __str__"
    a1.add(chanson_1)
    assert a1.__str__() == "Album 21 (1 chansons, 00:04:09)\n01: Let's_Dance - David_Bowie - 00:04:09", "test 2 Album __str__"

# FONCTION POUR TESTER LA METHODE add DE LA CLASSE Album
def test_Album_add():
    assert a1.add(chanson_1) == True, "test 1 Album add"
    assert a1.add(chanson_2) == False, "test 2 Album add"

# APPEL DES DIFFERENTES FONCTIONS TEST
test_Album__str__()
test_Album_add()

#####################################
# Test du comportement du programme #
#####################################

# QUELQUES TESTS ICI POUR TESTER QUE LES 3 CLASSES COLLABORENT CORRECTEMENT
# ET PEUVENT ETRE UTILISE POUR CREER DES ALBUMS DE CHANSONS SELON LES CONSIGNES
# DE LA MISSION
# Je ne comprends pas ce qui est à produire...