from tkinter import ttk 
from tkinter import * 
import tkinter as tk
import json
import numpy as np
import matplotlib.pyplot as plt 
import sys
import json
from fpdf import FPDF 
import time
from PIL import Image, ImageTk

file = "data.json"
firstTime = True

def create_letterhead(pdf, WIDTH):
    pdf.image("./resources/letterhead.png", 0, 0, WIDTH)

def create_title(title, pdf):
    
    # Add main title
    pdf.set_font('Helvetica', 'b', 20)  
    pdf.ln(40)
    pdf.write(5, title)
    pdf.ln(10)
    
    # Add date of report
    pdf.set_font('Helvetica', '', 14)
    pdf.set_text_color(r=128,g=128,b=128)
    today = time.strftime("%d/%m/%Y")
    pdf.write(4, f'{today}')
    
    # Add line break
    pdf.ln(10)

def write_to_pdf(pdf, words):
    
    # Set text colour, font size, and font type
    pdf.set_text_color(r=0,g=0,b=0)
    pdf.set_font('Helvetica', '', 13)
    
    pdf.write(5, words)
  
def main():
            file = "data.json"

            f = open(file)

            data = json.load(f)
            print("opened json data")
            imp_dict = data.items()
            imp_list = list(data.items())[1][1]

            mait_list = list(data.items())[0][1]
            
            print (list(imp_list.values()), list(mait_list.values()))
            print("calculating the results")
            Importance = np.array(list(imp_list.values()))

            Maitrise = np.array(list(mait_list.values()))

            # # multiplying the arrays "importance" and "maitrise" to get the final scores
            result = np.multiply(Importance,Maitrise)



            # Opening JSON file
            f = open('data.json')
            # creating the dataset
            courses = list(data["Importance"].keys())
            values = list(result)
            print("ploting the data")
            
            # creating the bar plot
            plt.bar(courses, values, color ='blue', 
                    width = 0.4)
            hfont = {'family':'sans-serif'}
            plt.xlabel("Aspects environmentaux",fontdict=hfont)
            plt.ylabel("Indice d'impact",fontdict=hfont)
            plt.title("Etat de la gestion environnementale | 23 Juin - 30 Juin ",fontdict=hfont)
            plt.savefig('./resources/rapportHebdomadaire.png')
            
            print("creating the PDF")
            # Global Variables
            TITLE = "Rapport de la gestion environnementale"
            WIDTH = 210
            HEIGHT = 297

            # Create PDF
            pdf = FPDF() # A4 (210 by 297 mm)


            '''
            First Page of PDF
            '''
            # Add Page
            pdf.add_page()

            # Add lettterhead and title
            create_letterhead(pdf, WIDTH)
            create_title(TITLE, pdf)

            # Add the generated visualisations to the PDF
            pdf.image("resources/rapportHebdomadaire.png", 5, 130, WIDTH)
            
            # Add some words to PDF
            write_to_pdf(pdf, "de 1 à 5: Acceptable")
            pdf.ln(5)
            write_to_pdf(pdf, "de 6 à 10: Surveillance nécessaire ")
            pdf.ln(5)
            write_to_pdf(pdf, "de 10 à 15: Actions correctives nécessaires")
            pdf.ln(5)
            write_to_pdf(pdf, "de 15 à 25: Inacceptable, actions immédiates requises")
            pdf.ln(5)

            

            
            
            

            # # Add some words to PDF
            # write_to_pdf(pdf, "2. The visualisations below shows the trend of total sales for Heicoders Academy and the breakdown of revenue for year 2016:")

            # Generate the PDF
            pdf.output("rapport_h.pdf", 'F')
            


def Save():
    # 
    file = "data.json"



    result = {"Importance":{"Energie":int(ImpEnergie.get(1.0, "end-1c")),"Air":int(ImpAir.get(1.0, "end-1c")),"Bruit":int(ImpBruit.get(1.0, "end-1c")),"Eau":int(ImpEau.get(1.0, "end-1c")),"Dechet":int(ImpDechets.get(1.0, "end-1c"))}
              ,"Maitrise":{"Energie":int(MaitEnergie.get(1.0, "end-1c")),"Air":int(MaitAir.get(1.0, "end-1c")),"Bruit":int(MaitBruit.get(1.0, "end-1c")),"Eau":int(MaitEau.get(1.0, "end-1c")),"Dechet":int(MaitDechet.get(1.0, "end-1c"))}}
    
    # Serializing json
    json_object = json.dumps(result, indent=4)
 
    with open(file, "w") as outfile:
        outfile.write(json_object)

# Top level window 
root = Tk()
frame = ttk.Frame(root, padding=10)
frame.grid()

root.title("Aerogest") 
root.iconbitmap("resources/LOGO.ico")
root.geometry('600x370') 
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
                        text = "Save",
                        command = Save) 
saveButton.grid(column=1, row=7)
GenerateReport = tk.Button(frame, 
                        text = "Generer le rapport",  
                        command = main)
GenerateReport.grid(column=6, row=7)
# Label Creation 
lbl = tk.Label(frame, text = "") 

quit = tk.Button(frame, text="Quit", command=frame.destroy)


image = Image.open("./resources/letterhead1.png")
photo = ImageTk.PhotoImage(image)

label = Label(root, image = photo)
label.image = photo
label.grid(row=9)

frame.mainloop()

