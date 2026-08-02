def setup():
  size(500,500)

def draw_vertical_lines(x1, y1, x2, y2):
  space = abs(x1-x2)/5 
  while (x1 < x2): 
    line(x1,y1 - 50, x1, y1 + 50)
    x1 = x1 + space
  
def draw():
  x2 = random.randint(0,500) 
  y1 = random.randint(0,500) 
  x1 = random.randint(0,x2) 
  y2 = random.randint(0,500)
  print("x1=",x1),("y1=",y1),("x2=",x2),("y2=",y2)
  background(255)
  draw_vertical_lines(x1, y1, x2, y2)
  time.sleep(0.25)

run()