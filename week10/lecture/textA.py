#Define vendingMachine

class vendingMachine:
    def __init__(self, count=0, max=0):
        self.count = count
        self.max = max
        self.stock = 100
        
    def refill(self):
        self.count = self.max
        print("Refilled")
        
    def sell(self, order):
        self.count -= order
        print('sold: ',order)
    
    def print_stock(self):
        print('Current stock: ', self.count)
        
stock = int(input())
vm = vendingMachine(stock)
vm.print_stock()
order_1 = int(input())
vm.sell(order_1)
vm.print_stock()
vm.refill()
vm.print_stock()
        
    