class Bill:
    def __init__(self,amount):
        self.__amount = amount
    
    def get_amount(self):
        return self.__amount
    
    def pay(self):
        pass

class card_payment(Bill):
    def __init__(self, amount):
        super().__init__(amount)
    
    def pay(self):
        print(f'amount {self.get_amount()} paid using card')

class cash_payment(Bill):
    def __init__(self, amount):
        super().__init__(amount)
    
    def pay(self):
        print(f'amount {self.get_amount()} paid using cash')

p1 = cash_payment(100)
p1.pay()

p2= card_payment(1000)
p2.pay()

