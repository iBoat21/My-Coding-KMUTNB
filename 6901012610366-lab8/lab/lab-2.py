class Student:
    def __init__(self, student_id, name, course, age):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.age = age
        
    def show(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Course:", self.course)
        print("Age:", self.age)
    
    # def show_youngest(self):
    #     if self.age < 20:
    #         print("Youngest Student:")
    #         self.show()

def show_youngest_student(students):
    if not students:
        print("No students available.")
        return

    youngest_student = min(students, key=lambda s: s.age)
    print("Youngest Student:")
    youngest_student.show()

def read_student_file(filename):
    global student_array
    student_array = []
    try:
        with open(filename, "r") as f:
            for line in f:
                if not line.strip():
                    continue
                parts = line.split()
                if len(parts) == 4:
                    student_id, name, course, age = parts
                    student = Student(student_id, name, course, int(age))
                    student_array.append(student)
                else:
                    print("Invalid line format:", line)
    except FileNotFoundError:
            print("File not found. Please make sure '", filename, "' exists.")
    
def main():
    read_student_file("student_data.txt")
    show_youngest_student(student_array)

if __name__ == "__main__":
    main()