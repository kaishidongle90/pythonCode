import random
import string
class Guess(object):
    def __init__(self):
        self._li = self.markNum()

    def markNum(self):
        li = []
        while len(li) < 4:
            n =  random.randint(0,9)
            if n not in li:
                li.append(n)
        print li
        return li


    def userInput(self):
        userNum = raw_input('please input four number only int:')
        if userNum.isdigit() and len(set(userNum)) == 4:
            return self.verify(userNum)
#            if result == 0:
#                return 0
        else:
            print 'please input again !!'

    def verify(self,userNum):
        a = 0
        b = 0    
        userNum = userNum
        for i in range(len(userNum)):
            if int(userNum[i]) in self._li:
                if int(userNum[i]) == self._li[i]:
                    a +=1
                else:
                    b +=1
            if a==4:
                return 0
        print ('%dA%dB'%(a,b))

    def run(self):
        times = 0
        while times < 15:
            result = self.userInput()
            if result == 0:
                print 'contruation!!!'
                return 
            else:
                times +=1




if __name__ == "__main__":
    qing = Guess()
    qing.run()
