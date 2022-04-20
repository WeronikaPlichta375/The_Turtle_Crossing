from turtle import Turtle, Screen
from mturtle import MTurtle
from cars import Car
from level import Level
import time
screen = Screen()
NR_OF_CARS = 80
screen.screensize(600, 600)
screen.title("The Turtle Crossing Capstone")
screen.tracer(0)

gamer = MTurtle()
level = Level()


screen.listen()
screen.onkey(gamer.go_forward, "w")
screen.onkey(gamer.go_right, "d")
screen.onkey(gamer.go_left, "a")

list_car = []
for x in range(-1, NR_OF_CARS+1):
    list_car.append(Car())
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.3)
    for car in list_car:
        car.move()

    #Collisison
    for car in list_car:
        if gamer.distance(car) < 20:
            screen.clear()
            level.info_loss()
            screen.update()
            game_is_on = False
            break
    if gamer.ycor() > 295:

        for x in range(-1, len(list_car)):
            list_car[x].starting_position()
            #Increasing diffuclity by adjusting a speed and adding more cars
            list_car[x].adjust_speed()
            if x % 3 == 0:
                list_car.append(Car())

        if level.nr_level == 5:
            level.info_win()
            screen.update()
            game_is_on = False
            break

        level.level_up()
        gamer.goto(0, -300)
        screen.update()



screen.exitonclick()
