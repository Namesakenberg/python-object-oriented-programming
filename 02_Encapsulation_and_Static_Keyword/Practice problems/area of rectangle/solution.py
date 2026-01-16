class Rectangle:
    def __init__(self):
        self.length = int(input('enter the length of the rectangle' ))
        self.width = int(input('enter the width of the rectangle ' ))

    def area(self):
        return self.length*self.width

    def is_square(self):
        return True if self.length == self.width else False 

r1 = Rectangle()
print(r1.area())
print(r1.is_square())


r2 = Rectangle()
print(r2.area())
print(r2.is_square())