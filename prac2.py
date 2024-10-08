class Address :
    def __init__(self, name="", number="", address=""):
        self.name = name
        self.number = number
        self.address = address
        
    def showAddress(self):
        print("이름 : %s\n전화 : %s\n주소 : %s" 
              %(self.name, self.number, self.address))

a1 = Address("홍길동","010-1234-5678","서울시 강남구 역삼동")
a1.showAddress()