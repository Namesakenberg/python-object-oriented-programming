class Phone:
    def __init__(self,RAM,storage,camera):
        print('inside Phones constructor')
        self.__ram = RAM
        self.storage = storage
        self.camera = camera
    
    def get_details(self):
        return f"specs : {self.__ram} ,{self.storage},{self.camera}"

class SmartPhone(Phone):
    def __init__(self, RAM, storage, camera,price,os):
        print('inside smartphones constructor')
        super().__init__(RAM, storage, camera)  # using super we call the parents constructor , thus from the child constructor the parent constructor is called 
        self.price =price
        self.os = os 

m35 = SmartPhone(16,256,100,20000,'snapdragon')