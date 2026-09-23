class Person():
    def __init__(self, id, name, addr, weight_kg, height_cm):
        self.id = id
        self.name = name
        self.addr = addr
        self.weight_kg = float(weight_kg)
        self.height_cm = float(height_cm)
    
    def bmi(self):
        height_m = self.height_cm/100
        return self.weight_kg / (height_m**2)
    
    def show(self):
        return f"{self.id} | {self.name} | {self.addr} | {self.weight_kg} | {self.height_cm} | {self.bmi()}"
    
class Student(Person):
    def __init__(self, id, name, addr, weight_kg, height_cm, course, gpa):
        super().__init__(id, name, addr, weight_kg, height_cm)
        self.course = course
        self.gpa = float(gpa)

    def show(self):
        base_info = super().show()
        return f"{base_info} | {self.course} | {self.gpa}"
    
class Employee(Person):
    def __init__(self, id, name, addr, weight_kg, height_cm, dep, salary):
        super().__init__(id, name, addr, weight_kg, height_cm)
        self.dep = dep
        self.salary = float(salary)
        
    def show(self):
        base_info = super().show()
        return f"{base_info}, | {self.dep} {self.salary}"
    
if __name__ == "__main__":
    p1 = Person("001","John Doe","KMUTNB", 180.0, 80)
    s1 = Student("S101", "Wichai", "Nonthaburi", 60.0, 170.0, "Computer Engineering", 3.45)
    e1 = Employee("E501", "Suda", "Nakhon Pathom", 52.0, 162.0, "Backend Developer", 45000.0)
    print("--- Person ---")
    print(p1.show())
    print("\n--- Student ---")
    print(s1.show())
    print("\n--- Employee ---")
    print(e1.show())