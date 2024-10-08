class Member : 
    def __init__(self, name=None, age=0) :
        self.__name = name
        self.__age = age
        
    def getName(self) :
        return self.__name
    
    def setName(self, name) :
        self.__name = name
        
    def getAge(self) :
        return self.__age
    
    def setAge(self, age) :
        self.__age = age
        
    def say(self) :
        print('이름 :', self.__name)
        print('나이 :', self.__age)

member = Member()
member.say()
print('-' * 20)

member.setName('홍길동')
member.setAge(25)
member.say()
print('-' * 20)


