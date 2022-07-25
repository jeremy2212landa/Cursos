from PyPDF2 import PdfFileWriter, PdfFileReader

writer =PdfFileWriter()
file = r"/home/kattaleya/Documentos/develop/py/Python_course/scripts/test.pdf"
reader = PdfFileReader(file)

for page in range(reader.numPages):
    writer.addPage(reader.getPage(page))

writer.encrypt("usertest")

with open (f"encriptado.pdf", "wb") as file:
    writer.write(file)
    file.close()
print (f"archivo encriptado")