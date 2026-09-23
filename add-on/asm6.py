import random
print("\n" + "=" * 60)
print("ข้อ 6: สุ่มค่า 10 จำนวน 100-1000 แจ้งเตือนเมื่อค่ามากกว่า 800")
print("=" * 60)

# --------------------------------------------------
# ข้อ 6 - รูปแบบที่ 1: ไม่ใช้ฟังก์ชัน
# --------------------------------------------------
print("\n--- ข้อ 6 รูปแบบที่ 1: ไม่ใช้ฟังก์ชัน ---")
for i in range(10):
    val = random.randint(100, 1000)
    if val > 800:
        print(f"ค่าที่ {i+1}: {val} - แจ้งเตือน! ค่ามากกว่า 800")
    else:
        print(f"ค่าที่ {i+1}: {val} - ปกติ")

# --------------------------------------------------
# ข้อ 6 - รูปแบบที่ 2: ฟังก์ชันไม่มีพารามิเตอร์ ไม่คืนค่า
# --------------------------------------------------
print("\n--- ข้อ 6 รูปแบบที่ 2: ฟังก์ชันไม่มีพารามิเตอร์ ไม่คืนค่า ---")
def random_alert_no_param_no_return():
    for i in range(10):
        val = random.randint(100, 1000)
        if val > 800:
            print(f"ค่าที่ {i+1}: {val} - แจ้งเตือน! ค่ามากกว่า 800")
        else:
            print(f"ค่าที่ {i+1}: {val} - ปกติ")

random_alert_no_param_no_return()

# --------------------------------------------------
# ข้อ 6 - รูปแบบที่ 3: ฟังก์ชันมีพารามิเตอร์ ไม่คืนค่า
# --------------------------------------------------
print("\n--- ข้อ 6 รูปแบบที่ 3: ฟังก์ชันมีพารามิเตอร์ ไม่คืนค่า ---")
def random_alert_with_param_no_return(count, min_val, max_val, threshold):
    for i in range(count):
        val = random.randint(min_val, max_val)
        if val > threshold:
            print(f"ค่าที่ {i+1}: {val} - แจ้งเตือน! ค่ามากกว่า {threshold}")
        else:
            print(f"ค่าที่ {i+1}: {val} - ปกติ")

random_alert_with_param_no_return(10, 100, 1000, 800)

# --------------------------------------------------
# ข้อ 6 - รูปแบบที่ 4: ฟังก์ชันมีพารามิเตอร์ มีการคืนค่า
# --------------------------------------------------
print("\n--- ข้อ 6 รูปแบบที่ 4: ฟังก์ชันมีพารามิเตอร์ มีการคืนค่า ---")
def random_alert_with_param_with_return(count, min_val, max_val, threshold):
    results = []
    for i in range(count):
        val = random.randint(min_val, max_val)
        status = "แจ้งเตือน! ค่ามากกว่า " + str(threshold) if val > threshold else "ปกติ"
        results.append((val, status))
    return results

result6 = random_alert_with_param_with_return(10, 100, 1000, 800)
for i, (val, status) in enumerate(result6, 1):
    print(f"ค่าที่ {i}: {val} - {status}")