from openpyxl import Workbook

    #Line 7  how to create a new empty workbook.
    #Lines 13 & 14  how to add data to specific cells.
    #Line 17 how to save the spreadsheet 

filename = "hello_world.xlsx"

workbook = Workbook()

sheet = workbook.active

sheet["A1"] = "hello"
sheet["B1"] = "world!"


workbook.save(filename=filename)
