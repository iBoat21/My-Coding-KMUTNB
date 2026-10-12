# check words character/vowel/palindrome

import tkinter as tk

def count_character():
    text = ent_text.get()
    char_to_find = ent_char.get()
    
    if not char_to_find:
        lbl_result.config(text="Result: Please enter character to find")
        return
        
    count = text.count(char_to_find)
    lbl_result.config(text=f"Character '{char_to_find}' count: {count}")

def count_vowels():
    text = ent_text.get().lower()
    vowels = "aeiou"
    count = sum(1 for ch in text if ch in vowels)
    lbl_result.config(text=f"Total Vowels (a, e, i, o, u): {count}")

def check_palindrome():
    text = ent_text.get()
    clean_text = "".join(ch.lower() for ch in text if ch.isalnum())
    
    if not clean_text:
        lbl_result.config(text="Result: Please enter text first")
        return

    if clean_text == clean_text[::-1]:
        lbl_result.config(text=f"'{text}' is a Palindrome")
    else:
        lbl_result.config(text=f"'{text}' is NOT a Palindrome")

root = tk.Tk()
root.title("Text Analyzer")
root.geometry("380x300")

tk.Label(root, text="Input Text:", font=("Arial", 10)).pack(anchor="w", padx=20, pady=(10, 0))
ent_text = tk.Entry(root, width=40)
ent_text.pack(padx=20, pady=5)

tk.Label(root, text="Search Character:", font=("Arial", 10)).pack(anchor="w", padx=20, pady=(5, 0))
ent_char = tk.Entry(root, width=10)
ent_char.pack(anchor="w", padx=20, pady=5)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=15)

btn_count_char = tk.Button(btn_frame, text="Count Character", width=16, command=count_character)
btn_count_char.grid(row=0, column=0, padx=5, pady=3)

btn_count_vowels = tk.Button(btn_frame, text="Count Vowels", width=16, command=count_vowels)
btn_count_vowels.grid(row=0, column=1, padx=5, pady=3)

btn_palindrome = tk.Button(btn_frame, text="Check Palindrome", width=34, command=check_palindrome)
btn_palindrome.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

lbl_result = tk.Label(root, text="Result will appear here", font=("Arial", 10, "bold"), fg="blue")
lbl_result.pack(pady=10)

root.mainloop()