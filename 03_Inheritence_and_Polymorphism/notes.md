Class reationships :

whenever we make a big systems ,  we would have a lot of classes ,
and these classes will interact with each other.
thus the clasess will have some sort of relationships 

there are 2 types of relationships :  1) aggregation , 2) inheritance


1) Aggregation : 

Aggregation means "has-a" relationship , thus one class owns the other class
eg -> if a class "address" is used in a class "customer" then , customer class owns the address class
thus customer has a adderess . 
such relations are called aggregation.

check the code example.py 

where 
the main class Customer which has a field address , but this address itself is a complex entity 
thus the variable in which address is stored , is a class 
now to have a customer's address in the address variable , 
we have to create an object of the address class , and then pass this object as an parameter to the customer class.

in this way address class is used in the customer class 

thus using aggregation we can pass an object of a class as a prameter to another class.



Definition :
Aggregation : When two classes exist, and one class uses an object of another class (passed from outside), it is called aggregation.
thus a 'has-a' relationship exists 


now , if we make the pincode variable of the address class private , then we wont be able to pass the adderess's object correctly to the Customer class 
but if we make a getter in address and call it in the customer class , we can still get the result.

---------------------------------------------------------------------------------------------------------------------------------------

Inheritence

inspired from real world , inheritance has a parent class and a child class , thus an object created from the child class will be able to access all the methods and attributes of the parent class.

the main objective of inheritence is code resuablility (DRY).

example usecase : 

Consider a online teching-learning platform like Udemy , 
now to implement such system , we have 2 classes 1)Student class 2) Instructor class
in the student class , the methods are : 
Login , Register , enroll , review 
and in the instructor class the methods are :
Login , Register , create_course , reply

now in the above architecture of class , since both student and teacher will Login and Register , the code in both the classes violates the DRY principle and hence it is not a good coding practice 

instead : 
if we create a parent class => User 
and 2 child classes -> Student and Techer 
where student class will only have enroll and review 
and the teacher class will only have create_course and reply

the code becomes clean and properly implemented 