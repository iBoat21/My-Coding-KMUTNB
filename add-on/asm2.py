print("\n" + "=" * 60)
print("ข้อ 2: ตรวจสอบจำนวนเฉพาะ 1-100")
print("=" * 60)
# --------------------------------------------------
# ข้อ 2 - รูปแบบที่ 1: ไม่ใช้ฟังก์ชัน
# --------------------------------------------------
print("\n--- ข้อ 2 รูปแบบที่ 1: ไม่ใช้ฟังก์ชัน ---")
primes2 = []
for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes2.append(num)
print("จำนวนเฉพาะ 1-100:", primes2)

# --------------------------------------------------
# ข้อ 2 - รูปแบบที่ 2: ฟังก์ชันไม่มีพารามิเตอร์ ไม่คืนค่า
# --------------------------------------------------
print("\n--- ข้อ 2 รูปแบบที่ 2: ฟังก์ชันไม่มีพารามิเตอร์ ไม่คืนค่า ---")
def find_primes_no_param_no_return():
    primes = []
    for num in range(2, 101):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    print("จำนวนเฉพาะ 1-100:", primes)

find_primes_no_param_no_return()

# --------------------------------------------------
# ข้อ 2 - รูปแบบที่ 3: ฟังก์ชันมีพารามิเตอร์ ไม่คืนค่า
# --------------------------------------------------
print("\n--- ข้อ 2 รูปแบบที่ 3: ฟังก์ชันมีพารามิเตอร์ ไม่คืนค่า ---")
def find_primes_with_param_no_return(start, end):
    primes = []
    for num in range(start, end + 1):
        if num < 2:
            continue
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    print(f"จำนวนเฉพาะ {start}-{end}:", primes)

find_primes_with_param_no_return(1, 100)

# --------------------------------------------------
# ข้อ 2 - รูปแบบที่ 4: ฟังก์ชันมีพารามิเตอร์ มีการคืนค่า
# --------------------------------------------------
print("\n--- ข้อ 2 รูปแบบที่ 4: ฟังก์ชันมีพารามิเตอร์ มีการคืนค่า ---")
def find_primes_with_param_with_return(start, end):
    primes = []
    for num in range(start, end + 1):
        if num < 2:
            continue
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

result2 = find_primes_with_param_with_return(1, 100)
print("จำนวนเฉพาะ 1-100:", result2)