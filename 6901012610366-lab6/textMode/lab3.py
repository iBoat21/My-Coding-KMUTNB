def countVowels():
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

def main():
    global text
    text = input("Enter a string: ")
    vowel_count = countVowels()
    print(f"The number of vowels in the string is: {vowel_count}")

if __name__ == "__main__":
    main()
    