from processing import *

def setup():
    size(500, 500)

def draw_rain_drops_util(volume):
  sum = 0
  while(sum < volume):
    x = random(50,400)
    y = random(100,350)
    r = random(3,30)
    ellipse(x,y,r*2,r*2)
    sum = sum + r

def draw():
    background(254)
    draw_rain_drops_util(10)

run()