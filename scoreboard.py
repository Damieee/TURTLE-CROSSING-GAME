FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level=1
        self.update_score()
        
        
    def update_score(self):
        self.goto(-250,250)
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)
        

    def increase_score(self):
        self.level+=1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=("Arial", 24, "normal"))