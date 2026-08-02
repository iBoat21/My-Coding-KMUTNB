from processing import *

def setup():
    size(500, 500)

def draw_rain_drops_util_r_below(value):
  r_flag = True
  while(r_flag):
    x = random(100,400)
    y = random(150,350)
    r = random(3,30)
    ellipse(x,y,r*2,r*2)
    if (r < value):
      r_flag = False

def draw():
    background(254)
    draw_rain_drops_util_r_below(5)

run()