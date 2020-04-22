from openpyxl import load_workbook

# Start by opening the spreadsheet and selecting the main sheet
workbook = load_workbook(filename="testdata2.xlsx")
sheet = workbook.active

# Write what you want into a specific cell
sheet["A1"] = "CONTRACT"
sheet["B1"] = "CLIN"
sheet["C1"] = "DESCRIPTION"
sheet["D1"] = "DATE"
sheet["E1"] = "OPEN?"
# Save the spreadsheet
workbook.save(filename="testdata2_append.xlsx")