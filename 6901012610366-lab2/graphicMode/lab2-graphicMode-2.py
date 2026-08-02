from processing import *

def setup():
    size(600, 400)
    background(255)
    noLoop()

def trapezoid():
    line(200, 150, 400, 150)
    line(400, 150, 480, 280)
    line(480, 280, 120, 280)
    line(120, 280, 200, 150)

def draw():
    trapezoid()

run()