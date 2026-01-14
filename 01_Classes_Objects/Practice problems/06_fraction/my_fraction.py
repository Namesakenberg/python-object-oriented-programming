# as an use case of OOP, creating my own FRACTION data type here .
# in pyhton fraction is not present as an data type 

class Fraction():
    def __init__(self,num,deno):
        if deno == 0 : 
            raise ValueError("denominator cannot be zero")
        self.num = num
        self.deno = deno
    
    def __str__(self):
        return f"{self.num} / {self.deno}"
    
    def addition(self,other):
        ans_num = (self.num*other.deno) + (other.num*self.deno)
        ans_deno = self.deno*other.deno
        return Fraction(ans_num , ans_deno)
    
    def subtraction(self,other):
        ans_num = (self.num*other.deno) - (other.num*self.deno)
        ans_deno = self.deno*other.deno
        return Fraction(ans_num , ans_deno)
    
    def multiplication(self,other):
        ans_num = (self.num*other.num)
        ans_deno = self.deno*other.deno
        return Fraction(ans_num , ans_deno)
    
    def divide(self,other):
        ans_num  = (self.num * other.deno)
        ans_deno = (self.deno* other.num)
        return Fraction(ans_num , ans_deno)
    
f1 = Fraction(2,3)
f2 = Fraction(3,2)
print(f1.addition(f2))
print(f1.subtraction(f2))
print(f1.multiplication(f2))
print(f1.divide(f2))


