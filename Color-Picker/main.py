from tkinter import *
from tkinter import colorchooser

root = Tk()
root.title("Color Picker")
root.geometry("800x200")


def color():
    my_color = colorchooser.askcolor()[1]
    my_label = Label(root, text=my_color).pack(pady=10)
    my_label2 = Label(root, text="You Picked a Color !", font=("courier", 32), bg=my_color).pack()


my_button = Button(root, text="Pick A Color", command=color).pack()

root.mainloop()
