#start to build a working file

from openpyxl import load_workbook
import openpyxl.styles

wb = load_workbook(filename='chart.xlsx')  # file to open must be in the same dirctory or must switch to get the file
ws1 = wb['Defects'] #selects the tab
ws1.sheet_properties.tabColor = "1072BA" #Colors must be aRGB hex values
c = ws1['C2'] = 2345 #changed value in cell
# openpyxl.worksheet.worksheet.Worksheet.insert_rows()
# openpyxl.worksheet.worksheet.Worksheet.insert_cols()
# openpyxl.worksheet.worksheet.Worksheet.delete_rows()
# openpyxl.worksheet.worksheet.Worksheet.delete_cols()
ws1.insert_cols(5,9)
ws1.delete_cols(6, 3)#deletes columns


print(ws1)

wb.save('New_Chart.xlsx')


