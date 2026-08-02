amount = -1
while amount != 0:
    amount = int(input("Enter the amount you want to exchange (press 0 to exit): ")) 
    print("คุณได้รับเหรียญ 10 บาท จำนวน", amount // 10, "เหรียญ")
    amount = amount % 10
    print("คุณได้รับเหรียญ 5 บาท จำนวน", amount // 5, "เหรียญ")
    amount = amount % 5
    print("คุณได้รับเหรียญ 1 บาท จำนวน", amount // 1, "เหรียญ")
    amount = amount % 1
    