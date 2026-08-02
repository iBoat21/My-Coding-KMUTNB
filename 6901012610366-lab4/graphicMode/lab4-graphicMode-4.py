from processing import *

def setup():
  size(500,500)

x= 100
y= 100
s= 300

def draw_ladder(x,y,s):
  line(x, y, x, y+s) #ตำแหน่งข้างบันไดซ้าย
  line(x+s, y, x+s, y+s) #ตำแหน่งข้างบันไดขวา
  while y < 350: #วาดซี่บันไดที่มีระยะห่างคงที่
    y = y + 50
    line(x,y,x+s,y)

def draw():
  draw_ladder(x,y,s)


run()