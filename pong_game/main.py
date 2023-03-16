from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
from net import Net

screen = Screen()

screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pong game")
screen.tracer(0)

NET_POSITION = [(0,0), (0,80), (0,-80), (0,160), (0,-160), (0, -240), (0, -320)]

for i in NET_POSITION:
    new_net = Net(i)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

def for_score():
    time.sleep(1)
    if i % 2 == 0:
        ball.reset_position()
    else:
        ball.reset_position()
        ball.bounce_y()

game_is_on = True
while game_is_on:

    for i in range(1000):
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()


        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
            ball.bounce_x()


        if ball.xcor() == 390:
            for_score()
            scoreboard.l_point()
        if ball.xcor() == -390:
            for_score()
            scoreboard.r_point()


screen.exitonclick()