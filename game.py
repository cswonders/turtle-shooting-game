import turtle
import time
import player

class Game():
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(1000, 1000)

    def run(self):
        s = turtle.Turtle()
        s.hideturtle()
        s.penup()
        s.goto(0, -120)
        s.write("The Amazing \n Turtle Game", align="center", font = ("Brush Script MT", 150, "bold"))
        time.sleep(1)
        for i in range(0, 101, 5):
            s.pencolor((i/100, i/100, i/100))
            s.write("The Amazing \n Turtle Game", align="center", font = ("Brush Script MT", 150, "bold"))
        s.clear()
        s.goto(0, 0)
        t1 = player.Player(self.screen)
        time.sleep(0.25)
        for i in range(0, 101, 4):
            s.pencolor((i/100, i/100, i/100))
            s.write("3", align="center", font = ("Brush Script MT", 150, "bold"))
        s.clear()
        time.sleep(0.25)
        for i in range(0, 101, 4):
            s.pencolor((i/100, i/100, i/100))
            s.write("2", align="center", font = ("Brush Script MT", 150, "bold"))
        s.clear()
        time.sleep(0.25)
        for i in range(0, 101, 4):
            s.pencolor((i/100, i/100, i/100))
            s.write("1", align="center", font = ("Brush Script MT", 150, "bold"))
        s.clear()
        time.sleep(0.25)
        for i in range(0, 101, 4):
            s.pencolor((i/100, i/100, i/100))
            s.write("GO", align="center", font = ("Brush Script MT", 150, "bold"))
        s.clear()
        s.hideturtle()
        print(s.isvisible())
        t1.run()
        
       
g = Game()
g.run()
