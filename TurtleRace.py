from turtle import Turtle
from random import randint

laura = Turtle()

laura.color('red')
laura.shape('turtle')

rik = Turtle()
lauren = Turtle()
carrieanne = Turtle()

laura.penup()
laura.goto(-160,100)
laura.pendown()

rik.color('green')
rik.shape('turtle')
rik.penup()
rik.goto(-160, 70)
rik.pendown()

lauren.color('blue')
lauren.shape('turtle')
lauren.penup()
lauren.goto(-160,40)
lauren.pendown()

carrieanne.color('yellow')
carrieanne.shape('turtle')
carrieanne.penup()
carrieanne.goto(-160,10)
carrieanne.pendown()

input("press enter to close")



for movement in range(100):
    laura.forward(randint(1,5))
    rik.forward(randint(1,5))
    lauren.forward(randint(1,5))
    carrieanne.forward(randint(1,5))
    
