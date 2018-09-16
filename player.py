from turtle import Turtle, Screen
import bullet
class Player(Turtle):
    def __init__(self, wn):
        super().__init__()
        self.wn = wn
        self.t = Turtle()
        self.cannon = bullet.Bullet()

    def turn_right(self):
        self.right(10)

    def turn_left(self):
        self.left(10)
        
    def drive(self):
        self.forward(10)
    
    def reverse(self):
        self.backward(7)   
    
    def run(self):
        self.wn.onkey(self.turn_right, "Right")
        self.wn.onkey(self.turn_left, "Left")
        self.wn.onkey(self.drive, "Up")
        self.wn.onkey(self.reverse, "Down")
        self.wn.onkey(self.cannon.shoot, "space")
        self.wn.listen()
