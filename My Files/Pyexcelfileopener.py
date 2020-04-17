from openpyxl import load_workbook
workbook = load_workbook(filename="reviews-sample1.xlsx")

print("Names are ",workbook.sheetnames)
#print("workbook type is", type(workbook))
sheet = workbook.active
#print("Sheet type is: ",type(sheet))


sheet.title
print(sheet.title)
sheet["A1"].value
#print(sheet["A1"].value)
#print(sheet["F10"].value)
#print(sheet.cell(row=10, column=6).value)
#print(sheet["A1:C2"])
#for row in sheet.iter_rows(min_row=1,
                           #max_row=2,
                           #min_col=1,
                           #max_col=3,
                           #values_only=True):
    #print(row)
#testing for different values to see different results from sample data
for value in sheet.iter_rows(min_row=2,
                             min_col=4,
                             max_col=7,
                             values_only=True):
    print(value)

for value in sheet.iter_rows(min_row=2,
                             min_col=4,
                             max_col=8,
                             values_only=True):
    print(value)
