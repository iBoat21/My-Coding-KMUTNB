import random

print("=" * 60)
print("ข้อ 1: สร้างอาร์เรย์ 20 จำนวน สุ่มค่า 10-99")
print("=" * 60)

# --------------------------------------------------
# ข้อ 1 - รูปแบบที่ 1: ไม่ใช้ฟังก์ชัน
# --------------------------------------------------
print("\n--- ข้อ 1 รูปแบบที่ 1: ไม่ใช้ฟังก์ชัน ---")
arr1 = []
for i in range(20):
    num = random.randint(10, 99)
    arr1.append(num)
print("อาร์เรย์ 20 จำนวน:", arr1)

# --------------------------------------------------
# ข้อ 1 - รูปแบบที่ 2: ฟังก์ชันไม่มีพารามิเตอร์ ไม่คืนค่า
# --------------------------------------------------
print("\n--- ข้อ 1 รูปแบบที่ 2: ฟังก์ชันไม่มีพารามิเตอร์ ไม่คืนค่า ---")
def generate_random_array_no_param_no_return():
    arr = []
    for i in range(20):
        num = random.randint(10, 99)
        arr.append(num)
    print("อาร์เรย์ 20 จำนวน:", arr)

generate_random_array_no_param_no_return()

# --------------------------------------------------
# ข้อ 1 - รูปแบบที่ 3: ฟังก์ชันมีพารามิเตอร์ ไม่คืนค่า
# --------------------------------------------------
print("\n--- ข้อ 1 รูปแบบที่ 3: ฟังก์ชันมีพารามิเตอร์ ไม่คืนค่า ---")
def generate_random_array_with_param_no_return(count, min_val, max_val):
    arr = []
    for i in range(count):
        num = random.randint(min_val, max_val)
        arr.append(num)
    print(f"อาร์เรย์ {count} จำนวน (ค่า {min_val}-{max_val}):", arr)

generate_random_array_with_param_no_return(20, 10, 99)

# --------------------------------------------------
# ข้อ 1 - รูปแบบที่ 4: ฟังก์ชันมีพารามิเตอร์ มีการคืนค่า
# --------------------------------------------------
print("\n--- ข้อ 1 รูปแบบที่ 4: ฟังก์ชันมีพารามิเตอร์ มีการคืนค่า ---")
def generate_random_array_with_param_with_return(count, min_val, max_val):
    arr = []
    for i in range(count):
        num = random.randint(min_val, max_val)
        arr.append(num)
    return arr

result1 = generate_random_array_with_param_with_return(20, 10, 99)
print("อาร์เรย์ 20 จำนวน:", result1)
