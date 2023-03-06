#from turtle import Turtle,Screen
#
#timmy = Turtle()
#timmy.shape("turtle")
#timmy.color("cyan")
#
#for i in range(4):
#  timmy.forward(100)
#  timmy.right(90)

#import heroes
#print(heroes.gen())

##### Challenge 2 ##################
from turtle import Turtle, Screen

lin = Turtle()

#for i in range(10):
#  lin.forward(10)
#  lin.pu()
#  lin.forward(10)
#  lin.pd()

############# Challenge 3 ##############

#for i in range(3):
#  lin.forward(100)
#  lin.right(120)
#
#for i in range(4):
#  lin.forward(100)
#  lin.right(90)
#
#for i in range(5):
#  lin.forward(100)
#  lin.right(360/5)

import random

def color():
  screen = Screen()
  screen.colormode(255)
  R = random.randrange(0, 257, 10)
  G = random.randrange(0, 257, 10)
  B = random.randrange(0, 257, 10)
  lin.pencolor((R,G,B))

#for i in range(3,11):
#  color()
#  for index in range(i):
#    lin.forward(100)
#    lin.right(360/i)

################# Challenge 4 #############

#lin.pensize(10)
#angle = [0, 90, 180, 270]
#
#for i in range(200):
#    color()
#    lin.speed(0)
#    lin.forward(30)
#    lin.setheading(random.choice(angle))

def random_color():
    screen = Screen()
    screen.colormode(255)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color

##############Challenge 5##################

for i in range(1,360):
    if i % 5 == 0:
        lin.setheading(i)
        lin.speed(0)
        lin.color(random_color())
        lin.circle(100)
    else:
        continue


screen = Screen()
screen.exitonclick()
