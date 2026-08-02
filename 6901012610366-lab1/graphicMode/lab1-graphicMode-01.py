from processing import *

def setup():
    size(1000, 1000)

def draw_L(x, y, w, h):
    line(x, y, x, y - h)
    line(x, y, x + w, y)

def draw_I(x, y, w, h):
    line(x + (w/2), y, x + (w/2), y - h)

def draw_N(x, y, w, h):
    line(x, y, x, y - h)
    line(x, y - h, x + w, y)
    line(x + w, y, x + w, y - h)

def draw_E(x, y, w, h):
    line(x, y, x, y - h)
    line(x, y - h, x + w, y - h)
    line(x, y - (h / 2), x + w, y - (h / 2))
    line(x, y, x + w, y)


def draw():
    background(255)
    stroke(0)
    strokeWeight(3)
    
    w = 50
    h = 100
    gap = 20
    
    start_x = 100
    start_y = 200
    
    draw_L(start_x, start_y, w, h)
    
    start_x += w + gap
    draw_I(start_x, start_y, w, h)
    
    start_x += w + gap
    draw_N(start_x, start_y, w, h)
    
    start_x += w + gap
    draw_E(start_x, start_y, w, h)

run()