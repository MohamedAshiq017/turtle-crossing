from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=0
        self.penup()
        self.hideturtle()
        self.goto(-280,250)
        self.write(arg=f"Level:{self.level}",align='left',font=FONT)
        


    def update_score(self):
        self.clear()
        self.level+=1
        self.write(arg=f"Level:{self.level}",align='left',font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER",align='center',font=FONT)


