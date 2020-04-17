class compress():
    def compress(self,string):

        res = ""

        count = 1

        #Add in first character
        res += string[0]

        #Iterate through loop, skipping last one
        for i in range(len(string)-1):
            if(string[i] == string[i+1]):
                if count==1:
                    res += '#'
                count+=1

            else:
                if(count > 1):
                    #Ignore if no repeats
                    res += str(count)
                    res+='#'
                res += string[i+1]
                count = 1
        #print last one
        if(count > 1):
            res += str(count)
        return res
    def decompress(self,string):
        self.res=""
        self.ready = False
        self.num=""
        for i in range(0,len(string)):
            try:
                if(string[i]=='#'and string[i+1]!='#'):
                    self.ready=True
                    #print('aassgf')
                    continue
                else:

                    if self.ready==True and string[i]!='#':
                        self.num=self.num+string[i]
                        #print(self.num)
                    elif (self.ready==True and string[i]=='#'):
                        k=int(self.num)
                        print(k)
                        for j in range(0,k-1):
                            self.res+=self.res[-1]
                        self.ready = False
                        self.num=""
                        continue
                    else:
                        print(string[i])
                        self.res+=string[i]
            except:
                pass
        return self.res

    #sa#10###3#sdsewrdws#8#d#5#ew
if __name__ == "__main__":
    o = compress()
    print(o.compress('saaaaaaaaaa###sdsewrdwssssssssdddddew'))
    print(o.decompress('sa#10#t#3#sdsewrdws#8#d#5#ew'))