from tkinter import *
from tkinter import messagebox
import pybase64
import os
def main_screen():
    screen=Tk()
    screen.geometry("512x450")
    screen.config(bg="black")
    
    def reset():
        code.set("")
        text1.delete(1.0,END)


    Label(text="encrypte or decrypte the text:",bg="black", fg="white", font=("calibri", 15)).place(x=12, y=12)
    screen.title=("secretmessage")
    text1=Text(font="Robote 20",bg="grey80",relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=12,y=54,width=500,height=100)
    Label(text="enter the key:",bg="black",fg="white",font=("calibri", 15)).place(x=10,y=160)
   
    code=StringVar()
    Entry(textvariable=code,width=19,bg="grey80",bd=0,font=("arial",25),show="*").place(x=10,y=200,height=70,width=500)
    Button(text="ENCRYPT", height=4, width=25, bg="green1", fg="black", bd=0).place(x=10, y=290)
    Button(text="DECRYPT", height=4, width=25, bg="red1", fg="black", bd=0).place(x=317, y=290)
    Button(text="RESET", height=4, width=69, bg="blue1", fg="black", bd=0 ,command=reset).place(x=10, y=370)

    
    
    
    
    screen.mainloop()
    




main_screen()