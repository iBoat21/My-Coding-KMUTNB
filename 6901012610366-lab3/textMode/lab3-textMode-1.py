def weight():
    weight = float(input("Enter your weight in kilograms: "))
    return weight

def height():
    height = float(input("Enter your height in meters: "))
    return height

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def select():
    print("Select an option:")
    print("1. BMI for adults")
    print("2. BMI for children")
    choice = int(input("Enter your choice: "))
    return choice

def main():
    choice = select()
    weight_value = weight()
    height_value = height()
    bmi_value = calculate_bmi(weight_value, height_value)
    
    if choice == 1:
        print(f"Your BMI for adults is: {bmi_value:.2f}")
    elif choice == 2:
        print(f"Your BMI for children is: {bmi_value:.2f}")
    else:
        print("Invalid choice. Please select either 1 or 2.")

if __name__ == "__main__":
    main()
