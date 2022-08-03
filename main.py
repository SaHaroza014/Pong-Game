from turtle import Turtle, Screen
from paddle import Paddle
from play_ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.title("Pong Game")
screen.setup(height=600, width=1000)
screen.tracer(0)
screen.bgcolor('black')

right_paddle = Paddle((440, 0))
left_paddle = Paddle((-440, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkeypress(right_paddle.move_up, 'Up')
screen.onkeypress(right_paddle.move_down, 'Down')
screen.onkeypress(left_paddle.move_up, 'w')
screen.onkeypress(left_paddle.move_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_spd)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 330 or ball.distance(left_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    if ball.xcor() > 480:
        score.l_point()
        score.update()
        ball.reset()

    if ball.xcor() < -480:
        score.r_point()
        score.update()
        ball.reset()

screen.exitonclick()
