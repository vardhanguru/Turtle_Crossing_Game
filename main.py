import time
from player import Player
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor("white")
screen.tracer(0)
player=Player()
score=Scoreboard()
car=CarManager()

screen.listen()
screen.onkey(player.up,"Up")
screen.onkey(player.down,"Down")
game_is_on = True
p=10
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.generate(0.5)
    car.move(10)
    for i in car.lists:
        if player.distance(i.xcor()-p,i.ycor())<20:
            print("xollkod")
            game_is_on=False
    if player.ycor()>320:
        score.score+=1
        score.update()
        player.goto(0,-320)
        car.levelup()
        p=0
        


screen.exitonclick()