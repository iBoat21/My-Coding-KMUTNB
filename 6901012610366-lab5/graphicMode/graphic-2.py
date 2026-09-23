from processing import *

def setup():
    size(500, 500)
    rectMode(CENTER)
    noStroke()

def draw_positive(x, y, base_size):
    d = dist(mouseX, mouseY, x, y)
    
    max_dist = 150.0
    factor = constrain(d / max_dist, 0.2, 1.0)
    
    s = base_size * factor
    
    fill(50, 150, 255)
    rect(x, y, s, s / 3)     
    rect(x, y, s / 3, s)     

def draw():
    background(30)
    
    num_items = 5
    base_size = 60
    y = height / 2
    
    for i in range(num_items):
        x = (i + 0.5) * (width / num_items)
        draw_positive(x, y, base_size)

run()