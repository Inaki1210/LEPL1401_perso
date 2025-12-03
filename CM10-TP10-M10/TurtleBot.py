
import turtle as t
from math import pi, cos, sin

class TurtleBot:
    move = False
    turn = False
    distance = 0
    direction = ''
    x = 0
    y = 0
    angle_rad = 0

    def __init__(self,name):
        self.__name = name
        self.t = t.Turtle()
        self.__list = []

    def __str__(self):
        if TurtleBot.move == True:
            return str(self.__name)+" move : "+str(TurtleBot.distance)
        else:
            return str(self.__name)+" direction : "+TurtleBot.direction

    def move_forward(self, distance=0):
        self.t.forward(distance)
        TurtleBot.move = True
        TurtleBot.distance = distance
        TurtleBot.x += distance * cos(TurtleBot.angle_rad)
        TurtleBot.y += distance * sin(TurtleBot.angle_rad)
        self.__list.append(("Move forward", distance))
        
    def move_backward(self,distance=0):
        self.t.backward(distance)
        TurtleBot.move = True
        TurtleBot.distance = -distance
        TurtleBot.x -= distance * cos(TurtleBot.angle_rad)
        TurtleBot.y -= distance * sin(TurtleBot.angle_rad)
        self.__list.append(("Move backward", distance))
        
    def turn_left(self,angle=90):
        self.t.left(angle)
        TurtleBot.turn = True
        TurtleBot.direction = 'left'
        TurtleBot.angle_rad+= pi/2 
        self.__list.append(("Turn left", angle))

    def turn_right(self,angle=90):
        self.t.right(angle)
        TurtleBot.turn = True
        TurtleBot.direction = 'right'
        TurtleBot.angle_rad-= pi/2
        self.__list.append(("Turn right", angle))

    def position(cls) :
        return (cls.x,cls.y)

    def angle(cls) :
        "retourne l'angle en degres représentant la direction du robot"    
        return ( cls.angle_rad * 180 / pi ) % 360
    
    def history(self):
        return self.__list
    
    def unplay(self):
        for i in range(len(self.__list)):
            element = len(self.__list) -i
            if self.__list[element][0] == "Move forward":
                TurtleBot.move_backward(self.__list[element][1])
            if self.__list[element][0] == "Move backward":
                TurtleBot.move_forward(self.__list[element][1])
            if self.__list[element][0] == "Turn left":
                TurtleBot.turn_right()
            if self.__list[element][0] == "Turn right":
                TurtleBot.turn_left()
            self.__list = []