from turtle import Turtle, Screen
class Player(Turtle):
    def __init__(self, wn):
        self.wn = wn

    def turn_right(self):
        self.right(10)

    def turn_left(self):
        self.left(10)

    def run(self):
        self.wn.onkey(self.turn_right, "Right")
        self.wn.onkey(self.turn_left, "Left")
        self.wn.listen()
