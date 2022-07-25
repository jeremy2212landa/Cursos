from PyPDF2 import PdfFileWriter, PdfFileReader

writer =PdfFileWriter()
file = r"encriptado.pdf"
reader = PdfFileReader(file)

if reader.isEncrypted:
    reader.decrypt("usertest")
    for page in range(reader.numPages):
        writer.addPage(reader.getPage(page))
    
    with open(f"encriptado.pdf","wb") as file:
        writer.write(file)
        file.close()
    print("desbloqueado")
else:
    print("no estaba bloqueado")