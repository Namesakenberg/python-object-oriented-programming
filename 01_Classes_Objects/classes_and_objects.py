# implementing the atm machine 

class MyAtm:              # use pascal case while naming a class
    def __init__(self):   # this is a constructor -> this is a place where variables are created for each instance , w

        print('ENTER DETAILS TO CREATE AN ACCOUNT')

        acc_no = str(input('enter a 3 digit account number : '))
        if len(acc_no)!=3 or not acc_no.isdigit():
            print('Invalid entry')
            # add exception here for invalid entry
            
        self.account_number = acc_no

        print('Set your pin')
        new_pin = input("enter a 4 digit pin : ")

        # validity check
        if len(new_pin)!=4 or not new_pin.isdigit():
            print('Invalid PIN')
            # add exception for invalid pin 

        self.pin = new_pin
        print('PIN created successfully')


        initial_balance = int(input('add an amount greater than 1000 as initial balance : '))
        if initial_balance<1000:
            print('enter amount greater than 1000')
            return
        self.balance = initial_balance
        
        
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
        if check_pin == self.pin:
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
        if new_pin == self.pin:
            print('New PIN cannot be same as old PIN')
            return

        self.pin = new_pin
        print('PIN changed successfully')
                    

    def withdraw(self):
        if not self.confirm_pin():
            return
        need = int(input('enter the amount to be withdrawn'))
        if need > self.balance:
            print('insufficient balance')
            return
        if need <= 0:
            print('invalid amount')
            return
        else:
            self.balance-=need
            print(f'withdrawn {need} remaining balance is {self.balance}')

    
    def check_balance(self):
        if not self.confirm_pin():
            return  
        else:
            print(f"current balance : {self.balance}")
    
    

    # functionality -> set pin , change pin , withdraw , check balance 


obj = MyAtm()
obj.menu()