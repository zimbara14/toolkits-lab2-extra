import tkinter as tk
from tkinter import messagebox
import sys
sys.path.insert(1, '/Users/zimbara/Desktop/code/toolkits/lab2')
from main import result

top = tk.Tk()
top.wm_title("Attention!")


def clck():
    top.title="Result"
    if result():
        tk.messagebox.showinfo(top.title, "Congratulations! You guessed the number! Keep going.")
    else:
        tk.messagebox.showinfo(top.title, "Game over! You did not guess the number. Better luck next time.")


B1 = tk.Button(top, text="Click me to see your score", command=clck)
B1.pack()

top.mainloop()
