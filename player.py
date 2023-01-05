STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.tilt(90)
        self.penup()
        self.go_to_start()

    def move(self):
        new_ycor=self.ycor() + MOVE_DISTANCE
        new_xcor=self.xcor()
        self.goto(new_xcor, new_ycor)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def reach_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False