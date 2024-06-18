from tkinter import ttk 
from tkinter import * 
import tkinter as tk
# Top level window 
root = Tk()
frame = ttk.Frame(root, padding=10)
frame.grid()

root.title("EMS") 

root.geometry('400x200') 
# Function for getting Input 
# from textbox and printing it  
# at label widget 
  
def printInput(): 
    inp = inputtxt1.get(1.0, "end-1c") 
    lbl.config(text = "Provided Input: "+inp) 

desc1 = tk.Label(frame, text="Hello World!")

# TextBox Creation 
inputtxt1 = tk.Text(frame, 
                   height = 1, 
                   width = 5) 

desc1.grid(column=0, row=0)   # grid dynamically divides the space in a grid
inputtxt1.grid(column=1, row=0)
 
desc2 = tk.Label(frame, text="Hello World!")

# TextBox Creation 
inputtxt2 = tk.Text(frame, 
                   height = 1, 
                   width = 5) 
  
desc2.grid(column=0, row=1)   # grid dynamically divides the space in a grid
inputtxt2.grid(column=1, row=1)

desc2 = tk.Label(frame, text="Hello World!")

# TextBox Creation 
inputtxt2 = tk.Text(frame, 
                   height = 1, 
                   width = 5) 
  
desc2.grid(column=0, row=2)   # grid dynamically divides the space in a grid
inputtxt2.grid(column=1, row=2)
desc2 = tk.Label(frame, text="Hello World!")

# TextBox Creation 
inputtxt2 = tk.Text(frame, 
                   height = 1, 
                   width = 5) 
  
desc2.grid(column=0, row=3)   # grid dynamically divides the space in a grid
inputtxt2.grid(column=1, row=3)
desc2 = tk.Label(frame, text="Hello World!")

# TextBox Creation 
inputtxt2 = tk.Text(frame, 
                   height = 1, 
                   width = 5) 
  
desc2.grid(column=0, row=4)   # grid dynamically divides the space in a grid
inputtxt2.grid(column=1, row=4)
# Button Creation 
printButton = tk.Button(frame, 
                        text = "Print",  
                        command = printInput) 


# Label Creation 
lbl = tk.Label(frame, text = "") 

quit = tk.Button(frame, text="Quit", command=frame.destroy)

frame.mainloop()