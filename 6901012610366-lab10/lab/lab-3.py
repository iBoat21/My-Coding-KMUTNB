# temperature check
import tkinter as tk

def convert_temp():
    val = ent_celsius.get().strip()
    try:
        celsius = float(val)
        fahrenheit = (celsius * 9 / 5) + 32
        lbl_result.config(text=f"Result: {fahrenheit:.2f} F", fg="black")
    except ValueError:
        lbl_result.config(text="Error: Numbers only!", fg="red")

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("320x160")

lbl_prompt = tk.Label(root, text="Enter Temperature (C):", font=("Arial", 10))
lbl_prompt.pack(pady=(15, 2))

ent_celsius = tk.Entry(root, width=15, justify="center", font=("Arial", 11))
ent_celsius.pack(pady=2)

btn_convert = tk.Button(root, text="Convert", command=convert_temp)
btn_convert.pack(pady=8)

lbl_result = tk.Label(root, text="Result: -", font=("Arial", 11, "bold"))
lbl_result.pack(pady=5)

root.mainloop()