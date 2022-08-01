from turtle import Turtle

POSITIONS = [(440, 20), (440, 0), (440, -20), (440, -40)]


class Paddle:
    def __init__(self):
        self.segments = []
        self.create_paddle()

    def create_paddle(self):
        for segment in POSITIONS:
            paddle = Turtle(shape='square')
            paddle.hideturtle()
            paddle.color('white')
            paddle.penup()
            paddle.setpos(segment)
            paddle.showturtle()
            self.segments.append(segment)


