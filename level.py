from turtle import Turtle

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.nr_level=1
        self.update()
        
    def update(self):
        self.clear()
        self.goto(-290, 270)
        self.write(f"Level {self.nr_level}", align="center", font=("Courier", 25, "normal"))
    
    def level_up(self):
        self.nr_level+=1
        self.update()
        print("Level up")
        
    def info_win(self):
        self.goto(0, 0)
        self.write(f"Congratulations! You won!", align="center", font=("Courier", 35, "normal"))

    def info_loss(self):
        self.goto(0, 0)
        self.write(f";c You lost!", align="center", font=("Courier", 35, "normal"))