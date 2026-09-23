def char():
    characters = input("Enter characters to find: ")
    return characters

def voc():
    vocab = input("Enter a vocab: ")
    return vocab

def count_characters(text, characters):
    count = 0
    start = 0
    while start < len(text):
        index = text.find(characters, start)
        if index == -1:
            break
        count += 1
        start = index + max(1, len(characters))
    return count

def main():
    print("Character Counting Program")
    text = voc()
    characters = char()
    count = count_characters(text, characters)
    if count > 0:
        print(f"'{characters}' found {count} times in the text.")
    else:
        print(f"'{characters}' not found in the text.")

if __name__ == "__main__":
    main()