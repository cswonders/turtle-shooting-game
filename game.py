import turtle
import time
import player

class Game():
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(1000, 1000)
        bullet_list[]
        s = turtle.Turtle()
        s.ht()
        s.penup()
        s.goto(0, -120)
        s.write("The Amazing \n Turtle Game", align="center", font = ("Brush Script MT", 150, "bold"))
        time.sleep(1)
        for i in range(0, 101, 5):
            s.pencolor((i/100, i/100, i/100))
            s.write("The Amazing \n Turtle Game", align="center", font = ("Brush Script MT", 150, "bold"))
        s.reset()
        s.ht()
        t1 = player.Player(self.screen, bullet_list, -250, 0, 'd', 'a', 'w', 's', 'q')
        t2 = player.Player(self.screen, bullet_list, 250, 0, 'Right', 'Left', 'Up', 'Down', 'space')
        time.sleep(0.25)
        for i in range(0, 101, 4):
            s.pencolor((i/100, i/100, i/100))
            s.write("3", align="center", font = ("Brush Script MT", 150, "bold"))
        s.reset()
        s.ht()
        time.sleep(0.25)
        for i in range(0, 101, 4):
            s.pencolor((i/100, i/100, i/100))
            s.write("2", align="center", font = ("Brush Script MT", 150, "bold"))
        s.reset()
        s.ht()
        time.sleep(0.25)
        for i in range(0, 101, 4):
            s.pencolor((i/100, i/100, i/100))
            s.write("1", align="center", font = ("Brush Script MT", 150, "bold"))
        s.reset()
        s.ht()
        time.sleep(0.25)
        for i in range(0, 101, 4):
            s.pencolor((i/100, i/100, i/100))
            s.write("GO", align="center", font = ("Brush Script MT", 150, "bold"))
        s.reset()
        s.ht()

    def run(self):
        t1.run()
        t2.run()
        for i in bullet_list:
            i.run()
   
g = Game()
g.screen.ontimer(g.run, 5)
