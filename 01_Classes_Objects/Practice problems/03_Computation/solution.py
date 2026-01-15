class computation:
    def __init__(self):
        self.n = int(input('enter the number'))
    
    @staticmethod  # static method to get all the divisors 
    def listDiv(n):
        if n==0:
            return []
        Ldiv = []
        for i in range(1,n+1):
            if n%i==0:
                Ldiv.append(i)
        return Ldiv

    def listDivPrim(self):
        LPDiv=[]
        if self.n==0:
            return []
        for i in range(1,self.n+1):
            if self.n%i==0 and self.isPrime(i):
                LPDiv.append(i)
        return LPDiv

    def Factorial(self):
        '''
        if self.n==1 or self.n==0:
            return 1 
        return self.n*(self.Factorial(self.n-1))
        '''
        x = self.n
        if x == 0 :
            return 1 

        ans = 1 
        while x>0:
            ans*=x
            x-=1
        return ans
    
    
    def naturalSum(self):
        ans = 0
        for i in range(self.n+1):
            ans+=i
        return ans 
    
    def isPrime(self, x):
        if x <= 1:
            return False
        for i in range(2, x):
            if x % i == 0:
                return False
        return True

    def testPrime(self):
        if self.n ==0 or self.n==1:
            return False 
        for i in range(2,self.n):
            if self.n%i==0:
                return False
        return True
    
    def testPrims(self,other):
        if self.n == 0 or other.n==0:
            return False 
        for i in range(2,min(self.n,other.n)):
            if self.n %i==0 and other.n%i==0:
                return False
        return True 
    
    def tableMult(self):
        for i in range(1,11):
            print(self.n*i)
    
    def allTablesMult(self):
        x = self.n
        for i in range(1,x+1):
            print(' ')
            for j in range(1,11):
                print(j*i)



obj = computation()
print("factorial : ",obj.Factorial())
print("natural sum : ",obj.naturalSum())
obj.tableMult()
obj.allTablesMult()
print(obj.testPrime())
obj2  = computation()
print("test primes : ",obj.testPrims(obj2))