import openpyxl


class itemslist():
    def __init__(self):

        self.output = list()
        wb = openpyxl.load_workbook("datafile.xlsx")
        sheet = wb['Sheet1']  # wb.get_sheet_names())
        columnvalue=1
        for i in range(1, sheet.max_row + 1):

            if sheet.cell(row=i, column=1).value == None:
                pass
            else:
                self.output.append(sheet.cell(row=i, column=1).value)
        try:
            self.output.remove(None)
        except:
            pass
        print(self.output)

    def get(self):
        return self.output