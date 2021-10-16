import os 
import time
from tkinter import messagebox

time.sleep(200)

fh = open('match.txt')
for line in fh :
    line = len(line)



if line > 3 :
    
    quit()
    
 
else :
    messagebox.showinfo("warnnig","don't close the program again")
    os.system("shutdown /s")
    

os.system("rm match.txt")


