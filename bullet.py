from turtle import Turtle
import time
class Bullet(Turtle):
    def __init__(self):
        super().__init__()
        self.t = Turtle()
    
    def shoot(size,lposy,lposx,hop):
        self.t = Turtle()
        self.t.tracer()
        self.t.up()
        self.t.move(lposy,lposx)
        self.t.color("white")
        self.t.down()
        self.t.start_fill()
        self.t.circle(size)
        self.t.stop_fill()
        self.t.up()
        self.t.forward(lposx)
        self.t.left(90)
        self.t.forward(lposy)
        self.t.right(90)
        self.t.forward(hop)
        self.t.down()
        self.t.start_fill()
        self.t.color("blue")
        self.t.circle(size)
        self.t.stop_fill()
        self.t.up()
        self.t.update()
