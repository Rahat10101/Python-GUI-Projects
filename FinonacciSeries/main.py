from functools import lru_cache
from tkinter import*

root = Tk()
root.geometry("350x300")


@lru_cache(maxsize=1000)
def fibonacci(n):
    if type(n) != int:
        print("n must positive integer . ")
        print("Try again ! ")
    if n < 1:
        print("n must positive integer . ")

    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-1)


def generate():
    t.delete(0.0 , 'end')

    num = int(e.get())

    for n in range(1, num):
        print(fibonacci(n))

    #t.insert(0.0 , s)


l1 = Label(root, text = "  Input the Range : ")
l1.grid(row = 0, column = 0)

gap1 = Label(root, text = "    ")
gap1.grid(row = 1, column = 0)

gap2 = Label(root, text = "     ")
gap2.grid(row = 3, column = 0)


e = Entry(root, width = 30)
e.grid(row = 0, column = 1)

b1 = Button(root, text = " Generate Fibonacci " , bg = "#656665" , fg = "#ffffff", command = generate)
b1.grid(row = 2 , columnspan = 2)

t = Text(root, width = 25 , height = 10, wrap = WORD)
t.grid(row = 4 , columnspan = 2)

root.mainloop()