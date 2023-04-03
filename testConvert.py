import PyPDF2

# Abrir o arquivo PDF em modo de leitura binária
with open('pdfs/2022_PV_digital_D1_CD1_ingles.pdf', 'rb') as arquivo_pdf:

    # Criar objeto leitor do PyPDF2
    leitor_pdf = PyPDF2.PdfReader(arquivo_pdf)

    # Inicializar variável de texto
    texto = ""

    questoesHumanas = []
    questoesLinguagens = []
    redacao = []
    identificador = 1
    contador = 0

    # Loop por todas as páginas do PDF
    for num_pagina in range(len(leitor_pdf.pages)):
        pagina = leitor_pdf.pages[num_pagina]


        if "Questão" in pagina.extract_text():
            if identificador <= 45:
                questoesLinguagens.append([identificador,pagina.extract_text().split("Questão %2d - Linguagens, Códigos e suas Tecnologias", identificador)])
                identificador += 1
                contador += 1
            elif identificador > 45:
                contador = 0
                questoesHumanas.append([identificador,pagina.extract_text().split("Questão %2d - Ciências Humanas e suas Tecnologias", identificador)])
                identificador += 1
                contador += 1
        else:
            if identificador == 46:
                redacao.append(pagina.extract_text())
            elif  contador <= len(questoesLinguagens) and contador > 0 and identificador <= 45:
                questoesLinguagens[contador-1][1].append(pagina.extract_text())
            elif contador > 0 and contador <= len(questoesHumanas) and identificador > 45:
                questoesHumanas[contador-1][1].append(pagina.extract_text())              


        # Extrair o texto da página
    
# Imprimir o texto extraído
# print("{} \n {}".format(questoesHumanas,questoesLinguagens))
print(redacao)
print(questoesLinguagens)
# print(questoesHumanas)