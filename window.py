from tkinter import ttk 
from tkinter import * 
import tkinter as tk
from App import main

file = "data.json"
# Top level window 
root = Tk()
frame = ttk.Frame(root, padding=10)
frame.grid()

root.title("Aerogest") 
root.iconbitmap("resources/LOGO.ico")
root.geometry('600x300') 
# Function for getting Input 
# from textbox and printing it  
# at label widget 

    

message = tk.Label(frame, text="Veuillez Introduire les indices d'impact ")
message.grid(column=0, row=0)
Implbl = tk.Label(frame, text="Importance")
Implbl.grid(column=0, row=1)
ImpEaudesc = tk.Label(frame, text="Eau")

# TextBox Creation 
ImpEau = tk.Text(frame, 
                   height = 1, 
                   width = 5) 

ImpEaudesc.grid(column=0, row=2)   # grid dynamically divides the space in a grid
ImpEau.grid(column=1, row=2)
 
ImpBruitdesc = tk.Label(frame, text="Bruit")

# TextBox Creation 
ImpBruit = tk.Text(frame, 
                   height = 1, 
                   width = 5) 
  
ImpBruitdesc.grid(column=0, row=3)   # grid dynamically divides the space in a grid
ImpBruit.grid(column=1, row=3)

ImpAirdesc = tk.Label(frame, text="Air")

# TextBox Creation 
ImpAir = tk.Text(frame, 
                   height = 1, 
                   width = 5) 
  
ImpAirdesc.grid(column=0, row=4)   # grid dynamically divides the space in a grid
ImpAir.grid(column=1, row=4)
ImpEnergiedesc = tk.Label(frame, text="Energie")

# TextBox Creation 
ImpEnergie = tk.Text(frame, 
                   height = 1, 
                   width = 5) 
  
ImpEnergiedesc.grid(column=0, row=5)   # grid dynamically divides the space in a grid
ImpEnergie.grid(column=1, row=5)
ImpDechetsdesc = tk.Label(frame, text="Dechets")

# TextBox Creation 
ImpDechets = tk.Text(frame, 
                   height = 1, 
                   width = 5) 
  
ImpDechetsdesc.grid(column=0, row=6)   # grid dynamically divides the space in a grid
ImpDechets.grid(column=1, row=6)
PlaceHolder1 = tk.Label(frame, text=" ")
PlaceHolder1.grid(column=3, row=1)

PlaceHolder2 = tk.Label(frame, text=" ")
PlaceHolder2.grid(column=3, row=2)
PlaceHolder3 = tk.Label(frame, text=" ")
PlaceHolder3.grid(column=3, row=3)
PlaceHolder4 = tk.Label(frame, text=" ")
PlaceHolder4.grid(column=3, row=4)
PlaceHolder5 = tk.Label(frame, text=" ")
PlaceHolder5.grid(column=3, row=5)
PlaceHolder6 = tk.Label(frame, text=" ")
PlaceHolder6.grid(column=3, row=6)

Maitlbl = tk.Label(frame, text="Maitrise")
Maitlbl.grid(column=5, row=1)
MaitEaudesc = tk.Label(frame, text="Eau")

# TextBox Creation 
MaitEau = tk.Text(frame, 
                   height = 1, 
                   width = 5) 

MaitEaudesc.grid(column=5, row=2)   # grid dynamically divides the space in a grid
MaitEau.grid(column=6, row=2)
 
MaitBruitdesc = tk.Label(frame, text="Bruit")

# TextBox Creation 
MaitBruit = tk.Text(frame, 
                   height = 1, 
                   width = 5) 
  
MaitBruitdesc.grid(column=5, row=3)   # grid dynamically divides the space in a grid
MaitBruit.grid(column=6, row=3)

MaitAirdesc = tk.Label(frame, text="Air")

# TextBox Creation 
MaitAir = tk.Text(frame, 
                   height = 1, 
                   width = 5) 
  
MaitAirdesc.grid(column=5, row=4)   # grid dynamically divides the space in a grid
MaitAir.grid(column=6, row=4)
MaitEnergiedesc = tk.Label(frame, text="Energie")

# TextBox Creation 
MaitEnergie = tk.Text(frame, 
                   height = 1, 
                   width = 5) 
  
MaitEnergiedesc.grid(column=5, row=5)   # grid dynamically divides the space in a grid
MaitEnergie.grid(column=6, row=5)
MaitDechetdesc = tk.Label(frame, text="Dechets")

# TextBox Creation 
MaitDechet = tk.Text(frame, 
                   height = 1, 
                   width = 5) 
  
MaitDechetdesc.grid(column=5, row=6)   # grid dynamically divides the space in a grid
MaitDechet.grid(column=6, row=6)
# Button Creation 
saveButton = tk.Button(frame, 
                        text = "Save") 
saveButton.grid(column=1, row=7)
GenerateReport = tk.Button(frame, 
                        text = "Generer le rapport",  
                        command = main(file))
GenerateReport.grid(column=6, row=7)
# Label Creation 
lbl = tk.Label(frame, text = "") 

quit = tk.Button(frame, text="Quit", command=frame.destroy)

frame.mainloop()