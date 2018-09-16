from turtle import Turtle, Screen
class Player(Turtle):
    def __init__(self, wn):
        super().__init__()
        self.wn = wn
        self.t = Turtle()

    def turn_right(self):
        self.right(10)
        print('Left')

    def turn_left(self):
        self.left(10)
        print('Right')

    def run(self):
        self.wn.onkey(self.turn_right, "Right")
        self.wn.onkey(self.turn_left, "Left")
        self.wn.listen()
