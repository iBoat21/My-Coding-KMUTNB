def grade():
    score = int(input("Enter your score: "))
    if score >=80:
        print("Your grade is A")
    elif score >=70:
        print("Your grade is B")
    elif score >=60:
        print("Your grade is C")
    elif score >=50:
        print("Your grade is D")
    else:
        print("Your grade is F")

def main():
        grade()

if __name__ == "__main__":
    main()