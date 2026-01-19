class Vehicle:
    def __init__(self,seating):
        self.seating = seating

    def fare(self):
        return self.seating*100

class Bus(Vehicle):
    def __init__(self):
        super().__init__(50)

    
    def fare(self):
        base_fare  = super().fare()
        extra =  (0.1*base_fare)
        return base_fare+extra
        
    
v1 = Vehicle(10)
print(v1.fare())
b1 = Bus()
print(b1.fare())