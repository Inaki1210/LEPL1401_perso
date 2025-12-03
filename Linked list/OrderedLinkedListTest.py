import unittest
from OrderedLinkedList import OrderedLinkedList

class TestOrderedLinkedList(unittest.TestCase):

    def setUp(self):
        # Cette méthode est appelée avant chaque test
        self.empty_list = OrderedLinkedList()
        self.non_empty_list = OrderedLinkedList([3, 1, 2])

    def test_initialisation_vide(self):
        # Test de l'initialisation d'une liste vide
        self.assertEqual(self.empty_list.size(), 0)
        self.assertIsNone(self.empty_list.first())

    def test_initialisation_avec_elements(self):
        # Test de l'initialisation avec des éléments
        self.assertEqual(self.non_empty_list.size(), 3)
        self.assertEqual(self.non_empty_list.first().value(), 1)
        self.assertEqual(
            self.non_empty_list.first().next().value(), 2)
        self.assertEqual(
            self.non_empty_list.first().next().next().value(), 3)

    def test_ajout_element(self):
        # Test de l'ajout d'un élément
        self.empty_list.add(5)
        self.assertEqual(self.empty_list.size(), 1)
        self.assertEqual(self.empty_list.first().value(), 5)

    def test_ajout_plusieurs_elements(self):
        # Test de l'ajout de plusieurs éléments
        self.empty_list.add(10)
        self.empty_list.add(5)
        self.empty_list.add(7)
        self.assertEqual(self.empty_list.size(), 3)
        self.assertEqual(self.empty_list.first().value(), 5)
        self.assertEqual(
            self.empty_list.first().next().value(), 7)
        self.assertEqual(
            self.empty_list.first().next().next().value(), 10)

    def test_suppression_element(self):
        # Test de la suppression d'un élément
        self.non_empty_list.remove()
        self.assertEqual(self.non_empty_list.size(), 2)
        self.assertEqual(self.non_empty_list.first().value(), 2)

    def test_position_element(self):
        # Test de la position d'un élément
        self.assertEqual(self.non_empty_list.getPosition(1), 1)
        self.assertEqual(self.non_empty_list.getPosition(3), 3)
        self.assertEqual(self.non_empty_list.getPosition(4), -1)

if __name__ == '__main__':
    unittest.main()