class words_filter():
    def __init__(self,str1):
                    self.lis3 = ""
                    for i in str1:
                        if i !='\n' and i !='\t':
                            self.lis3=self.lis3+i
                        else:
                            pass

    def output(self):


        return self.lis3