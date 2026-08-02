def print_roof():
    print("   *   ")
    print("  ***  ")
    print(" ***** ")
    print("*******")

def print_ceiling():
    print("-------")

def print_wall():
    print("|     |")
    print("|     |")
    print("|     |")

def print_floor():
    print("-------")

def print_house(h):
    print_roof()
    for i in range(h):
        print_ceiling()
        print_wall()
    print_floor()


def main():
    print_house(int(input("Enter height of the house: ")))

if __name__ == "__main__":
    main()