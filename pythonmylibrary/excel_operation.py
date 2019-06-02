import openpyxl


work_book = openpyxl.load_workbook("test.xlsx")
sheet_name = work_book.sheetnames[0]
print(sheet_name)

sheet = work_book[sheet_name]
cell_value = sheet["A10"].value
print(cell_value)
