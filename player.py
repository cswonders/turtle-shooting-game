from turtle import Turtle, Screen
import bullet
class Player(Turtle):
    def __init__(self, wn, x, y):
        super().__init__()
        self.wn = wn
        self.t = Turtle()
        self.cannon = bullet.Bullet()
        self.x = x
        self.y = y
        self.penup()
        self.goto(self.x, self.y)

    def turn_right(self):
        self.right(10)

    def turn_left(self):
        self.left(10)
        
    def drive(self):
        self.forward(10)
        self.x = self.xcor()
        self.y = self.ycor()
        if self.x >= 500:
            self.x = -490
        if self.y >= 500:
            self.y = -490
        elif self.y <= -500:
            self.y = 490
        self.goto(self.x, self.y)
        print(str(self.x) + ', ' + str(self.y))
    
    def reverse(self):
        self.backward(7)
        self.x = self.xcor()
        self.y = self.ycor()
        if self.x <= -500:
            self.x = 490
        if self.y <= -500:
            self.y = 490
        elif self.y >= 490:
            self.y = -490
        self.goto(self.x, self.y)
    
    def run(self):
        self.wn.onkey(self.turn_right, "Right")
        self.wn.onkey(self.turn_left, "Left")
        self.wn.onkey(self.drive, "Up")
        self.wn.onkey(self.reverse, "Down")
        self.wn.onkey(self.cannon.spawn, "space")
        self.wn.listen()
