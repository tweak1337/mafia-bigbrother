from datetime import datetime, timedelta
import openpyxl

file = 'story.xlsx'
wb = openpyxl.load_workbook(file)
sheet = wb.worksheets[0]
row_count = sheet.max_row
range_cells = sheet['B2':f'B{row_count}']
insult_list = []
for row in range_cells:
    for cell in row:
        insult_list.append(cell.value)

print(insult_list)