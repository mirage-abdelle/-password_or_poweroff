from tkinter import messagebox
import os


os.system("echo 0 > match.txt")


print("Warning  if you try the wrong password your pc ganna  powroff ")

a =input('enter password : ')
b="karim"
if a==b :
    os.system("echo it's match > match.txt")
    messagebox.showinfo("congratulations!!","           match \n your welcome to your pc")


else :
    messagebox.showinfo("warnnig","call : +212616946513 \n for your password")
    os.system("shutdown /s")