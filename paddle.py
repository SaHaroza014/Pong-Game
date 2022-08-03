from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, positions):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('white')
        self.turtlesize(stretch_wid=6, stretch_len=2)
        self.goto(positions)

    def move_up(self):
        y = self.ycor()
        y += 20
        self.sety(y)

    def move_down(self):
        y = self.ycor()
        y -= 20
        self.sety(y)
