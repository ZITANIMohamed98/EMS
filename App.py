import numpy as np
import matplotlib.pyplot as plt 
import sys
import json
from fpdf import FPDF 
import datetime

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

        imp_dict = data.items()
        imp_list = list(data.items())[1][1]

        mait_list = list(data.items())[0][1]

        Importance = np.array(list(imp_list.values()))

        Maitrise = np.array(list(mait_list.values()))

        # multiplying the arrays "importance" and "maitrise" to get the final scores
        result = np.multiply(Importance,Maitrise)



        # Opening JSON file
        #f = open('data.json')
        # creating the dataset
        courses = list(data["Importance"].keys())
        values = list(result)
        
        fig = plt.figure(figsize = (10, 5))
        
        # creating the bar plot
        plt.bar(courses, values, color ='green', 
                width = 0.4)
        
        plt.xlabel("Aspects environmentaux")
        plt.ylabel("Indice d'impact")
        plt.title("etat de la gestion environnementale - Mois de Mai")
        plt.savefig('./resources/rapportHebdomadaire.png')
        
        # Global Variables
        TITLE = "Monthly Business Report"
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

        # Add some words to PDF
        write_to_pdf(pdf, "1. The table below illustrates the annual sales of Heicoders Academy:")
        pdf.ln(15)

        

        # Add the generated visualisations to the PDF
        pdf.image("resources/rapportHebdomadaire.png", 5, 200, WIDTH*4)
        pdf.ln(10)
        

        # Add some words to PDF
        write_to_pdf(pdf, "2. The visualisations below shows the trend of total sales for Heicoders Academy and the breakdown of revenue for year 2016:")

        # Generate the PDF
        pdf.output("rapport_hebdomadaire"+str(datetime.datetime.now())+".pdf", 'F')