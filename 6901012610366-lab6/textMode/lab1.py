def a():
    print("Finding characters program from left")
    text = input("Enter a vocab: ")
    characters = input("Enter characters to find: ")
    
    found = False
    start = 0
    length = len(text)
    
    while start < length:
        index = text.find(characters, start)
        if index == -1:
            break
        print(f"Found '{characters}' at index {index}")
        found = True
        # Move forward past the current match (or by 1 for single-char offset)
        start = index + max(1, len(characters))

    if not found:
        print(f"'{characters}' not found in text.")

def b():
    print("Finding characters program from right (Starting from right = Index 0)")
    text = input("Enter a vocab: ")
    characters = input("Enter characters to find: ")
    
    found = False
    end = len(text)
    
    while end > 0:
        index = text.rfind(characters, 0, end)
        if index == -1:
            break
            
        # คำนวณ Index โดยเริ่มนับจากขวาสุดให้เป็น 0
        right_index = (len(text) - 1) - index
        
        print(f"Found '{characters}' at right-index {right_index} (Normal index was {index})")
        found = True
        end = index

    if not found:
        print(f"'{characters}' not found in text.")

def e():
    print("Is this vocab a palindrome?")
    text = input("Enter a vocab: ")
    text = text.lower().replace(" ", "")
    while True:
        if text == text[::-1]:
            print(f"'{text}' is a palindrome.")
            break
        else:
            print(f"'{text}' is not a palindrome.")
            break

def main():
    print("Select an option:")
    print("1. Find characters from left")
    print("2. Find characters from right")
    print("3. Check if vocab is a palindrome")
    
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            a()
        elif choice == 2:
            b()
        elif choice == 3:
            e()
        else:
            print("Invalid choice. Please select either 1, 2, or 3.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()