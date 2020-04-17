import openpyxl


class record_availability_checker():
    def __init__(self,given_str):
        ctr=0
        given_str=str(given_str)
        given_str=given_str.strip()

        wb = openpyxl.load_workbook("datafile.xlsx")
        sheet = wb['Sheet1']  # wb.get_sheet_names())
        wb2 = openpyxl.load_workbook("datafile2.xlsx")
        sheet2 = wb2['Sheet1']  # wb.get_sheet_names())
        columnvalue=1
        for i in range(1, sheet.max_row + 1):
            if ((sheet.cell(row=i, column=columnvalue).value == given_str)):
                ctr = 1

                self.output = sheet.cell(row=i, column=2).value
                self.output1 = sheet.cell(row=i, column=3).value

                break
            else:
                pass
        for i in range(1, sheet2.max_row + 1):
            if ((sheet2.cell(row=i, column=columnvalue).value == given_str)):
                ctr = 1

                self.output2 = sheet2.cell(row=i, column=2).value


                break
            else:
                pass
        if (ctr == 0):

            self.output = ""

    def get(self):
        return self.output
    def get1(self):
        return self.output1
    def get2(self):
        return self.output2