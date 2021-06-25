from tkinter import *
from random import randint
from tkinter import ttk
from PIL import ImageTk, Image

root = Tk()
root.title(' Rock, Paper, Scissors ')
root.geometry("800x900")
root.config(bg="white")

rock = ImageTk.PhotoImage(Image.open('Rock.png'))
paper = ImageTk.PhotoImage(Image.open('paper.png'))
scissors = ImageTk.PhotoImage(Image.open('Scissors.png'))

image_list = [rock, paper, scissors]

pick_number = randint(0, 2)

image_label = Label(root, image=image_list[pick_number], bd=0)
image_label.pack(pady=20)


def spin():
    pick_number = randint(0, 2)
    image_label.config(image=image_list[pick_number])

    if user_choice.get() == "Rock":
        user_choice_value = 0
    elif user_choice.get() == "Paper":
        user_choice_value = 1
    elif user_choice.get() == "Scissors":
        user_choice_value = 2

    if user_choice_value == 0:
        if pick_number == 0:
            win_lose_label.config(text="It's A Tie ! Spin Again ...")
        elif pick_number == 1:
            win_lose_label.config(text="Paper Cover Rock ! You Lose ...")
        elif pick_number == 2:
            win_lose_label.config(text="Rock Smashes Scissors !  You Win !!!")

    if user_choice_value == 1:
        if pick_number == 1:
            win_lose_label.config(text="It's A Tie ! Spin Again ...")
        elif pick_number == 0:
            win_lose_label.config(text="Paper Cover Rock ! You Win !!!")
        elif pick_number == 2:
            win_lose_label.config(text="Scissors Cuts Paper ! You Lose...")

    if user_choice_value == 2:
        if pick_number == 2:
            win_lose_label.config(text="It's A Tie ! Spin Again ...")
        elif pick_number == 0:
            win_lose_label.config(text="Rock Smashes Scissors ! You Lose ...")
        elif pick_number == 1:
            win_lose_label.config(text="Scissors Cuts Paper ! You Win !!!")


user_choice = ttk.Combobox(root, value=("Rock", "Paper", "Scissors"))
user_choice.current(0)
user_choice.pack(pady=20)

spin_button = Button(root, text="Spin !", command=spin)
spin_button.pack(pady=10)

win_lose_label = Label(root, text="", font=("Helvetica", 18), bg="white")
win_lose_label.pack(pady=50)

root.mainloop()
