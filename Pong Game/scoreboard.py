from turtle import Turtle


class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(position)
        self.hideturtle()
        self.color("white")

    def score_display(self):
        self.write(self.score, align="center", font=("Arial", 50, "normal"))

    def score_update(self):
        self.score += 1
        self.clear()
