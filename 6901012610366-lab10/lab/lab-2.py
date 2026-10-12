# counter app
import tkinter as tk

counter = 0

def increase():
    global counter
    counter += 1
    lbl_count.config(text=str(counter))

def decrease():
    global counter
    counter -= 1
    lbl_count.config(text=str(counter))

def reset():
    global counter
    counter = 0
    lbl_count.config(text=str(counter))

root = tk.Tk()
root.title("Counter App")
root.geometry("250x180")

lbl_count = tk.Label(root, text="0", font=("Arial", 32, "bold"))
lbl_count.pack(pady=10)

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

btn_increase = tk.Button(frame_buttons, text="Increase", width=8, command=increase)
btn_increase.grid(row=0, column=0, padx=4)

btn_decrease = tk.Button(frame_buttons, text="Decrease", width=8, command=decrease)
btn_decrease.grid(row=0, column=1, padx=4)

btn_reset = tk.Button(root, text="Reset", width=18, command=reset)
btn_reset.pack(pady=5)

root.mainloop()