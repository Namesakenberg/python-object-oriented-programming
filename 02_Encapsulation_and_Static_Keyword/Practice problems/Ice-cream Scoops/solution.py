class Scoop:
    __scoopcount = 0 
    
    def __init__(self, flavour, num_scoops=1):
        self.flavour = flavour
        self.__price = 0
        self.ordered_scoops = num_scoops
        Scoop.__scoopcount += num_scoops
    
    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price
    
    def __str__(self):
        return f"Flavour: {self.flavour}, Scoops: {self.ordered_scoops}, Price: {self.__price}"

    @staticmethod
    def sold():
        return Scoop.__scoopcount
    

class Bowl:
    __bowlcount = 0 

    def __init__(self, max_scoops=3):
        self.__scoop_list = [] 
        self.max_scoops = max_scoops
        self.current_scoops = 0
        Bowl.__bowlcount += 1

    def add_scoops(self, *new_scoops):
        for i in new_scoops:
            if self.current_scoops + i.ordered_scoops <= self.max_scoops:
                self.__scoop_list.append(i)
                self.current_scoops += i.ordered_scoops
                print(f"{i.flavour} added")
            else:
                print("Bowl is full")
                break
        
    def display(self):
        total = 0 
        for i in self.__scoop_list:
            total += i.get_price() * i.ordered_scoops
            print(f"Flavour: {i.flavour}, Scoops: {i.ordered_scoops}, Price: {i.get_price()}")
        print("Total price of the bowl:", total)
    
    @staticmethod
    def sold():
        return Bowl.__bowlcount

choco = Scoop('chocolate', 1)
choco.set_price(100)
print(choco)

berry = Scoop('berry', 2)
berry.set_price(120)
print(berry)

vanilla = Scoop('vanilla')  # default scoops = 1
vanilla.set_price(150)
print(vanilla)

print('--------------------------------------------------------')

bowl1 = Bowl()  # default max_scoops = 3
bowl1.add_scoops(choco)
bowl1.add_scoops(berry, vanilla)
bowl1.display()

print('--------------------------------------------------------')

bowl2 = Bowl()
bowl2.add_scoops(berry)
bowl2.display()

print("Total scoops sold:", Scoop.sold())
print("Total bowls sold:", Bowl.sold())