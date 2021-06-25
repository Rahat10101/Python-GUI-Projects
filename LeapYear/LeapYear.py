from tkinter import*

root = Tk()
root.geometry("350x300")

def check_year():
    t.delete(0.0 , 'end')

    year = int(e.get())

    if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        s = "{} is a Leap Year . ".format(year)

    else:
        s = "{} is not a Leap Year . ".format(year)

    t.insert(0.0, s)


l1 = Label(root, text = "  Input Year ")
l1.grid(row = 0, column = 0)

gap1 = Label(root, text = "    ")
gap1.grid(row = 1, column = 0)

gap2 = Label(root, text = "     ")
gap2.grid(row = 3, column = 0)


e = Entry(root, width = 30)
e.grid(row = 0, column = 1)

b1 = Button(root, text = " Check " , bg = "#656665" , fg = "#ffffff", command = check_year)
b1.grid(row = 2 , columnspan = 2)

t = Text(root, width = 25 , height = 10, wrap = WORD)
t.grid(row = 4 , columnspan = 2)

root.mainloop()

