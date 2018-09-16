from turtle import Turtle
import time
class bullet(Turtle):
    def shoot(size,lposy,lposx,hop):
        t = Turtle()
        t.tracer()
        t.up()
        t.move(lposy,lposx)
        t.color("white")
        t.down()
        t.start_fill()
        t.circle(size)
        t.stop_fill()
        t.up()
        t.forward(lposx)
        t.left(90)
        t.forward(lposy)
        t.right(90)
        t.forward(hop)
        t.down()
        t.start_fill()
        t.color("blue")
        t.circle(size)
        t.stop_fill()
        t.up()
        t.update()
