from turtle import Turtle, Screen
import bullet
class Player(Turtle):
    def __init__(self, wn, bl, x, y, right, left, up, down, shoot):
        super().__init__()
        self.wn = wn
        self.x = x
        self.y = y
        self.penup()
        self.goto(self.x, self.y)
        self.rightk = right
        self.leftk = left
        self.upk = up
        self.downk = down
        self.shootk = shoot

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
    
    def shoot():
        bl.append(bullet.Bullet(self.wn, self.xcor, self.ycor, 15))
    
    def run(self):
        self.wn.onkey(self.turn_right, self.rightk)
        self.wn.onkey(self.turn_left, self.leftk)
        self.wn.onkey(self.drive, self.upk)
        self.wn.onkey(self.reverse, self.downk)
        self.wn.onkey(self.shoot, self.shootk)
        self.wn.listen()
        #self.wn.ontimer(self.run, 5)
