#Reading PDFs

import PyPDF2

pdfFile = open('meetingminutes1.pdf', 'rb')

reader = PyPDF2.PdfFileReader(pdfFile)

mo = reader.numPages
print(mo)

page = reader.getPage(0)#goes to the first page
print(page.extractText())#gets text of first page and displays

for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText())