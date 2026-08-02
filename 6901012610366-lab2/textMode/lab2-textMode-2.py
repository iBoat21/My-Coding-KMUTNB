height = int(input("Enter Height (Cm): "))
weight = int(input("Enter Weight (Kg): "))

BMI = weight / (height /100) ** 2
print(f"BMI is: {BMI:.2f}")