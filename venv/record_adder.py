import openpyxl


class record_add():
    #def __init__(self,given_str1,given_str2,given_str3):              # ################## foor camera #########
    def __init__(self, given_str1, given_str2):
        ctr=0
        given_str1=str(given_str1)
        given_str2 = str(given_str2)
        ##################### for cameraa#################
        '''given_str3=str(given_str3)

        s1=given_str3[0:23000]
        s2=given_str3[23000:]
        print('gone',len(list(given_str3)))'''
        wb = openpyxl.load_workbook("datafile.xlsx")
        sheet = wb['Sheet1']  # wb.get_sheet_names())
        # ############# for camera
        '''wb2 = openpyxl.load_workbook("datafile2.xlsx")
        sheet2 = wb2['Sheet1']  # wb.get_sheet_names())'''
        columnvalue=1
        for i in range(1, sheet.max_row + 1):
            if ((sheet.cell(row=i, column=columnvalue).value == given_str1)):
                ctr = 1

                cell = sheet.cell(row=i, column=1)
                cell.value = given_str1.strip()

                cell = sheet.cell(row=i, column=2)
                cell.value = given_str2.strip()
                #################### for camera##################################
                '''cell = sheet.cell(row=i, column=3)
                cell.value = s1'''
                ############## for camera ################
                '''cell = sheet2.cell(row=i, column=2)
                cell.value = s2
                cell = sheet2.cell(row=i, column=1)
                cell.value = given_str1'''

                break
            else:
                pass
        if (ctr == 0):

            for i in range(1, sheet.max_row + 2):
                # print('maxrow',sheet.max_row)

                if str(sheet.cell(row=i, column=1).value) == 'None':
                    cell = sheet.cell(row=i, column=1)
                    cell.value = given_str1.strip()

                    cell = sheet.cell(row=i, column=2)
                    cell.value = given_str2.strip()
                    ############################ for camera
                    '''cell = sheet.cell(row=i, column=3)
                    cell.value = s1
                    
                    cell = sheet2.cell(row=i, column=2)
                    cell.value = s2
                    cell = sheet2.cell(row=i, column=1)
                    cell.value = given_str1'''
                    break


        else:
            pass
        wb.save("datafile.xlsx")
        '''wb2.save(("datafile2.xlsx"))''' ############ for camera #############
    def get(self):
        return self.output