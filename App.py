import numpy as np
import matplotlib.pyplot as plt 
import sys
import json
from fpdf import FPDF 
import time

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
    pdf.set_font('Helvetica', '', 12)
    
    pdf.write(5, words)
    
def main(file):

        f = open(file)

        data = json.load(f)
        print("opened json data")
        imp_dict = data.items()
        imp_list = list(data.items())[1][1]

        mait_list = list(data.items())[0][1]
        print("calculating the results")
        Importance = np.array(list(imp_list.values()))

        Maitrise = np.array(list(mait_list.values()))

        # multiplying the arrays "importance" and "maitrise" to get the final scores
        result = np.multiply(Importance,Maitrise)



        # Opening JSON file
        #f = open('data.json')
        # creating the dataset
        courses = list(data["Importance"].keys())
        values = list(result)
        print("ploting the data")
        
        # creating the bar plot
        plt.bar(courses, values, color ='blue', 
                width = 0.4)
        
        plt.xlabel("Aspects environmentaux")
        plt.ylabel("Indice d'impact")
        plt.title("etat de la gestion environnementale - Mois de Juin")
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
        
main("data.json")