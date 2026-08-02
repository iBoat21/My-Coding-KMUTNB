from processing import *

x = 100
y = 100
w = 50
h = 100
gap = 50

def setup():
  size(1000,1000)
  
def lineL():
  line(x,y,x,y-h)
  line(x,y,x+w, y)
  
def lineI():
  x_i = x + w + gap
  line(x_i, y, x_i, y - h)
  
def lineN():
  x_n = x+w+gap+gap
  line(x_n, y, x_n, y - h)
  line(x_n, y - h, x_n + w, y)
  line(x_n + w, y, x_n + w, y - h)
  
def lineE():
  x_e = x+w+gap+gap+gap+gap
  line(x_e, y, x_e, y - h)
  line(x_e, y - h, x_e + w, y - h)
  line(x_e, y - (h / 2), x_e + w, y - (h / 2))
  line(x_e, y, x_e + w, y)
  

def draw():
  background(255)
  lineL()
  lineI()
  lineN()
  lineE()
  
run()
  