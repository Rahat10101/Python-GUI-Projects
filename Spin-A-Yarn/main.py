from tkinter import *

root = Tk()
root.title('Spin a Yarn')
root.geometry("500x400")


def grab():
    my_label.config(text=my_spin.get())


names = ("Nafu", "Roza", "Nafu Babu", "Picchi Billi")
#my_spin = Spinbox(root, from_=0, to=100000, increment=1, font=("Helvetica", 20))
my_spin = Spinbox(root, values=names, font=("Helvetica", 20))
my_spin.pack(pady=20)

my_button = Button(root, text="Submit", command=grab)
my_button.pack(pady=20)

my_label = Label(root, text="")
my_label.pack(pady=20)

root.mainloop()
