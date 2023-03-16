from turtle import Turtle



class Net(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.pu()
        self.shapesize(stretch_wid=2, stretch_len=0.5)
        self.goto(position)


