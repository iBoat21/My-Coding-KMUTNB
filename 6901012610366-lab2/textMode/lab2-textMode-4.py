def say_hello():
    choice = int(input("Enter Choice:"))
    match choice:
        case 1:
            result = print("Hello, KMUTNB")
        case 2:
            result = print("Sawassdee, KMUTNB")
        case 3:
            result = print("สวัสดี, KMUTNB")
        case 4:
            result = print("Error: Invalid Choice")
        case _:
            result = print("Error: Invalid Choice")
    print(f"Result: {result}")

def main():
    say_hello()

if __name__ == "__main__":
    main()