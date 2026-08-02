balance = 1000.0

def check_balance():
    print(f"ยอดเงินปัจจุบันของคุณคือ: {balance:.2f} บาท")

def deposit(amount):
    global balance 
    if amount > 0:
        balance += amount
        print(f"ฝากเงินสำเร็จจำนวน {amount:.2f} บาท")
    else:
        print("จำนวนเงินไม่ถูกต้อง!")


def withdraw(amount):
    global balance
    if amount > 0 and amount <= balance:
        balance -= amount
        print(f"ถอนเงินสำเร็จจำนวน {amount:.2f} บาท")
    else:
        print("จำนวนเงินไม่ถูกต้อง หรือยอดเงินของคุณไม่เพียงพอ!")
        
def main():
    choice = 0

    while choice != 4:
        print("\n===== ยินดีต้อนรับสู่ระบบธนาคาร =====")
        print("1. ตรวจสอบยอดเงิน")
        print("2. ฝากเงิน")
        print("3. ถอนเงิน")
        print("4. ออกจากระบบ")

        choice = int(input("กรุณาเลือกรายการ (1-4): "))

        if choice == 1:
            check_balance()

        elif choice == 2:
            money = float(input("ระบุจำนวนเงินที่ต้องการฝาก: "))
            deposit(money)

        elif choice == 3:
            money = float(input("ระบุจำนวนเงินที่ต้องการถอน: "))
            withdraw(money)

        elif choice == 4:
            print("ขอบคุณที่ใช้บริการ ลาโกน!")
        else:
            print("เลือกเมนูไม่ถูกต้อง กรุณาเลือกใหม่")
if __name__ == "__main__":
    main()