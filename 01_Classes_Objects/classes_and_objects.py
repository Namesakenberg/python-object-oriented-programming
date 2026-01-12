# implementing the atm machine 

class MyAtm:              # use pascal case while naming a class
    def __init__(self):   # this is a constructor -> this is a place where variables are created for each instance , w
        self.account_number = None
        self.pin = ''
        self.balance = 0


    def menu(self):
        while True:
            input_option = int(input(
                "What would you like to continue with:\n"
                "1: Set PIN\n"
                "2: Change PIN\n"
                "3: withdraw\n"
                "4: Check Balance\n"
                "5: Exit\n"
            ))
        
            if input_option == 1 : 
                self.set_pin()
            elif input_option == 2 :
                self.change_pin()
            elif input_option==3:
                self.withdraw()
            elif input_option == 4:
                self.check_balance()
            elif input_option == 5:
                break
            else:
                print("invalid input")
                
    
    def set_pin(self):
        if len(self.pin) != 0:
            print('a pin is already created to change the current pin , press 2')
            self.menu()
    
        new_pin = input("enter new 4 digit pin : ")
        
        if len(new_pin)!=4 or  any(ch.isalpha() for ch in new_pin)  or any(not ch.isalnum() for ch in new_pin) :
            print('new pin is not valid')
            self.menu()

        else:
            self.pin = new_pin
            print('a pin is created')


    def change_pin(self):

        new_pin = input("enter new 4 digit pin : ")

        if len(new_pin)!=4 or any(ch.isalpha() for ch in new_pin)  or any(not ch.isalnum() for ch in new_pin) :
            print('new pin is not valid')
            

        elif len(self.previous_pins)==0:
            print("no pin set thus creating a new pin :")
            self.pin= self.set_pin()
            print("new pin set ")

        else:
            self.pin = new_pin

        
        

    def withdraw(self):
        pass
    
    def check_balance(self):
        pass
    
    

    # functionality -> set pin , change pin , withdraw , check balance 


obj = MyAtm()
obj.menu()