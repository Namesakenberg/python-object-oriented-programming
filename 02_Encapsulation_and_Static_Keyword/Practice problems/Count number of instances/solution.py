class Car:
    __count =0
    def __init__(self):
        Car.__count+=1
        print('object created')

    @staticmethod
    def getcount():
        return f"no of instances = {Car.__count}"

maruti = Car()
bmw = Car()
honda = Car()
xyz = Car()
print(honda.getcount())