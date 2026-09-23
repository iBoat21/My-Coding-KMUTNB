print("\n" + "=" * 60)
print("ข้อ 7: หาค่ามัธยฐาน 3 จำนวน / 5 จำนวน / n จำนวน")
print("=" * 60)

# --------------------------------------------------
# ข้อ 7 - รูปแบบที่ 1: ไม่ใช้ฟังก์ชัน
# --------------------------------------------------
print("\n--- ข้อ 7 รูปแบบที่ 1: ไม่ใช้ฟังก์ชัน ---")
# 3 จำนวน
nums3 = [15, 42, 23]
sorted3 = sorted(nums3)
median3 = sorted3[len(sorted3) // 2]
print(f"ชุดข้อมูล 3 จำนวน {nums3} -> มัธยฐาน = {median3}")

# 5 จำนวน
nums5 = [10, 50, 30, 20, 40]
sorted5 = sorted(nums5)
median5 = sorted5[len(sorted5) // 2]
print(f"ชุดข้อมูล 5 จำนวน {nums5} -> มัธยฐาน = {median5}")

# n จำนวน
numsn = [5, 2, 8, 1, 9, 3, 7]
sortedn = sorted(numsn)
mediann = sortedn[len(sortedn) // 2]
print(f"ชุดข้อมูล n จำนวน {numsn} -> มัธยฐาน = {mediann}")

# --------------------------------------------------
# ข้อ 7 - รูปแบบที่ 2: ฟังก์ชันไม่มีพารามิเตอร์ ไม่คืนค่า
# --------------------------------------------------
print("\n--- ข้อ 7 รูปแบบที่ 2: ฟังก์ชันไม่มีพารามิเตอร์ ไม่คืนค่า ---")
def find_median_no_param_no_return():
    nums3 = [15, 42, 23]
    sorted3 = sorted(nums3)
    median3 = sorted3[len(sorted3) // 2]
    print(f"ชุดข้อมูล 3 จำนวน {nums3} -> มัธยฐาน = {median3}")

    nums5 = [10, 50, 30, 20, 40]
    sorted5 = sorted(nums5)
    median5 = sorted5[len(sorted5) // 2]
    print(f"ชุดข้อมูล 5 จำนวน {nums5} -> มัธยฐาน = {median5}")

    numsn = [5, 2, 8, 1, 9, 3, 7]
    sortedn = sorted(numsn)
    mediann = sortedn[len(sortedn) // 2]
    print(f"ชุดข้อมูล n จำนวน {numsn} -> มัธยฐาน = {mediann}")

find_median_no_param_no_return()

# --------------------------------------------------
# ข้อ 7 - รูปแบบที่ 3: ฟังก์ชันมีพารามิเตอร์ ไม่คืนค่า
# --------------------------------------------------
print("\n--- ข้อ 7 รูปแบบที่ 3: ฟังก์ชันมีพารามิเตอร์ ไม่คืนค่า ---")
def find_median_with_param_no_return(data):
    sorted_data = sorted(data)
    median = sorted_data[len(sorted_data) // 2]
    print(f"ชุดข้อมูล {data} -> มัธยฐาน = {median}")

find_median_with_param_no_return([15, 42, 23])
find_median_with_param_no_return([10, 50, 30, 20, 40])
find_median_with_param_no_return([5, 2, 8, 1, 9, 3, 7])

# --------------------------------------------------
# ข้อ 7 - รูปแบบที่ 4: ฟังก์ชันมีพารามิเตอร์ มีการคืนค่า
# --------------------------------------------------
print("\n--- ข้อ 7 รูปแบบที่ 4: ฟังก์ชันมีพารามิเตอร์ มีการคืนค่า ---")
def find_median_with_param_with_return(data):
    sorted_data = sorted(data)
    median = sorted_data[len(sorted_data) // 2]
    return median

m3 = find_median_with_param_with_return([15, 42, 23])
print(f"ชุดข้อมูล 3 จำนวน [15, 42, 23] -> มัธยฐาน = {m3}")

m5 = find_median_with_param_with_return([10, 50, 30, 20, 40])
print(f"ชุดข้อมูล 5 จำนวน [10, 50, 30, 20, 40] -> มัธยฐาน = {m5}")

mn = find_median_with_param_with_return([5, 2, 8, 1, 9, 3, 7])
print(f"ชุดข้อมูล n จำนวน [5, 2, 8, 1, 9, 3, 7] -> มัธยฐาน = {mn}")

print("\n" + "=" * 60)
print("จบการทำงานทุกข้อ")
print("=" * 60)