from processing import *

def setup():
    size(500, 500)

def draw_raindrop(n):
    i = 0
    while(i < n):
        x = random(100, 400)
        y = random(150, 350)
        r = random(3, 30)
        ellipse(x, y, r * 2, r * 2)
        i = i + 1

def draw():
    background(254)
    draw_raindrop(10)

run()