from random import randint
import sys

class PlusGame:
    def __init__(self):
        self.cnt = 0        # 맞춘 문제 개수
        self.tot = 0        # 점수
        self.cont = False   # 계속 진행여부 
    
    def input(self) : 
        self.cnt = 0
        
        for i in range(5):
            num1 = randint(10, 99)
            num2 = randint(10, 99)
            result = num1 + num2
            
            # _ : 변수값을 사용안할 때 사용하는 변수명
            for _ in range(2):
                answer = int(input(f"[{i+1}] {num1} + {num2} = "))
                if answer == result:
                    print("딩동뎅")
                    self.cnt += 1
                    break
                else:
                    print("틀렷따..")
            print()
    
    def output(self) : 
        self.tot = self.cnt * 20    # 점수 계산
        print(f"당신은 총 {self.cnt}문제를 맞추어서 총 {self.tot}점 입니다.")
    
    def is_continue(self) : 
        cho = input("계속하시겠습니까?(Y/N): ")
        if cho == "y" or cho == "Y":
            self.cont = True
        else :
            self.cont = False


