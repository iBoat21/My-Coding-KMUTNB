class Vehicle:
    def __init__(self, license_plate, brand, model, year, daily_rate):
        self.license_plate = license_plate
        self.brand = brand
        self.model = model
        self.year = int(year)
        self.daily_rate = float(daily_rate)

    def show_info(self):
        return (f"ทะเบียน: {self.license_plate} | ยี่ห้อ: {self.brand} "
                f"| รุ่น: {self.model} ({self.year}) | ค่าเช่า/วัน: {self.daily_rate:,.2f} บาท")

    def calculate_rental_cost(self, days):
        return self.daily_rate * days


class Car(Vehicle):
    def __init__(self, license_plate, brand, model, year, daily_rate, seats):
        super().__init__(license_plate, brand, model, year, daily_rate)
        self.seats = int(seats)

    def show_info(self):
        base_info = super().show_info()
        return f"{base_info} | จำนวนที่นั่ง: {self.seats} ที่นั่ง"

    def calculate_rental_cost(self, days):
        weeks = days // 7           
        remaining_days = days % 7   

        payable_days = (weeks * 5) + min(remaining_days, 5)
        return self.daily_rate * payable_days


class Truck(Vehicle):
    def __init__(self, license_plate, brand, model, year, daily_rate, payload):
        super().__init__(license_plate, brand, model, year, daily_rate)
        self.payload = float(payload)

    def show_info(self):
        base_info = super().show_info()
        return f"{base_info} | น้ำหนักบรรทุก: {self.payload} ตัน"
    
if __name__ == "__main__":
    v1 = Vehicle("กข-1234", "Honda", "Wave 110i", 2021, 300.0)
    car1 = Car("1กข-9999", "Toyota", "Corolla Cross", 2023, 1500.0, seats=5)
    truck1 = Truck("80-5555", "Isuzu", "ELF", 2020, 2500.0, payload=3.5)

    print("=== ข้อมูลยานพาหนะ ===")
    print(v1.show_info())
    print(car1.show_info())
    print(truck1.show_info())

    print("\n=== ทดสอบคำนวณค่าเช่าระยะเวลา 7 วัน ===")
    days = 7
    print(f"- {v1.brand} {v1.model} เช่า {days} วัน: {v1.calculate_rental_cost(days):,.2f} บาท (คิด 7 วันเต็ม)")
    print(f"- {car1.brand} {car1.model} เช่า {days} วัน: {car1.calculate_rental_cost(days):,.2f} บาท (โปรโมชัน จ่ายเพียง 5 วัน)")
    print(f"- {truck1.brand} {truck1.model} เช่า {days} วัน: {truck1.calculate_rental_cost(days):,.2f} บาท (ไม่มีโปร คิด 7 วันเต็ม)")