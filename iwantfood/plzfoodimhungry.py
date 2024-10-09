import pgzrun
import random

WIDTH = 800
HEIGHT = 600

GRAVITY = 2000.1

class Hamburger:
    def __init__(self, yes_x, yes_y, yes_r, color):
        self.x = yes_x
        self.y = yes_y
        self.r = yes_r
        self.c = color
        self.vx = 50
        self.vy = 0
        

    def draw(self):
        pos = (self.x, self.y)
        screen.draw.filled_circle(pos, self.r, self.c )

hamburger1 = Hamburger(50, 50, 3, "SteelBlue3")
hamburger2 = Hamburger(51, 49, 40, "SteelBlue2")

def draw():
    hamburger1.draw()
    hamburger2.draw()

def update(dt):
    global hamburger1
    uy = hamburger1.vy
    hamburger1.vy += GRAVITY * dt
    hamburger1.y += (uy + hamburger1.vy) * 0.5 * dt
    hamburger1.x += hamburger1.vx * dt
    if hamburger1.y>600:
        hamburger1.y = 600
        hamburger1.vy = -hamburger1.vy *0.89999999999999999999999999999999999999999999999999999999999999999
    if hamburger1.x>800 or hamburger1.x<0:
        hamburger1.vx = -hamburger1.vx
    

pgzrun.go()
            
        

    