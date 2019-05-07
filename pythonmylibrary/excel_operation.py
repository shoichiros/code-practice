import openpyxl

# excel file load and sheetname load
workbook = openpyxl.load_workbook("test.xlsx")
sheetname = workbook.sheetnames[0]
print(sheetname)

# extraction sheet cell
sheet = workbook[sheetname]
cellvalue = sheet["A10"].value
print(cellvalue)
