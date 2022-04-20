from turtle import Turtle

class MTurtle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(0, -300)
        self.left(90)
        self.speed = 10

    def go_forward(self):
        self.forward(10)

    def go_right(self):
        self.right(90)

    def go_left(self):
        self.left(90)
