from tkinter import *
from tkinter import messagebox
import pybase64
import os
def main_screen():
    screen=Tk()
    screen.geometry("512x384")
    
    Label(text="encrypte or decrypte the text:", fg="black", font=("calibri", 14)).place(x=12, y=12)
    screen.title=("secretmessage")
    text1=Text(font="Robote 20",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=12,y=54,width=500,height=100)
    Label(text="enter the key:",fg="black",font=("calibri", 14)).place(x=10,y=150)
    text2=Text(font="Robote 20",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text2.place(x=12,y=190,width=500,height=100)

    
    
    
    
    screen.mainloop()
    




main_screen()