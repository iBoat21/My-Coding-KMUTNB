from processing import *

def setup():
    size(500, 500)
    noStroke() 
    fill(100, 200, 255)

def draw_square(x, y, z):
    rectMode(CENTER) 
    rect(x, y, z, z)

def draw_positive(offsetX, offsetY):
    box_size = 60 
    draw_square(offsetX, offsetY, box_size)            
    draw_square(offsetX - box_size, offsetY, box_size)
    draw_square(offsetX + box_size, offsetY, box_size)
    draw_square(offsetX, offsetY - box_size, box_size)
    draw_square(offsetX, offsetY + box_size, box_size)

def draw():
    background(255)
    draw_positive(mouseX, mouseY)

run()