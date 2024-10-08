class Car :
    def __init__(self, model, color, speed) :
        self.model = model
        self.color = color
        self.speed = speed
        
    def drive(self, speed) :
        self.speed = speed
        
    def output(self) :
        print('모델 :', self.model)
        print('색상 :', self.color)
        print('속도 :', self.speed)
 
myCar = Car('E-Class', 'blue', 0)
myCar.output()
print('-' * 20)

myCar.drive(50)
myCar.output()
