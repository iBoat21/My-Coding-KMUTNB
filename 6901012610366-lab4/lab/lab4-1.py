from processing import *

def setup():
  size(500,500)
  
def plusShape(cx,cy,s):
  rectMode(CENTER)
  rect(cx,cy,s,s)
  rect(cx,cy-s,s,s)
  rect(cx-s,cy,s,s)
  rect(cx+s,cy,s,s)
  rect(cx,cy+s,s,s)
  
def loopPlusShape(n):
  i=0
  while i<n:
    x = 70 + (i*90)
    y = 250
    plusShape(x,y,20)
    i=i+1

def draw():
  background(254)
  loopPlusShape(5)
  
  
run()