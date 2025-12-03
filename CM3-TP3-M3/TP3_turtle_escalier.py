import turtle

wn = turtle.Screen()
yorick = turtle.Turtle()

i = 0

while i <3:
    yorick.forward(20)
    yorick.right(90)
    yorick.forward(20)
    yorick.left(90)
    i+=1
    
wn.mainloop()