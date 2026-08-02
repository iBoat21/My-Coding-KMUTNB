from processing import *

def setup():
  size(500,500)
  
def draw_circle(x,y,r):
  ellipse(x,y,r*2,r*2)
  
  
def draw_balloon(x,y,r):
  draw_circle(x,y,50)
  line(x,y+50,x,y+200)

def cal_distance(x1,x2,y1,y2):
  diffx = abs(x1-x2)
  diffy = abs(y1-y2)
  result = sqrt(diffx*diffx)+(diffy*diffy)
  return result
  
def draw():
  x = random(100,400)
  y = random(150,350)
  draw_circle(x,y,random(3,30))
  draw_balloon(x,200,50)
  d = cal_distance(x,200,mouseX,mouseY)
  # line(x,200,x,200+d)
  if mouseX > x:
    line(x,200,x,200+d)
  else:
    line(x,200,x,200+d)

run()