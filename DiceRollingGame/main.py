import random
from tkinter import *
import tkinter as tk



root=tk.Tk()
root.geometry("700x400")
root.title("Rolling Dice")

l1 = Label(root,font=("Courier",250))

def roll():
    number = ["\u2680","\u2681","\u2682","\u2683","\u2684","\u2685"]
    l1.config(text=f'{random.choice(number)} {random.choice(number)}')
    l1.pack()

b1 = tk.Button(root,text="Let's Roll ! ",foreground= 'red', command= roll)
b1.place(x=320,y=180)

root.mainloop()