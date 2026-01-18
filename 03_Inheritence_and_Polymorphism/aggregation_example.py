class Customer:
    def __init__(self,name,num,address):
        self.name = name
        self.number = num
        self.address = address
    
    def get_details(self):
        return f"name:{self.name} , contact:{self.number},building:{self.address.apt_name},area:{self.address.area},city{self.address.city},pin : {self.address.get_pincode()}"
    
    def edit_profile(self):
        self.number=int(input('enter the new contact number'))
        self.address.update_address()

class address:
    def __init__(self,apt_name,area,city,pin_code):
        self.apt_name = apt_name
        self.area = area
        self.city = city
        self.__pincode = pin_code
    
    def get_pincode(self):
        return self.__pincode
    
    def update_address(self):
        self.apt_name = (input('enter new building name '))
        self.area = (input('enter new area '))
        self.city = (input('enter new city '))
        self.__pincode=int(input('enter new pincode'))

 
home = address('chitradurga','kothrud','Pune',411038)
c1 = Customer('sid',10,home)
print(c1.get_details())
c1.edit_profile()
print(c1.get_details())



# here the main class Customer , has a field address , but this address itself is a complex entity 
# thus the variable in which address is stored , is a class 
# now to have a customer's address in the address variable , 
# we have to create an object for the address class , and then pass this object as an parameter to the customer class

# now if we make pincode variable of the address class as private then we cannot pass the object of address class to the customer class
# but if we make a getter in address and call it in the customer class , we can still get the result