from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.setposition(-280,250)
        self.write(f"Level: {self.score} ",False, align="left",font=("Courier",20, "normal"))


    def update(self):
        self.clear()
        self.write(f"Level: {self.score} ",False, align="left",font=("Courier",20, "normal"))


    def next_level(self):
        self.score += 1
        self.update()

    def game_over(self):
        self.setposition(0, 0)
        self.write(f"GAME OVER",False, align="center",font=("Courier",20, "normal"))

