# test GUI
import tkinter
window = tkinter.Tk() # create main window
window.title("My tk App") # set title
window.geometry("500x500") # set size

label = tkinter.Label(window, text="Hola")
label.pack()

textBox = tkinter.Entry(window)
textBox.pack()

btn = tkinter.Button(window, text="Multiply")
btn.pack()
window.mainloop()