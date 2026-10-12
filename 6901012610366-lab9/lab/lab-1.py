class Person:
    def __init__(self, name, addr, weight_kg, height_cm):
        self.name = name
        self.addr = addr
        self.weight_kg = float(weight_kg)
        self.height_cm = float(height_cm)

    def getBMI(self):
        """คำนวณและคืนค่า BMI ตามที่โจทย์กำหนดชื่อเมธอด getBMI()"""
        height_m = self.height_cm / 100
        return self.weight_kg / (height_m ** 2)

    def show(self):
        """แสดงข้อมูลพื้นฐานของบุคคลทั่วไป"""
        return f"Name: {self.name} | Address: {self.addr} | Weight: {self.weight_kg} kg | Height: {self.height_cm} cm"


class Student(Person):
    def __init__(self, student_id, name, addr, weight_kg, height_cm, course, gpa):
        super().__init__(name, addr, weight_kg, height_cm)
        self.student_id = student_id
        self.course = course
        self.gpa = float(gpa)

    def show(self):
        """เรียกใช้ show() และ getBMI() จากคลาสแม่ตามโจทย์"""
        base_info = super().show()
        bmi_value = self.getBMI()
        return f"ID: {self.student_id} | {base_info} | Course: {self.course} | GPA: {self.gpa:.2f} | BMI: {bmi_value:.2f}"


class Employee(Person):
    def __init__(self, employee_id, name, addr, weight_kg, height_cm, department, salary):
        super().__init__(name, addr, weight_kg, height_cm)
        self.employee_id = employee_id
        self.department = department
        self.salary = float(salary)

    def show(self):
        """เรียกใช้ show() และ getBMI() จากคลาสแม่ตามโจทย์"""
        base_info = super().show()
        bmi_value = self.getBMI()
        return f"ID: {self.employee_id} | {base_info} | Dept: {self.department} | Salary: {self.salary:,.2f} | BMI: {bmi_value:.2f}"


if __name__ == "__main__":
    p1 = Person("John Doe", "KMUTNB", 80.0, 180.0)
    
    s1 = Student("S101", "Wichai", "Nonthaburi", 60.0, 170.0, "Computer Engineering", 3.45)
    
    e1 = Employee("E501", "Suda", "Nakhon Pathom", 52.0, 162.0, "Backend Developer", 45000.0)

    print("--- Person ---")
    print(p1.show())
    print(f"BMI: {p1.getBMI():.2f}")

    print("\n--- Student ---")
    print(s1.show())

    print("\n--- Employee ---")
    print(e1.show())