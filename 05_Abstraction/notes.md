Abstarction => Means hidden

eg-> 
our laptop , which has a lot of internal circuits but to use a laptop we dont need to know the underlying things 

Abstraction is about:
Exposing only what is necessary and hiding implementation details, while defining what a class must do, not how it does it.

Abstract class -> a class which has alteast one abstract method
Abstract method -> methods in which no code is written



example usecase and explanation : 

consider we have a class bankApp , this bank app is the parent class , and it will have 2 child classes: 
1) the web_app 
2) the mobile_app

now the bankApp contains the code (eg-> database connectivity), which will be used by both the child classes.
now if we make the BankApp class an abstract class , then  , the BankApp class will say to the child classes that : 
before inheriting me , implement the abstract method .
here **abstract method will be some method which must be implemented by both the child classes before inheriting the methods from the parent class** (eg->securituy authentication)

thus in this case , 
the BankApp class is an Abstract class ,  which has the abstract method (security authentication) 
thus for the child classes web app and the mobile app , abstract method must be implemented, then only the methods of the BankApp can be inherited 

abstract method will be empty in the abstract class , as the implementation of the abstract method can be different in the child classes 