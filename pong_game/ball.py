from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        self.setpos(0,0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.setpos(0, 0)
        self.move_speed = 0.1
        self.bounce_x()



    #def right_down(self):
    #    new_x = self.xcor() + 10
    #    new_y = self.ycor() - 10
    #    self.goto(new_x, new_y)
#
    #def left_up(self):
    #    new_x = self.xcor() - 10
    #    new_y = self.ycor() + 10
    #    self.goto(new_x, new_y)
#
    #def left_down(self):
    #    new_x = self.xcor() - 10
    #    new_y = self.ycor() - 10
    #    self.goto(new_x, new_y)