from tkinter import *
from tkinter import messagebox
import base64
import os


def encrypt():
    password = code.get()
    if password == "1337":
        screen1 = Toplevel(screen)
        screen1.title("encryption")

        screen1.geometry("512x450")
        screen1.configure(bg="#ed3833")
        message = text1.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypted_message = base64_bytes.decode("ascii")
        Label(screen1, text="ENCRYPT", font="Arial", fg="white", bg="#ed3833").place(x=10, y=0)
        text2 = Text(screen1, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=300, height=150)
        text2.insert(END, encrypted_message)
    elif password == "":
        messagebox.showerror("Password Error", "Password field is empty")
    elif password != "1337":
        messagebox.showerror("Password Error", "Incorrect password")


def decrypt():
    password = code.get()
    if password == "1337":
        screen2 = Toplevel(screen)
        screen2.title("decryption")
        screen2.geometry("512x450")
        screen2.configure(bg="#00bd56")
        message = text1.get(1.0, END)
        try:
            decode_message = base64.b64decode(message.encode("ascii"))
            decrypted_message = decode_message.decode("ascii")
            Label(screen2, text="DECRYPT", font="Arial", fg="white", bg="#00bd56").place(x=10, y=0)
            text2 = Text(screen2, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
            text2.place(x=10, y=40, width=300, height=150)
            text2.insert(END, decrypted_message)
        except base64.binascii.Error:
            messagebox.showerror("Decryption Error", "Invalid Base64 encoded message")
    elif password == "":
        messagebox.showerror("Password Error", "Password field is empty")
    elif password != "1337":
        messagebox.showerror("Password Error", "Incorrect password")

    






def main_screen():
    global screen
    global code
    global text1

    screen = Tk()
    screen.geometry("512x450")
    screen.config(bg="black")
    screen.title("secretmessage")


    




    def reset():
        code.set("")
        text1.delete(1.0,END)


    Label(text="encrypte or decrypte the text:",bg="black", fg="white", font=("calibri", 15)).place(x=12, y=12)
    
    text1=Text(font="Robote 20",bg="grey80",relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=12,y=54,width=500,height=100)
    Label(text="enter the key:",bg="black",fg="white",font=("calibri", 15)).place(x=10,y=160)
   
    code=StringVar()
    Entry(textvariable=code,width=19,bg="grey80",bd=0,font=("arial",25),show="*").place(x=10,y=200,height=70,width=500)
    Button(text="ENCRYPT", height=4, width=25, bg="green1", fg="black", bd=0 ,command=encrypt).place(x=10, y=290)
    Button(text="DECRYPT", height=4, width=25, bg="red1", fg="black", bd=0,command=decrypt).place(x=317, y=290)
    Button(text="RESET", height=4, width=69, bg="blue1", fg="black", bd=0 ,command=reset).place(x=10, y=370)

    
    
    
    
    screen.mainloop()
    




main_screen()