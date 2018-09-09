import turtle.Turtle
class Player(Turtle)
    def __init__(self, wn):
        self.wn = wn

    def turn_right():
        self.right(10)

    def turn_left():
        self.left(10)

    self.wn.onkey(turn_right, "Right")
    self.wn.onkey(turn_left, "Left")
    self.wn.listen()