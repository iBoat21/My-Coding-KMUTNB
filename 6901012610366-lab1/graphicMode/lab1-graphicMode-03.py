from processing import *
import random 

def setup():
    size(400, 400)
    background(0) 

def draw():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    x = random.randint(0, 400)
    y = random.randint(0, 400)
  
    size_circle = random.randint(10, 120)
  
    fill(r, g, b)
    stroke(255) 
    strokeWeight(1)
    
    ellipse(x, y, size_circle, size_circle)

run()