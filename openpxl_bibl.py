import openpyxl

book = openpyxl.open('razb_uch.xlsx',read_only=True)

sheet = book.active

print(sheet[5][1].value)
for row in range(1,sheet.max_row + 1):
    autor = sheet[row][0].value
    name = sheet[row][1].value
    year = sheet[row][2].value
    rating = sheet[row][3].value
    print(row, autor, name, year, rating)
