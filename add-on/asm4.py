print("\n" + "=" * 60)
print("ข้อ 4: ตรวจสอบรหัสผ่าน 4 ตัว (กรอกได้ไม่เกิน 3 ครั้ง)")
print("=" * 60)

# --------------------------------------------------
# ข้อ 4 - รูปแบบที่ 1: ไม่ใช้ฟังก์ชัน
# --------------------------------------------------
print("\n--- ข้อ 4 รูปแบบที่ 1: ไม่ใช้ฟังก์ชัน ---")
correct_password = "1234"
attempts = 0
max_attempts = 3
authenticated = False
while attempts < max_attempts:
    # จำลองการกรอกรหัสผ่าน (ใช้ค่าทดสอบ)
    test_inputs = ["0000", "1111", "1234"]
    pwd = test_inputs[attempts]
    print(f"กรอกรหัสผ่านครั้งที่ {attempts + 1}: {pwd}")
    if pwd == correct_password:
        print("Authentication Successful")
        authenticated = True
        break
    else:
        print("รหัสผ่านไม่ถูกต้อง")
    attempts += 1
if not authenticated:
    print("Authentication Failed - เกินจำนวนครั้งที่กำหนด")

# --------------------------------------------------
# ข้อ 4 - รูปแบบที่ 2: ฟังก์ชันไม่มีพารามิเตอร์ ไม่คืนค่า
# --------------------------------------------------
print("\n--- ข้อ 4 รูปแบบที่ 2: ฟังก์ชันไม่มีพารามิเตอร์ ไม่คืนค่า ---")
def check_password_no_param_no_return():
    correct_password = "1234"
    attempts = 0
    max_attempts = 3
    authenticated = False
    test_inputs = ["0000", "1111", "1234"]
    while attempts < max_attempts:
        pwd = test_inputs[attempts]
        print(f"กรอกรหัสผ่านครั้งที่ {attempts + 1}: {pwd}")
        if pwd == correct_password:
            print("Authentication Successful")
            authenticated = True
            break
        else:
            print("รหัสผ่านไม่ถูกต้อง")
        attempts += 1
    if not authenticated:
        print("Authentication Failed - เกินจำนวนครั้งที่กำหนด")

check_password_no_param_no_return()

# --------------------------------------------------
# ข้อ 4 - รูปแบบที่ 3: ฟังก์ชันมีพารามิเตอร์ ไม่คืนค่า
# --------------------------------------------------
print("\n--- ข้อ 4 รูปแบบที่ 3: ฟังก์ชันมีพารามิเตอร์ ไม่คืนค่า ---")
def check_password_with_param_no_return(correct_password, test_inputs):
    attempts = 0
    max_attempts = 3
    authenticated = False
    while attempts < max_attempts:
        pwd = test_inputs[attempts]
        print(f"กรอกรหัสผ่านครั้งที่ {attempts + 1}: {pwd}")
        if pwd == correct_password:
            print("Authentication Successful")
            authenticated = True
            break
        else:
            print("รหัสผ่านไม่ถูกต้อง")
        attempts += 1
    if not authenticated:
        print("Authentication Failed - เกินจำนวนครั้งที่กำหนด")

check_password_with_param_no_return("1234", ["0000", "1111", "1234"])

# --------------------------------------------------
# ข้อ 4 - รูปแบบที่ 4: ฟังก์ชันมีพารามิเตอร์ มีการคืนค่า
# --------------------------------------------------
print("\n--- ข้อ 4 รูปแบบที่ 4: ฟังก์ชันมีพารามิเตอร์ มีการคืนค่า ---")
def check_password_with_param_with_return(correct_password, test_inputs):
    attempts = 0
    max_attempts = 3
    for pwd in test_inputs[:max_attempts]:
        attempts += 1
        print(f"กรอกรหัสผ่านครั้งที่ {attempts}: {pwd}")
        if pwd == correct_password:
            return "Authentication Successful"
        else:
            print("รหัสผ่านไม่ถูกต้อง")
    return "Authentication Failed - เกินจำนวนครั้งที่กำหนด"

result4 = check_password_with_param_with_return("1234", ["0000", "1111", "1234"])
print(result4)
