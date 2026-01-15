# create abd view 2d coordinate
import math
class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def dist(self,other):
        distance = math.sqrt((other.x-self.x)**2 + (other.y-self.y)**2)
        return distance
    
    def dist_from_origin(self):
        distance = math.sqrt((0-self.x)**2 + (0-self.y)**2)
        return distance
    
    def __str__(self):
        return f"x,y = {self.x},{self.y}"

class line:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b 
        self.c = c 
        # ax+by+c 
                               
    def check_point_on_line(self,point):
        # y = mx+c 
        if self.a*point.x + self.b*point.y + self.c ==0:
            return True
        return False
    
    def dist_btw_point_line(self,point):
        return (abs(self.a*point.x + self.b*point.y+self.c) / math.sqrt(self.a**2+self.b**2))
    
    def __str__(self):
        return f"{self.a}x + {self.b}y + {self.c}=0"

p1 = point(2,3)
p2 = point (3,2)
print(p1.dist_from_origin())
print(p1.dist(p2))

l1 = line(1,1,-2)
p3 = point(1,1)

print(l1.check_point_on_line(p3))
print(l1.dist_btw_point_line(p1))