import tkinter as tk
from tkinter import ttk
import random
import sys
import os
guesses = 7


def restart_script():
    # Execute the command to run the script again
    os.execl(sys.executable, sys.executable, *sys.argv)

# Call the restart_script() function to restart the script


def second_window():
    # Window for guessing
    
    window2 = tk.Toplevel(window1)
    window2.title("Guess!")
    window2.geometry("350x150")
    window2.configure(bg="black")
    # Title

    title_label = ttk.Label(text="Number Guessing Game", master=window2, font ="Calibri 15 bold")
    title_label.configure(background="black", foreground="white")
    title_label.pack()

    # Input Field For Window 2
    global answer
    global button3
    answer = tk.StringVar()
    input_frame2 = tk.Frame(master=window2)
    input_frame2.configure(bg="black")
    button3 = tk.Button(text="Restart", master=input_frame2, command=restart_script)
    button2 = tk.Button(text="guess!", master=input_frame2, command=lambda: guess(react))
    entry_field3 = tk.Entry(master=input_frame2, textvariable=answer)
    button2.pack(side="left")
    entry_field3.pack(side="left")
    input_frame2.pack(pady = 10)

    # output
    react = tk.StringVar()
    output_label = tk.Label(
        master=window2,
        text = "Output",
        font = "Calibri 12 bold",
        textvariable=react

    )
    output_label.configure(background="black", foreground="white")
    react.set("You got this!")
    output_label.pack()




def guess(react):
    global guesses
    react.set("You got this!")
    if answer.get() == random_num:
        react.set("You did it! Nice! Would you like to play again?")
        button3.pack(pady=5)
    elif guesses == 0:
        react.set("Out of guesses, would you like to try again?")
        button3.pack(pady=5)
    elif answer.get() != random_num and answer.get().isnumeric():
        react.set("Incorrect! You have " + str(guesses) + " left")
        guesses -= 1
    elif answer.get().isalpha():
        react.set("That's not right, pick a number next time please.")


# window for choosing the range of numbers
window1 = tk.Tk()
window1.title("Game")
window1.geometry("350x150")
window1.configure(bg="black")
# Title

title_label1 = tk.Label(text="Number Guessing Game", master=window1, font = "Calibri 15 bold")
title_label1.configure(background="black", foreground="white")
title_label1.pack()

# Input Field for Window 1
input1 = tk.IntVar()
input2 = tk.IntVar()


input_frame1 = tk.Frame(master=window1, bg='black')
entry_field1 = tk.Entry(master = input_frame1, textvariable=input1)
entry_field2 = tk.Entry(master=input_frame1, textvariable=input2)
button1 = tk.Button(master = input_frame1, text="Let's go!", command=second_window)
entry_field1.pack(side="left", padx = 5)
entry_field2.pack(side="left")
button1.pack(side="left", padx=5)
input_frame1.pack()
random_num = random.randint(input1.get(), input2.get())
# run
window1.mainloop()
