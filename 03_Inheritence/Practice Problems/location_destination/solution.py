class Point:
    def __init__(self,x,y):
        self.x = x 
        self.y = y 
    def __str__(self):
        return f"x,y = {self.x},{self.y}"
        
class Location:
    def __init__(self,location ,destination):
        self.location = location
        self.destination = destination

    def reflect(self):
        reflected_x = self.destination.x
        reflected_y = -self.destination.y
        print(f"Reflected Destination: ({reflected_x}, {reflected_y})")
loc = Point(2, 3)
dest = Point(4, 5)

place = Location(loc, dest)
place.reflect()
