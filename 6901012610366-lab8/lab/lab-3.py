class Product:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty
    
    def show(self):
        print("Product Name:", self.name)
        print("Price:", self.price)
        print("Quantity:", self.qty)
        
p1 = Product("Laptop", 1500, 5)
p1.show()