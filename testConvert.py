import PyPDF2

# Abrir o arquivo PDF em modo de leitura binária
with open('2022_PV_digital_D1_CD1_ingles.pdf', 'rb') as arquivo_pdf:

    # Criar objeto leitor do PyPDF2
    leitor_pdf = PyPDF2.PdfReader(arquivo_pdf)

    # Inicializar variável de texto
    texto = ""

    questoesHumanas = []
    questoesLinguagens = []
    contador = 90

    # Loop por todas as páginas do PDF
    for num_pagina in range(len(leitor_pdf.pages)):
        pagina = leitor_pdf.pages[num_pagina]

        # contador += 1
        aux2 = ""

        if "Questão" in pagina.extract_text():
            if contador <= 45:
                questoesLinguagens.append(pagina.extract_text().split("Questão %2d - Linguagens, Códigos e suas Tecnologias", contador))
                contador -= 1
            elif contador > 45:
                questoesHumanas.append(pagina.extract_text().split("Questão %2d - Ciências Humanas e suas Tecnologias", contador))
                contador -= 1
            # questoesHumanas.append(pagina.extract_text().split("Questão 01 - Linguagens, Código e suas Tecnologias"))
        # Extrair o texto da página
    
# Imprimir o texto extraído
print("{} \n {}".format(questoesHumanas,questoesLinguagens))
print(contador)