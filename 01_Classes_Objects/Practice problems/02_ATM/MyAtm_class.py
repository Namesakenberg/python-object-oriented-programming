# implementing the atm machine 

class MyAtm:              # use pascal case while naming a class
    __accountnumber = 99
    def __init__(self):   # this is a constructor -> this is a place where variables are created for each instance , w

        print('ENTER DETAILS TO CREATE AN ACCOUNT')
        self.__accountnumber = MyAtm.__accountnumber
        self.__accountnumber+=1
        
        print('Set your pin')
        new_pin = input("enter a 4 digit pin : ")

        # validity check
        if len(new_pin)!=4 or not new_pin.isdigit():
            print('Invalid PIN')
            # add exception for invalid pin 

        self.__pin = new_pin
        print('PIN created successfully')


        initial_balance = int(input('add an amount greater than 1000 as initial balance : '))
        if initial_balance<1000:
            return
        else:
            self.__balance = initial_balance
    
        
    # getter and setters for balance
    def get_balance(self):
        return self.__balance

    def set_balance(self,new_value):
        self.__balance = new_value


    @staticmethod       # this is an static method 
    def get_account_number():   # we do not pass , self here as a parameter as the static variable is at class level 
        return MyAtm.__accountnumber     # thus we call this static variable using class name and not object name 

    def menu(self):
        while True:
            input_option = int(input(
                "What would you like to continue with:\n"
                "1: Change PIN\n"
                "2: withdraw\n"
                "3: Check Balance\n"
                "4: Exit\n"
            ))
        
            if input_option == 1 :
                self.change_pin()
            elif input_option==2:
                self.withdraw()
            elif input_option == 3:
                self.check_balance()
            elif input_option == 4:
                break
            else:
                print("invalid input")
                

    
    def confirm_pin(self):
        # confirm old pin 
        check_pin = str(input('Enter the current PIN : '))
        if check_pin == self.__pin:
            return True 
        else:
            print('incorrect pin')
            return False 

    def change_pin(self):
        if not self.confirm_pin():
            return
    
        new_pin = str(input("enter new 4 digit pin : "))

        if len(new_pin)!=4 or not new_pin.isdigit() :
            print('new pin is not valid')
            return
        if new_pin == self.__pin:
            print('New PIN cannot be same as old PIN')
            return

        self.__pin = new_pin
        print('PIN changed successfully')
                    

    def withdraw(self):
        if not self.confirm_pin():
            return
        need = int(input('enter the amount to be withdrawn'))
        if need > self.__balance:
            print('insufficient balance')
            return
        if need <= 0:
            print('invalid amount')
            return
        else:
            self.__balance-=need
            print(f'withdrawn {need} remaining balance is {self.__balance}')

    
    def check_balance(self):
        if not self.confirm_pin():
            return  
        else:
            print(f"current balance : {self.__balance}")
    
    

    # functionality -> set pin , change pin , withdraw , check balance 


obj = MyAtm()  
print(obj.get_balance())
obj.set_balance(10000000000000)
print("updated balance")
print(obj.get_balance())

print(obj.get_account_number())
print(MyAtm.accountnumber)