import math
from processing import *

x, y = 50.0, 360.0
vx, vy = 0.0, 0.0
g = 0.3
path = []

def setup():
    size(800, 400)
    reset_simulation(55, 12)  
    
def draw():
    global x, y, vx, vy, g, path
    
    background(245, 245, 245)
    
    fill(100, 180, 100)
    noStroke()
    rect(0, 360, 800, 40)
    
    x += vx
    y += vy
    vy += g
    path.append((x, y))
    
    if y >= 360:
        reset_simulation(55, 12)
            
    stroke(70, 130, 240)
    strokeWeight(2)
    for i in range(len(path) - 1):
        line(path[i][0], path[i][1], path[i+1][0], path[i+1][1])
        
    fill(235, 80, 80)
    noStroke()
    ellipse(x, y, 20, 20)

def reset_simulation(angle_deg, speed):
    global x, y, vx, vy, path
    x, y = 50.0, 360.0
    rad = math.radians(angle_deg)
    vx = speed * math.cos(rad)
    vy = -speed * math.sin(rad)
    path = [(x, y)]
    
run()