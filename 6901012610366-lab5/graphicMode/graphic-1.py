from processing import *

x = [100, 400, 200, 450, 300]
y = [50, 30, 10, 70, 20]

def setup():
    size(500, 500)
    
def draw():
    background(240)
    
    fill(0, 150, 255)
    
    i = 0
    while i < len(x):
        ellipse(x[i], y[i], 20, 20)
        
        y[i] = y[i] + 2
        
        if y[i] > 500:
            y[i] = 0
            
        i = i + 1

run()