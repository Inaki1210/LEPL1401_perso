# Programme créé par Iñaki Salomé-Parra et Hélène Dodrémont Groupe 11.97
# Tests de XYRobot.py

import unittest
from graphics import GraphWin, Line, Point 
from math import pi, cos, sin  
import XYRobot as XYR

class testXYRobot(unittest.TestCase):

    def setUp(self):
        self.robot_test = XYR.XYRobot("RT",100,100)
    
    def test_angle(self):
        self.assertEqual(self.robot_test.angle(), 0, "Le robot ne pointe pas vers 0°")
        self.robot_test.turn_right()
        self.assertEqual(self.robot_test.angle(), 90,"Le robot ne pointe pas vers 90°")
        self.robot_test.turn_right()
        self.assertEqual(self.robot_test.angle(), 180, "Le robot ne pointe pas vers 180°")
        self.robot_test.turn_left()
        self.assertEqual(self.robot_test.angle(), 90, "Le robot ne pointe pas vers 90°")

    def test_move(self):
        self.assertEqual(self.robot_test.position(), (100,100), "Le robot n'est pas à la position (100,100).")
        self.robot_test.move_forward(50)
        self.assertEqual(self.robot_test.position(), (150,100), "Le robot n'est pas à la position (150,100).")
        self.robot_test.move_backward(50)
        self.assertEqual(self.robot_test.position(), (100,100), "Le robot n'est pas à la position (100,100).")
        self.robot_test.turn_right()
        self.robot_test.move_forward(10)
        self.assertEqual(self.robot_test.position(), (100, 110), "Le robot n'est pas à la position (100,110).")
        self.robot_test.move_backward(10)
        self.assertEqual(self.robot_test.position(),(100,100), "Le robot n'est pas à la position (100,100)")
        self.robot_test.turn_right()
        self.robot_test.move_forward(10)
        self.assertEqual(self.robot_test.position(), (90,100), "Le robot n'est pas à la position (90,100)")
        self.robot_test.move_backward(10)
        self.assertEqual(self.robot_test.position(),(100,100), "Le robot n'est pas à la position (100,100)")

if __name__ == '__main__':
    unittest.main(verbosity=2)