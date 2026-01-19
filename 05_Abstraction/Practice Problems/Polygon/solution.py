from abc import ABC,abstractmethod


class Polygon(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Polygon):
    def __init__(self,length ,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length*self.breadth

class Triangle(Polygon):
    def __init__(self,height,base):
        self.height = height
        self.base = base 
    def area(self):
        return self.base*self.height*0.5

shape1 = Rectangle(10,5)
print(shape1.area())

shape2 = Triangle(3,6)
print(shape2.area())
        

    