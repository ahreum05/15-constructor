# 기본값
# => 정수 : 0
# => 실수 : 0
# => 문장열 : ""
# => bool : False
class Triangle :
    def __init__(self, b=0, h=0):
        self.base = b
        self.height = h
        
    def setTriangle(self, b, h) :
        self.base = b
        self.height = h
    
    def getArea(self) :
        return self.base * self.height / 2

t1 = Triangle(45, 7)
print("삼각형의 넓이 :", t1.getArea())

t2 = Triangle()
t2.setTriangle(5, 12)
print("삼각형의 넓이 :", t2.getArea())