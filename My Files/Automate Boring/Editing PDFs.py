#editing PDFs

import PyPDF2

pdf1File = open('meetingminutes1.pdf', 'rb')
pdf2File = open('meetingminutes2.pdf', 'rb')
reader1 = PyPDF2.PdfFileReader(pdf1File)
reader2 = PyPDF2.PdfFileReader(pdf2File)
writer = PyPDF2.PdfFileWriter()

for pageNum in range(reader1.numPages):#copies the whole document to an object
    page=reader1.getPage(pageNum)
    writer.addPage(page)

for pageNum in range(reader2.numPages):
    page=reader2.getPage(pageNum)
    writer.addPage(page)

outputfile = open('combinedminutes.pdf', 'wb')#can only combin existing PDF Files/pages into another PDF
#file cannot create new from code the write function only appends to a document pdf files
writer.write(outputfile)
outputfile.close()
pdf1File.close()
pdf2File.close()