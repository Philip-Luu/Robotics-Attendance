from openpyxl import load_workbook
from Scanning import*
from datetime import datetime

now = datetime.now()

#Constants
EXCEL_START_VALUE = 5
EXCEL_END_VALUE = 95
EXCEL_RELATIVE_PATH = "Excel Attendance Program\Student Attendance Template - Copy.xlsx"

#Opening File
wb = load_workbook(filename = EXCEL_RELATIVE_PATH)
sheet = wb['Sheet1']


#Getting data from sheet 
Name_ID = []
for row in sheet.iter_rows(min_row=EXCEL_START_VALUE, max_row=EXCEL_END_VALUE):
    Name_ID.append(row[2].value)
    
scanID = True
while scanID:
    wb.save(EXCEL_RELATIVE_PATH)
    validPrompt = False
    Error = False
    MissingPermissionSlip = False
    while validPrompt == False:
        fullID = scanPrompt(Error, MissingPermissionSlip)
        if fullID == "ll":
            exit()
        try:
            index = Name_ID.index(int(fullID)) + EXCEL_START_VALUE
            if index >= 63:
                MissingPermissionSlip = True
            else:
                validPrompt = True
        except (ValueError, TypeError):
            Error = True

    now = datetime.now()
    if sheet["E" + str(index)].value == None:
        sheet['E'+ str(index)] = now.strftime("%H:%M")
    else:
        sheet['F'+ str(index)] = now.strftime("%H:%M")
    
