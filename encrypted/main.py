from tkinter import *
from tkinter import messagebox
import pybase64
import os
def main_screen():
    screen=Tk()
    screen.geometry("512x384")
    
    screen.title=("secretmessage")
    screen.mainloop()


    Label(text="encrypte or decrypte the text:", fg="black", font=("calibri", 14)).place(x=12, y=12)




main_screen()