import openpyxl


class recordoverride():
    def __init__(self,given_str1,given_str2):

        given_str1=str(given_str1)
        given_str2 = str(given_str2)
        wb = openpyxl.load_workbook("datafile.xlsx")
        sheet = wb['Sheet1']  # wb.get_sheet_names())
        print('recordoverride str 1 = ',given_str1)
        for i in range(1, sheet.max_row + 1):
            if ((sheet.cell(row=i, column=1).value == given_str1)):

                cell = sheet.cell(row=i, column=1)
                cell.value = given_str1
                cell = sheet.cell(row=i, column=2)
                cell.value = given_str2
                print('vlae override')
                # time.sleep(2.5)

                break
            else:
                pass

        wb.save("datafile.xlsx")
