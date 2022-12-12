from turtle import Turtle
import random
LISTS=[-200,-150,-100,-50,0,50,100,150,200]
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
X_COR=300
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.shapesize(1,2,1)
        self.speeds=STARTING_MOVE_DISTANCE
        self.penup()
        self.x=10
        self.y=10
        self.lists=[]

    def generate(self,speed):
            if random.randint(1,6)==3:
                ob=CarManager()
                ob.showturtle()
                ob.color(random.choice(COLORS))
                ob.speed("slowest")
                ob.goto(X_COR,random.randint(-250,250))
                self.lists.append(ob)

    def move(self,x):
        for i in self.lists:
            i.backward(self.speeds)

    def levelup(self):
        self.speeds+=10




