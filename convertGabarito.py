import PyPDF2

with open('pdfs/2022_GB_impresso_D1_CD1.pdf', 'rb') as arquivo_pdf:

    leitor_pdf = PyPDF2.PdfReader(arquivo_pdf)

    pagina = leitor_pdf.pages[0]

    print(pagina.extract_text())