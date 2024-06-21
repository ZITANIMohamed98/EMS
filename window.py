from tkinter import ttk 
from tkinter import * 
import tkinter as tk
from App import main

file = "data.json"
# Top level window 
root = Tk()
frame = ttk.Frame(root, padding=10)
frame.grid()

root.title("EMS") 

root.geometry('400x200') 
# Function for getting Input 
# from textbox and printing it  
# at label widget 
  
def saveInput(): 
    inp = inputtxt1.get(1.0, "end-1c") 
    

message = tk.Label(frame, text="Veuillez Introduire les indices d'impact ")
Implbl = tk.Label(frame, text="Importance")

ImpEaudesc = tk.Label(frame, text="Eau")

# TextBox Creation 
ImpEau = tk.Text(frame, 
                   height = 1, 
                   width = 5) 

ImpEaudesc.grid(column=0, row=0)   # grid dynamically divides the space in a grid
ImpEau.grid(column=1, row=0)
 
desc2 = tk.Label(frame, text="Bruit")

# TextBox Creation 
inputtxt2 = tk.Text(frame, 
                   height = 1, 
                   width = 5) 
  
desc2.grid(column=0, row=1)   # grid dynamically divides the space in a grid
inputtxt2.grid(column=1, row=1)

desc2 = tk.Label(frame, text="Air")

# TextBox Creation 
inputtxt2 = tk.Text(frame, 
                   height = 1, 
                   width = 5) 
  
desc2.grid(column=0, row=2)   # grid dynamically divides the space in a grid
inputtxt2.grid(column=1, row=2)
desc2 = tk.Label(frame, text="Energie")

# TextBox Creation 
inputtxt2 = tk.Text(frame, 
                   height = 1, 
                   width = 5) 
  
desc2.grid(column=0, row=3)   # grid dynamically divides the space in a grid
inputtxt2.grid(column=1, row=3)
desc2 = tk.Label(frame, text="Dechets")

# TextBox Creation 
inputtxt2 = tk.Text(frame, 
                   height = 1, 
                   width = 5) 
  
desc2.grid(column=0, row=4)   # grid dynamically divides the space in a grid
inputtxt2.grid(column=1, row=4)

Implbl = tk.Label(frame, text="\Maitrise")

ImpEaudesc = tk.Label(frame, text="Eau")

# TextBox Creation 
ImpEau = tk.Text(frame, 
                   height = 1, 
                   width = 5) 

ImpEaudesc.grid(column=0, row=0)   # grid dynamically divides the space in a grid
ImpEau.grid(column=1, row=0)
 
desc2 = tk.Label(frame, text="Bruit")

# TextBox Creation 
inputtxt2 = tk.Text(frame, 
                   height = 1, 
                   width = 5) 
  
desc2.grid(column=0, row=1)   # grid dynamically divides the space in a grid
inputtxt2.grid(column=1, row=1)

desc2 = tk.Label(frame, text="Air")

# TextBox Creation 
inputtxt2 = tk.Text(frame, 
                   height = 1, 
                   width = 5) 
  
desc2.grid(column=0, row=2)   # grid dynamically divides the space in a grid
inputtxt2.grid(column=1, row=2)
desc2 = tk.Label(frame, text="Energie")

# TextBox Creation 
inputtxt2 = tk.Text(frame, 
                   height = 1, 
                   width = 5) 
  
desc2.grid(column=0, row=3)   # grid dynamically divides the space in a grid
inputtxt2.grid(column=1, row=3)
desc2 = tk.Label(frame, text="Dechets")

# TextBox Creation 
inputtxt2 = tk.Text(frame, 
                   height = 1, 
                   width = 5) 
  
desc2.grid(column=0, row=4)   # grid dynamically divides the space in a grid
inputtxt2.grid(column=1, row=4)
# Button Creation 
saveButton = tk.Button(frame, 
                        text = "Save",  
                        command = SaveInput) 

GenerateReport = tk.Button(frame, 
                        text = "Generer le rapport",  
                        command = main(file))
# Label Creation 
lbl = tk.Label(frame, text = "") 

quit = tk.Button(frame, text="Quit", command=frame.destroy)

frame.mainloop()