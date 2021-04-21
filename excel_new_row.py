import openpyxl

workbook = openpyxl.load_workbook("/Users/lojiang/Desktop/zxjt.xlsx")
worksheet = workbook["sheetname"]

for index, row in enumerate(worksheet.rows):
    if index == 0:
        row[6].value = "New Name By Python"
    else:
        if row[3].value == "cell value of row3":
            row[6].value = "BJDB6_BN_L_" + row[4].value + "_POD" + str(int(int((row[0].value)+1)/2)) + "_" + str(int(row[0].value + 1)%2 + 1)
        elif row[3].value == "cell value of row3":
            row[6].value = "BJDB2_BN_L_" + row[4].value + "_POD" + str(int(int((row[0].value)+1)/2)) + "_" + str(int(row[0].value + 1)%2 + 1)

workbook.save(filename='/Users/lojiang/Desktop/zxjt.xlsx')

workbook_new = openpyxl.Workbook()
workbook_new.save(filename='/Users/lojiang/Desktop/zxjt_new.xlsx')
