import random
print("\n" + "=" * 60)
print("ข้อ 3: สร้างจำนวน 10 จำนวน p(x,y) = x^y")
print("=" * 60)
# --------------------------------------------------
# ข้อ 3 - รูปแบบที่ 1: ไม่ใช้ฟังก์ชัน
# --------------------------------------------------
print("\n--- ข้อ 3 รูปแบบที่ 1: ไม่ใช้ฟังก์ชัน ---")
results3 = []
for i in range(10):
    x = random.randint(1, 100)
    y = random.randint(0, 5)
    p = x ** y
    results3.append((x, y, p))
    print(f"p({x}, {y}) = {p}")

# --------------------------------------------------
# ข้อ 3 - รูปแบบที่ 2: ฟังก์ชันไม่มีพารามิเตอร์ ไม่คืนค่า
# --------------------------------------------------
print("\n--- ข้อ 3 รูปแบบที่ 2: ฟังก์ชันไม่มีพารามิเตอร์ ไม่คืนค่า ---")
def power_xy_no_param_no_return():
    for i in range(10):
        x = random.randint(1, 100)
        y = random.randint(0, 5)
        p = x ** y
        print(f"p({x}, {y}) = {p}")

power_xy_no_param_no_return()

# --------------------------------------------------
# ข้อ 3 - รูปแบบที่ 3: ฟังก์ชันมีพารามิเตอร์ ไม่คืนค่า
# --------------------------------------------------
print("\n--- ข้อ 3 รูปแบบที่ 3: ฟังก์ชันมีพารามิเตอร์ ไม่คืนค่า ---")
def power_xy_with_param_no_return(count, x_min, x_max, y_min, y_max):
    for i in range(count):
        x = random.randint(x_min, x_max)
        y = random.randint(y_min, y_max)
        p = x ** y
        print(f"p({x}, {y}) = {p}")

power_xy_with_param_no_return(10, 1, 100, 0, 5)

# --------------------------------------------------
# ข้อ 3 - รูปแบบที่ 4: ฟังก์ชันมีพารามิเตอร์ มีการคืนค่า
# --------------------------------------------------
print("\n--- ข้อ 3 รูปแบบที่ 4: ฟังก์ชันมีพารามิเตอร์ มีการคืนค่า ---")
def power_xy_with_param_with_return(x, y):
    return x ** y

for i in range(10):
    x = random.randint(1, 100)
    y = random.randint(0, 5)
    p = power_xy_with_param_with_return(x, y)
    print(f"p({x}, {y}) = {p}")