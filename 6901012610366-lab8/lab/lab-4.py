class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        print(f"Product Name: {self.name}, Price: ${self.price:.2f}")
        
def add_product(name, price):
    with open("products.txt","a") as file:
        file.write(f"{name},{price}\n")
    print(f"เพิ่มสินค้า'{name}'สำเร็จแล้ว\n")
    
def read_products_from_file(filename):
    products = []
    try:
        with open(filename, "r") as file:
            for line in file:
                if not line.strip():
                    continue
                name, price = line.split(",")
                product = Product(name.strip(), float(price.strip()))
                products.append(product)
    except FileNotFoundError:
        print(f"File '{filename}' not found. Please make sure it exists.")
    return products

def display_info(products):
    if not products:
        print("ไม่มีสินค้า")
        return
    
    print("รายการสินค้า")
    for product in products:
        product.display_info()

def main():
    while True:
        print("1: Add product")
        print("2: View products")
        print("3: Exit")
        
        choice = input("Enter Choice (1-3): ").strip()

        match choice:
            case "1":
                # รับค่า name และ price ก่อนส่งเข้าฟังก์ชัน
                name = input("Enter product name: ").strip()
                try:
                    price = float(input("Enter product price: "))
                    add_product(name, price)
                except ValueError:
                    print("ราคาต้องเป็นตัวเลขเท่านั้น!\n")

            case "2":
                # อ่านไฟล์ก่อน แล้วส่งผลลัพธ์ไปให้ display_info()
                items = read_products_from_file("products.txt")
                display_info(items)

            case "3":
                print("ออกจากโปรแกรม")
                break

            case _:
                print("กรุณาเลือกเฉพาะ 1, 2 หรือ 3\n")
        
if __name__ == "__main__":
    main()