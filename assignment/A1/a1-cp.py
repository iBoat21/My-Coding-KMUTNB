import math
from processing import *

# --- ค่าคงที่ทางฟิสิกส์ ---
g = 9.8            # ความเร่งโน้มถ่วง (m/s^2)
theta_deg = 22.0   # มุมพื้นเอียง (องศา)
theta = theta_deg * math.pi / 180.0
sin_theta = math.sin(theta)
cos_theta = math.cos(theta)
dt = 0.035         # Time-step

racers = [ 
    {
        "name": "1. Solid Sphere (c = 0.4)",
        "c": 0.4,
        "color": (255, 100, 100),
        "s": 0.0,      # ระยะทางตามแนวพื้นเอียง (m)
        "v": 0.0,      # ความเร็วเชิงเส้น (m/s)
        "theta_rot": 0.0, # มุมการหมุน (rad)
        "rank": 0
    },
    {
        "name": "2. Solid Cylinder (c = 0.5)",
        "c": 0.5,
        "color": (100, 200, 255),
        "s": 0.0,
        "v": 0.0,
        "theta_rot": 0.0,
        "rank": 0
    },
    {
        "name": "3. Hollow Cylinder (c = 1.0)",
        "c": 1.0,
        "color": (120, 240, 150),
        "s": 0.0,
        "v": 0.0,
        "theta_rot": 0.0,
        "rank": 0
    }
]

# พารามิเตอร์สนามแข่ง (Visual)
start_x = 80
start_y = 70
ramp_length_m = 7.5    # ความยาวพื้นเอียง (เมตร)
visual_scale = 62.0    # 1 เมตร = 62 พิกเซล
radius_px = 16.0       # รัศมีแสดงผล (พิกเซล)
radius_m = radius_px / visual_scale

is_running = True
finish_count = 0

def to_str2(num):
    int_part = int(num)
    frac_part = int(abs(num - int_part) * 100)
    frac_str = str(frac_part)
    if len(frac_str) == 1:
        frac_str = "0" + frac_str
    return str(int_part) + "." + frac_str

def reset_race():
    global finish_count, is_running
    finish_count = 0
    is_running = True
    for r in racers:
        r["s"] = 0.0
        r["v"] = 0.0
        r["theta_rot"] = 0.0
        r["rank"] = 0

def setup():
    size(600, 420)

def draw():
    global finish_count, is_running
    background(25, 28, 36)

    # 1. ฟิสิกส์คำนวณ (Euler-Cromer)
    if is_running:
        all_finished = True
        for r in racers:
            if r["s"] < ramp_length_m:
                all_finished = False
                # a = (g * sin(theta)) / (1 + c)
                a = (g * sin_theta) / (1.0 + r["c"])
                r["v"] += a * dt
                ds = r["v"] * dt
                r["s"] += ds
                
                # กลิ้งโดยไม่ไถล: d(theta) = ds / R
                r["theta_rot"] += ds / radius_m
                
                # เช็คเข้าเส้นชัย
                if r["s"] >= ramp_length_m:
                    r["s"] = ramp_length_m
                    finish_count += 1
                    r["rank"] = finish_count
        
        if all_finished:
            is_running = False

    # 2. วาดพื้นเอียง (Ramp)
    end_x = start_x + (ramp_length_m * visual_scale * cos_theta)
    end_y = start_y + (ramp_length_m * visual_scale * sin_theta)
    
    # ทางลาด
    stroke(180)
    strokeWeight(3)
    line(start_x - 10, start_y + radius_px, end_x + 30, end_y + radius_px)
    
    # เส้นชัย (Finish Line)
    stroke(255, 60, 60)
    strokeWeight(2)
    line(end_x, end_y - 25, end_x, end_y + radius_px + 10)
    
    fill(255, 80, 80)
    textSize(11)
    text("FINISH", end_x - 15, end_y - 30)

    # 3. วาดวัตถุแต่ละชิ้นและการหมุน
    for idx, r in enumerate(racers):
        c_rgb = r["color"]
        fill(c_rgb[0], c_rgb[1], c_rgb[2])
        stroke(255)
        strokeWeight(1.5)
        
        # คำนวณพิกัดบนระนาบพื้นเอียง
        pos_along = r["s"] * visual_scale
        cx = start_x + (pos_along * cos_theta)
        cy = start_y + (pos_along * sin_theta)
        
        # วาดวงกลม
        ellipse(cx, cy, radius_px * 2, radius_px * 2)
        
        # วาดกากบาทด้านในเพื่อแสดงการหมุน (Rolling Animation)
        stroke(20)
        strokeWeight(2)
        ang = r["theta_rot"]
        dx1 = radius_px * math.cos(ang)
        dy1 = radius_px * math.sin(ang)
        dx2 = radius_px * math.cos(ang + math.pi / 2)
        dy2 = radius_px * math.sin(ang + math.pi / 2)
        line(cx - dx1, cy - dy1, cx + dx1, cy + dy1)
        line(cx - dx2, cy - dy2, cx + dx2, cy + dy2)

        # อันดับเมื่อเข้าเส้นชัย
        if r["rank"] > 0:
            fill(255, 230, 80)
            textSize(12)
            text("Rank " + str(r["rank"]), cx - 18, cy - 22)

    # 4. HUD และตารางข้อมูล
    draw_hud()

def draw_hud():
    # กรอบแสดงค่าตัวเลข
    fill(18, 20, 26)
    stroke(60)
    strokeWeight(1)
    rectMode(CORNER)
    rect(30, 250, 540, 150)

    fill(255)
    textSize(13)
    text("Rotational Inertia Race (Rolling without Slipping)", 45, 272)
    
    textSize(11)
    fill(170)
    text("Formula: a = (g * sin) / (1 + c)  |  Incline angle = 22 deg", 45, 292)

    # แสดงสถิติของแต่ละลูก
    for i, r in enumerate(racers):
        c_rgb = r["color"]
        fill(c_rgb[0], c_rgb[1], c_rgb[2])
        row_y = 318 + (i * 24)
        
        status = "v = " + to_str2(r["v"]) + " m/s"
        if r["rank"] > 0:
            status += " (FINISHED #" + str(r["rank"]) + ")"
        
        text(r["name"] + " -> " + status, 45, row_y)

    fill(200, 200, 100)
    # text("Press [SPACE] or [R] to Restart Race", 320, 272)

def keyPressed():
    try:
        if key == " " or key == "r" or key == "R" or keyCode == 32:
            reset_race()
    except:
        pass

run()