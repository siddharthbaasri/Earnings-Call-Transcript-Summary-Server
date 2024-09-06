from PyPDF2 import PdfReader, PdfWriter

def getMergedPDF(PdfList):
    writer = PdfWriter()
    for file in PdfList:
        with open(file, 'rb') as file:
            reader = PdfReader(file)
            for num in range(0, len(reader.pages)):
                writer.add_page(reader.pages[num])

    with open('C:\\Projects\\Siddharth\\BaasriSiddharth.pdf', "wb") as fp:
        writer.write(fp)
    
    
def get_text(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        for page_number in range(0, len(reader.pages)):
            text += reader.pages[page_number].extract_text() + " "
    return text[:min(len(text), 200000)]
