import os
import PyPDF2

class convertSpecialEnem:
    def convertSpecialEnem(file):




        
directory = "pdfs/specialExams"
arquivos = os.listdir(directory)
for arquivo in arquivos:
    # print(arquivo)
    convertSpecialEnem.convertSpecialEnem(arquivo)



