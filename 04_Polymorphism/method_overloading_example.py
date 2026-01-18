# normal method overloading -> doesnot work in python 
class Shape:
    def area(self,radius):
        return 3.14*radius*radius
    
    def area(self,l,b):
        return l*b
s =Shape()
#s.area(10)

# to implement area as a single function with different inputs we can do :

class Shape1:
    def area(self,a,b=0):
        if b==0:
            return 3.14*a*a
        else:
            return a*b

s1 = Shape1()
print(s1.area(100))
print(s1.area(5,5))