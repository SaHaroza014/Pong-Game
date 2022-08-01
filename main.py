from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.title("Pong Game")
screen.setup(height=600, width=1000)
screen.bgcolor('black')

paddle = Paddle()

screen.listen()





screen.exitonclick()