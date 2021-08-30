from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_add = 10
        self.y_add = 10

    def move(self):
        self.goto(self.xcor() + self.x_add, self.ycor() + self.y_add)

    def bounce_x(self):
        self.x_add *= -1

    def bounce_y(self):
        self.y_add *= -1

    def update_when_right_misses(self):
        self.goto(0, 0)
        self.x_add = -10
        self.y_add = -10

    def update_when_left_misses(self):
        self.goto(0, 0)
        self.x_add = 10
        self.y_add = 10
