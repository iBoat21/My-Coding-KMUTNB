price_list = [200, 100, 1400, 800]
pay = 3000

def cal_dis():
    price = [int(x) for x in price_list]
    total_net_price = 0  
    
    print("--- รายละเอียดส่วนลดสินค้าแต่ละชิ้น ---")
    
    for x in price:
        if x > 2000:
            print(f"สินค้า ราคา {x} บาท -> Over price (เกินยอดที่กำหนด)")
            net_item = x  
        elif x >= 1000:
            discount = x * 0.15
            net_item = x - discount
            print(f"สินค้า ราคา {x} บาท -> ได้รับส่วนลด 15% ({discount} บาท) | เหลือสุทธิ {net_item} บาท")
        elif x >= 500:
            discount = x * 0.1
            net_item = x - discount
            print(f"สินค้า ราคา {x} บาท -> ได้รับส่วนลด 10% ({discount} บาท) | เหลือสุทธิ {net_item} บาท")
        elif x >= 300:
            discount = x * 0.05
            net_item = x - discount
            print(f"สินค้า ราคา {x} บาท -> ได้รับส่วนลด 5% ({discount} บาท) | เหลือสุทธิ {net_item} บาท")
        else:
            net_item = x
            print(f"สินค้า ราคา {x} บาท -> ไม่มีส่วนลด | เหลือสุทธิ {net_item} บาท")
            
        total_net_price += net_item
        
    print(f"\nรวมยอดสุทธิทั้งหมดที่ต้องชำระ: {total_net_price} บาท")
    return total_net_price
            
def cal_change(net_price):
    change_type = [1000, 500, 100, 50, 20, 10, 5, 2, 1]
    change_total = pay - net_price
    
    print(f"\n--- รายการเงินทอนสุทธิ {change_total} บาท ---")
    
    for coin in change_type:
        if change_total >= coin:
            count = int(change_total // coin)
            change_total = change_total % coin
            
            unit = "ใบ" if coin >= 20 else "เหรียญ"
            print(f"แบงค์/เหรียญ {coin} บาท จำนวน {count} {unit}")
        
if __name__ == "__main__":
    final_price = cal_dis()
    cal_change(final_price)
