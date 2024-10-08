class Car :
    def __init__(self, model=0, color=0, speed=0) :
        self.model = model
        self.color = color
        self.speed = speed
        
    def drive(self, speed) :
        self.speed = speed
        
    def output(self) :
        print('모델 :', self.model)
        print('색상 :', self.color)
        print('속도 :', self.speed)

myCar = Car()
myCar.output()
print('-' * 20)

myCar = Car('E-Class')
myCar.output()
print('-' * 20)

myCar = Car(color='blue')
myCar.output()
print('-' * 20)

myCar = Car(speed=50)
myCar.output()
print('-' * 20)

myCar = Car('E-Class', speed=50)
myCar.output()
print('-' * 20)

myCar = Car('E-Class', 'blue')
myCar.output()
print('-' * 20)

myCar = Car('E-Class', 'blue', 50)
myCar.output()
print('-' * 20)