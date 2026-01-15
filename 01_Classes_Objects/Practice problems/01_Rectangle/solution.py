class Rectangle:
    def __init__(self,len,wid):
        self.length = len
        self.width = wid
    
    def display(self):
        print(f"length : {self.length} , width : {self.width} ,perimeter : {self.perimeter()} , area:{self.area()}") 

    def perimeter(self):
        return 2*(self.length + self.width)
    
    def area(self):
        return self.length*self.width

my_rectangle = Rectangle(3 , 4)
my_rectangle.display()