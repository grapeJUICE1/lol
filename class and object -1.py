
class Computer :
    def __init__(self , cpu , ram , storage):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage

    def config(self):
        print(f'Config is {self.cpu} {self.ram}gb ram {self.storage}gb')


com1 = Computer('i5' , 8 , 500)
com2 = Computer('AMD 3' , 12 , 1000)

Computer.config((com1))
Computer.config((com2))

com1.config()
com2.config()
