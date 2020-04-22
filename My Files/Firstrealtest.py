from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference
    #Line 7  how to create a new empty workbook.
    #Lines 13 & 14  how to add data to specific cells.
    #Line 17 how to save the spreadsheet 

filename = "hello_world.xlsx"

workbook = Workbook()

sheet = workbook.active

#insert sample data
rows = [
    ["PART TYPE #", "GOOD", "BAD"],
    [1,	6,	3],
    [2,	10,	2],
    [3,	15,	9],
    [4,	6,	4],
    [5,	36,	16],
    [6,	0,	0],
    [7,	4,	1],
    [8,	10,	5],
    [9,	13,	6],
    [10, 23, 12],
    [11, 13, 7],
    [12, 0,	0],
    [13, 25, 10],
    [14, 22, 6],
    [15, 16, 5],
    [16, 9,	4],
    [17, 14, 5],
    [18, 15, 7],
    [19, 0,	0],
    [20, 24, 6],
    [21, 6,	2],
    [22, 2,	1],
    [23, 12, 6],
    [24, 0,	0],
    [25, 4,	1],
    [26, 0,	0],
]
for row in rows:

    sheet.append(row)

chart = BarChart()
data = Reference(worksheet=sheet,
                 min_row=1,
                 max_row=27,
                 min_col=2,
                 max_col=3)

chart.add_data(data, titles_from_data=True)
sheet.add_chart(chart, "E2")
chart.x_axis.title = "PART TYPE #"
chart.y_axis.title = "QA COUNT(per Part Type #)"

workbook.save("Partschart.xlsx")

#workbook.save(filename=filename)
