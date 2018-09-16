from turtle import Turtle
import time
class Bullet(Turtle):
    def __init__(self, wn, xi, yi, speed):
        super().__init__()
        self.ht()
        self.wn = wn
        self.goto(xi, yi)
        self.st()
        self.speed = speed
       
    def run()
        self.forward(self.speed)
        self.wn.ontimer(self.main, 5)
    
