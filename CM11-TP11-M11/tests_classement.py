import unittest
from linked_list import LinkedList 
from coureur import Coureur                      
from temps import Temps                 
from resultat import Resultat  
from OrderedLinkedList import OrderedLinkedList
from classement import Classement

class ClassementTest(unittest.TestCase):
    
    def setUp(self):
        self.class1 = Classement()
        self.coureur1 = Coureur("John", 20)
        self.coureur2 = Coureur("Bob", 32)
        self.coureur3 = Coureur("tibo", 16)
        
    def test_add(self):
        self.assertEqual(self.class1.size(), 0)
        self.class1.add(Resultat(self.coureur1, Temps(0, 13, 45)))
        self.assertEqual(self.class1.size(), 1)
        self.class1.add(Resultat(self.coureur2, Temps(0, 23, 12)))
        self.assertEqual(self.class1.size, 2)
    def test_get(self):
        self.class1.add(Resultat(self.coureur1, Temps(0, 13, 45)))
        self.assertEqual(self.class1.get(self.coureur1), Resultat(self.coureur1, Temps(0, 13, 45)))
        self.assertIsNone(self.class1.get(self.coureur3))
        
    def test_get_position(self):
        self.class1.add(Resultat(self.coureur1, Temps(0, 13, 45)))
        self.class1.add(Resultat(self.coureur2, Temps(0, 11, 12)))
        self.assertEqual(self.class1.get_position(self.coureur2), 1)
        self.assertEqual(self.class1.get_position(self.coureur1), 2)
        self.assertEqual(self.class1.get_position(self.coureur3), -1)
        
    def test_remove(self):
        self.class1.add(Resultat(self.coureur1, Temps(0, 13, 45)))
        self.class1.add(Resultat(self.coureur2, Temps(0, 12, 30)))
        self.assertEqual(self.class1.size(), 2)
        self.assertEqual(self.class1.remove(self.coureur1), self.coureur1)
        self.assertEqual(self.class1.size(), 1)
        self.assertEqual(self.class1.remove(self.coureur3), False)
        
    def test_str(self):
        self.class1.add(Resultat(self.coureur1, Temps(0, 13, 45)))
        self.class1.add(Resultat(self.coureur2, Temps(0, 12, 30)))
        self.class1.add(Resultat(self.coureur3, Temps(0, 14, 34)))
        att_str = (
            "1. Bob - Resultat(coureur=Bob, temps=Temps(0, 12, 30))\n"
            "2. John - Resultat(coureur=John, temps=Temps(0, 13, 45))\n"
            "3. Tibo - Resultat(coureur=Tibo, temps=Temps(0, 14, 34))\n"
        )
        self.assertEqual(str(self.class1), att_str)

        
if __name__ == "__main__":
    unittest.main()  