from turtle import Turtle
import time
class Bullet(Turtle):
    def __init__(self):
        super().__init__()
    
    def spawn(size,lposy,lposx,hop):
        self.tracer(0, 0)
        self.up()
        self.move(lposy,lposx)
        self.color("white")
        self.down()
        self.start_fill()
        self.circle(size)
        self.stop_fill()
        self.up()
        self.forward(lposx)
        self.left(90)
        self.forward(lposy)
        self.right(90)
        self.forward(hop)
        self.down()
        self.start_fill()
        self.color("blue")
        self.circle(size)
        self.stop_fill()
        self.up()
        self.update()
        return self.xcor(), self.ycor()
