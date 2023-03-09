import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_counter_clock():
    tim.circle(50, extent=-10)

def move_clock():
    tim.circle(50, extent=10)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backward, "b")
screen.onkey(turn_left, "d")
screen.onkey(turn_right, "a")
screen.onkey(tim.reset, "c")

screen.exitonclick()
