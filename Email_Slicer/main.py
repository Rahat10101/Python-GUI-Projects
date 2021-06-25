from tkinter import*

root = Tk()
root.geometry("350x300")

def slice():
    t.delete(0.0 , 'end')

    email = e.get()

    user_name = email[:email.index("@")]
    domain_name = email[email.index("@") + 1:]

    s = "Your username is '{}' \n and \nyour domain name is '{}' \n".format(user_name, domain_name)

    t.insert(0.0 , s)


l1 = Label(root, text = " Input E-Mail ")
l1.grid(row = 0, column = 0)

gap1 = Label(root, text = "    ")
gap1.grid(row = 2, column = 0)

gap2 = Label(root, text = "     ")
gap2.grid(row = 4, column = 0)

e = Entry(root, width = 30)
e.grid(row = 0, column = 1)

b1 = Button(root, text = " Check " , bg = "#656665" , fg = "#ffffff", command = slice)
b1.grid(row = 3, columnspan = 2)

t = Text(root, width = 25 , height = 10, wrap = WORD)
t.grid(row = 5 , columnspan = 2)

root.mainloop()
