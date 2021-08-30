import time
from scoreboard import Score
from ball import Ball
from turtle import Screen
from paddle import Paddle

screen = Screen()

screen.tracer(0)
screen.title("PONG")
screen.setup(width=1000, height=800)
screen.bgcolor("black")
r_paddle = Paddle((470, 0))
l_paddle = Paddle((-480, 0))
r_score = Score((100, 300))
l_score = Score((-100, 300))
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

is_on = True
speed_factor = 1
ball = Ball()
while is_on:
    screen.update()
    r_score.score_display()
    l_score.score_display()
    time.sleep(0.05/speed_factor)
    ball.move()
    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 440:
        r_score.score_update()
        ball.bounce_x()
        speed_factor += 1
    if ball.distance(l_paddle) < 50 and ball.xcor() < -440:
        ball.bounce_x()
        speed_factor += 1
        l_score.score_update()
    if ball.xcor() > 480:
        ball.update_when_right_misses()
        speed_factor = 1
    if ball.xcor() < -480:
        ball.update_when_left_misses()
        speed_factor = 1

screen.exitonclick()
