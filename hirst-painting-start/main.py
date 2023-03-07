###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
from turtle import Turtle, Screen
import random

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

timmy = Turtle()
screen = Screen()

screen.colormode(255)
timmy.speed(0)
timmy.pu()
timmy.hideturtle()

for i in range(10):
    timmy.goto(-200, i*50 - 200)
    for i in range(10):
        timmy.dot(20, random.choice(rgb_colors))
        timmy.forward(50)



screen.exitonclick()