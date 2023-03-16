import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

black_turtle = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(black_turtle.go_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    if black_turtle.ycor() == 280:
        black_turtle.go_back_to_original()
        scoreboard.add_score()
        car_manager.level_increase()

    for car in car_manager.all_cars:
        if black_turtle.distance(car) <= 30:
            scoreboard.game_over()
            game_is_on = False
        else:
            continue


screen.exitonclick()
