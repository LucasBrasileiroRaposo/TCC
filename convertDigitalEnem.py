import PyPDF2
def convertDigitalEnem(nomeArquivo) :
# Abrir o arquivo PDF em modo de leitura binária
    with open( "pdfs/provasDigitais/" + nomeArquivo, 'rb') as arquivo_pdf:

        # Criar objeto leitor do PyPDF2
        leitor_pdf = PyPDF2.PdfReader(arquivo_pdf)

        # Inicializar variável de texto

        redacao = []
        questoesHumanas = {}
        questoesLinguagens = {}
        questoesMatematica = {}
        questoesNatureza = {}
        identificador = 1

        if( "_D2_" in nomeArquivo):
            identificador = 91

        # Loop por todas as páginas do PDF
        for num_pagina in range(len(leitor_pdf.pages)):
            pagina = leitor_pdf.pages[num_pagina]


            if "Questão" in pagina.extract_text():
                if identificador <= 45:
                    questoesLinguagens[identificador] = pagina.extract_text().split("Questão %2d ", identificador)[0]
                    identificador += 1
                elif identificador > 45 and identificador <= 90:
                    questoesHumanas[identificador] = pagina.extract_text().split("Questão %2d - Ciências Humanas e suas Tecnologias", identificador)[0]
                    identificador += 1
                elif identificador > 90 and identificador <=135:
                    questoesNatureza[identificador] = pagina.extract_text().split("Questão %2d - Ciências da Natureza e suas Tecnologias", identificador)[0]
                    identificador += 1
                elif identificador > 135:
                    questoesMatematica[identificador] = pagina.extract_text().split("Questão %2d - Matemática e suas Tecnologias", identificador)[0]
                    identificador += 1

            else:
                if identificador == 46:
                    redacao.append(pagina.extract_text())
                elif (identificador-1  in questoesLinguagens) and identificador <= 45:
                    questoesLinguagens[identificador-1] += pagina.extract_text()
                elif (identificador-1 in questoesHumanas) and identificador > 45 and identificador <= 90:
                    questoesHumanas[identificador-1]  += pagina.extract_text()              
                elif (identificador-1  in questoesNatureza) and identificador <= 135 and identificador > 90:
                    questoesNatureza [identificador-1] += pagina.extract_text()
                elif (identificador-1 in questoesMatematica) and identificador > 135 and identificador <= 180:
                    questoesMatematica[identificador-1]  += pagina.extract_text()     


            # Extrair o texto da página
    
# Imprimir o texto extraído
# print("{} \n {}".format(questoesHumanas,questoesLinguagens))
        print("PROVA DIA 1")
        print(redacao)
        print(questoesLinguagens)
# print(questoesHumanas[49])
        print(questoesHumanas)
        print('\n\n\n')

        print("PROVA DIA 2")
        print(questoesNatureza)
        print(questoesMatematica)