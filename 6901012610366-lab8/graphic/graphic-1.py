from processing import *

class Balloon:
    def __init__(self, x, y, w, h, speed, r, g, b):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = speed
        self.color = (r, g, b)

    def update(self):
        self.y -= self.speed
        if self.y < -self.h:
            self.y = height + self.h

    def show(self):
        self.update()
        
        stroke(120)
        strokeWeight(1.5)
        line(self.x, self.y + self.h / 2, self.x, self.y + self.h / 2 + 40)
        
        noStroke()
        fill(self.color[0], self.color[1], self.color[2])
        ellipse(self.x, self.y, self.w, self.h)
        
        triangle(self.x - 4, self.y + self.h / 2 + 4,
                 self.x + 4, self.y + self.h / 2 + 4,
                 self.x, self.y + self.h / 2)

balloons = [
    Balloon(80, 500, 40, 50, 1.5, 255, 100, 100),
    Balloon(160, 550, 50, 65, 2.0, 100, 200, 255),
    Balloon(240, 480, 45, 55, 1.2, 150, 255, 150),
    Balloon(320, 520, 55, 70, 2.5, 255, 220, 100),
    Balloon(400, 560, 42, 52, 1.8, 220, 150, 255)
]

def setup():
    size(500, 600)

def draw():
    background(240, 248, 255)
    for b in balloons:
        b.show()