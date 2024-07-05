from turtle import Screen, Turtle
from Ball import Ball
from paddles import Paddle
from Scoreboard import Score
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.title("Ping-pong")
screen.bgcolor("black")
screen.tracer(0)

ycor = -275
for _ in range(29):
    net = Turtle("square")
    net.color("white")
    net.shapesize(stretch_wid=0.5, stretch_len=0.5)
    net.penup()
    net.goto(x=0, y=ycor)
    ycor += 20

paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))

screen.listen()
screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")
screen.onkey(paddle_left.up, "w")
screen.onkey(paddle_left.down, "s")

ball = Ball()
score = Score()

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(paddle_right) < 50 and ball.xcor() > 320) or (ball.distance(paddle_left) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() > 380:
        score.increase_left_score()
        ball.refresh()
    elif ball.xcor() < -380:
        score.increase_right_score()
        ball.refresh()


screen.exitonclick()

