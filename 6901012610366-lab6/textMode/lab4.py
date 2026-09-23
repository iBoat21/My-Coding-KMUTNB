def countWords():
    text = input("Enter a string: ")
    words = text.split()
    word_count = len(words)
    print("Number of words:", word_count)

def main():
    countWords()

if __name__ == "__main__":
    main()