from processing import *

x1, x2, x3 = 100, 250, 400
r = 40

y1, y2, y3 = 250, 250, 250
speed1 = 5
speed2 = 3
speed3 = 7

def setup():
    size(500, 500)
    noStroke()

def draw():
    background(30)

    global y1, y2, y3, speed1, speed2, speed3

    seconds = millis() / 1000

    if seconds >= 0:
        y1 += speed1  
        if y1 > height - r / 2 or y1 < r / 2: 
            speed1 = -speed1  
        fill(255, 100, 100) 
        ellipse(x1, y1, r, r)

    if seconds >= 2:
        y2 += speed2
        if y2 > height - r / 2 or y2 < r / 2:
            speed2 = -speed2
        fill(100, 255, 100) 
        ellipse(x2, y2, r, r)

    if seconds >= 4:
        y3 += speed3
        if y3 > height - r / 2 or y3 < r / 2:
            speed3 = -speed3
        fill(100, 100, 255) 
        ellipse(x3, y3, r, r)
        
run()