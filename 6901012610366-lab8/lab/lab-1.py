class student:
    def __init__(self, student_id, name, course, age):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.course = course

    def show(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Course:", self.course)
        print("Age:", self.age)
        
s1 = student("001", "John Doe", "Computer Engineering", 20)
s1.show()


        