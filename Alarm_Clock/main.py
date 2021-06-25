from tkinter import *
import tkinter as tk
import time
import time as tm
import threading
import datetime

# LOAD WINDOW
gui_window = tk.Tk()
gui_window.configure(background="black")
gui_window.attributes("-fullscreen", True)


# DISPLAY THE CURRENT TIME
# RETRIEVE THE CURRENT TIME
def display_time():
    current_our = tm.strftime('%I:')
    our_label['text'] = current_our
    our_label.after(1000, display_time)
    current_minute = tm.strftime('%M')
    minute_label['text'] = current_minute
    minute_label.after(1000, display_time)
    current_am = tm.strftime(' %p')
    am_label['text'] = current_am
    am_label.after(1000, display_time)


# DISPLAY THE CURRENT TIME
our_label = tk.Label(gui_window, font='CodeDemoBold 300', bg='black', fg='white')
our_label.grid(row=0, column=0)
minute_label = tk.Label(gui_window, font='CodeDemoLight 300', bg='black', fg='white')
minute_label.grid(row=0, column=1)
am_label = tk.Label(gui_window, font='CodeDemoBold 300', bg='black', fg='white')
am_label.grid(row=0, column=2)
display_time()


# DISPLAY THE GOOD MORNING MESSAGE (DEPENDENT ON THE TIME)
# RETRIEVE MORNING TEXT
def morningTextretrieve():
    currentTime = datetime.datetime.now()
    currentTime.hour
    if 6 <= currentTime.hour <= 12:
        morningText = "Good Morning!"
    elif 13 <= currentTime.hour <= 18:
        morningText = "Good Afternoon!"
    elif 19 <= currentTime.hour <= 5:
        morningText = "Good Night!"
    time.sleep(10)


i = 1
while i < 10:
    morningTextretrieve()
    time.sleep(10)
morningtextLabel['text'] = morningText
# DISPLAY THE GOOD MORNING MESSAGE
morningtextLabel = tk.Label(gui_window, font='CodeDemoBold 300', bg='black', fg='white')
morningtextLabel.grid(row=5, column=0)

gui_window.mainloop()