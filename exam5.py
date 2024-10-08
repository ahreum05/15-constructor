from random import sample

class Lotto :
    def __init__(self) :
        self.m = 0
        self.buyNum = 0
        
    def inputBuyNum(self) :
        self.buyNum = int(input('구매횟수를 입력하세요 : '))
        print()
        
    def outputResult(self) :
        print('{:2} {:2} {:2} {:2} {:2} {:2}'.format(*self.m))
        
    def selectLotto(self) :
        for i in range(self.buyNum) :
            self.m = sample([a for a in range(1, 46)], 6)
            self.m.sort()
            self.outputResult()
            
lotto = Lotto()
lotto.inputBuyNum()
lotto.selectLotto()


