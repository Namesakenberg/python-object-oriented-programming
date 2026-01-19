class Scoop:
    __scoopcount = 0 
    
    def __init__(self,flavour,num_scoops = 1):
        self.flavour = flavour
        self.__price = 0
        self.ordered_scoops = num_scoops
        Scoop.__scoopcount+=num_scoops
    
    def get_price(self):
        return self.__price

    def set_price(self,price):
        self.__price = price
    
    def __str__(self):
        return f"flavour : {self.flavour} ,No of scoops : {self.ordered_scoops},price : {self.__price}"

    @staticmethod
    def sold():
        return Scoop.__scoopcount
    
class Bowl:
    __bowlcount = 0 

    def __init__(self,max_scoops=3):
        self.__scoop_list = [] 
        self.max_scoops = max_scoops
        Bowl.__bowlcount+=1
        self.current_scoops = 0

    def add_scoops(self,*new_scoops):
        for i in new_scoops:
            if self.current_scoops + i.num_scoops <=self.max_scoops:
                self.__scoop_list.append(i)
                self.current_scoops+=i.num_scoops
                print(f'added {i.flavour}')
            else:
                print('bowl is full')
                break

    def get_scoop_list(self):
        return self.__scoop_list
    
    def max_scoops(self):
        if self.bowl_limit>3:
            return False
        return True 
        
    def display(self):
        total =0 
        for i in (self.__scoop_list):
            total+=i.get_price()*i.ordered_scoops
            print(f"flavour {i.flavour} , No of Scoops :{i.ordered_scoops},price : {i.get_price()}")
        print("total price of the bowl is ",total)
    
    @staticmethod
    def sold():
        print("total bowls sold : ",Bowl.__bowlcount)



choco = Scoop('chocolate', 1)
choco.set_price(100)
print(choco)


berry = Scoop('berry', 2)
berry.set_price(120)
print(berry)

vanilla = Scoop('vanilla') # no of scoop parameter not given, will take default value
vanilla.set_price(150)
print(vanilla)
print('--------------------------------------------------------')
bowl1 = Bowl() # max_scoop parameter not given, will take default value
bowl1.add_scoops(choco) # Giving one parameter
bowl1.add_scoops(berry, vanilla) # Multiple
bowl1.display()
print('--------------------------------------------------------')
bowl2 = Bowl()
bowl2.add_scoops(berry)


bowl2.display()
Bowl.sold()