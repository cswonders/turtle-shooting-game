from turtle import Turtle
import time
class Bullet(Turtle):
    def __init__(self, wn, xi, yi, speed, direction):
        super().__init__()
        self.ht()
        self.wn = wn
        self.goto(xi, yi)
        self.st()
        self.speed = speed
        self.setheading(direction)
       
    def run():
        self.forward(self.speed)
        self.wn.ontimer(self.main, 5)
    
