from processing import *

def setup():
    createCanvas(1000, 1000)

def draw():
    #L
    line(100,100,100,0)
    line(100,100,150,100)
    #I
    line(200,100,200,0)
    #N
    line(250,100,250,0)
    line(250,0,300,100)
    line(300,100,300,0)
    #E
    line(350,100,350,0)
    line(350,0,400,0)
    line(350,50,400,50)
    line(350,100,400,100)


    # กำหนดตัวแปรหลักสำหรับตำแหน่งและขนาด
x = 100
y = 100
w = 50
h = 100
gap = 50

def setup():
    size(1000, 1000)

def draw():
    background(255) # เพิ่มพื้นหลังสีขาวเพื่อให้เห็นเส้นชัดเจน
    
    # --- ตัวอักษร L ---
    # คำนวณตำแหน่งเริ่มต้นของ L: x1 = x, y1 = y
    line(x, y, x, y - h)
    line(x, y, x + w, y)
    
    # --- ตัวอักษร I ---
    # คำนวณตำแหน่งเริ่มต้นของ I: x2 = x + w + gap
    x_i = x + w + gap
    line(x_i, y, x_i, y - h)
    
    # --- ตัวอักษร N ---
    # คำนวณตำแหน่งเริ่มต้นของ N: x3 = x_i + gap
    x_n = x_i + gap
    line(x_n, y, x_n, y - h)
    line(x_n, y - h, x_n + w, y)
    line(x_n + w, y, x_n + w, y - h)
    
    # --- ตัวอักษร E ---
    # คำนวณตำแหน่งเริ่มต้นของ E: x4 = x_n + w + gap
    x_e = x_n + w + gap
    line(x_e, y, x_e, y - h)
    line(x_e, y - h, x_e + w, y - h)
    line(x_e, y - (h / 2), x_e + w, y - (h / 2)) # ใช้ h/2 แทนค่าคงที่ 50
    line(x_e, y, x_e + w, y)

run()