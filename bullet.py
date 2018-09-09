from turtle import Turtle
import time
class bullet(Turtle):
    def prep(sx,sy,speed,d,bsize):
        t = Turtle()
        t.tracer(0,0)
        t.forward(0 + sx)
        t.left(90)
        t.forward(0 + sy)
        t.ht()
        if d == "left":
            t.left(90)
        else:
            t.right(90)
    def shoot():  
        time.sleep(float(speed/10000))
        t.color((255,255,255))
        t.begin_fill()
        t.circle(bsize)
        t.end_fill()
            t.forward(speed)
            t.color("green")
            t.begin_fill()
            t.circle(bsize)
            t.end_fill()
            t.update()
bullet.shoot(0,0,5,"left",5)
