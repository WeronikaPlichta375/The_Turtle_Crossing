from turtle import Turtle
from random import randrange, randint
colors=["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "wheat", "SlateGray", "SeaGreen", "blue", "green", "red", "violet"]
class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.color(colors[randint(0, len(colors))-1])
        self.starting_position()
        self.x_postion=310
        self.car_speed = 1

    def starting_position(self):
        self.goto(randrange(270, 2200, 30), randrange(-260, 270, 30))

    def move(self):
        
        new_x = self.xcor()-randint(3, 20)
        self.goto(new_x, self.ycor())

    def adjust_speed(self):
        if self.car_speed>8:
            pass
        else:
            self.car_speed+=2
            self.speed(self.car_speed)
        
