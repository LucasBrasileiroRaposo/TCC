import os
import convertDigitalEnem
diretorio = "pdfs/provasDigitais"
arquivos = os.listdir(diretorio)
for arquivo in arquivos:
    # print(arquivo)
    convertDigitalEnem.convertDigitalEnem(arquivo)