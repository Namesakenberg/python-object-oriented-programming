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

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

what gets inherited from the parent class when a child class is created : 
1) Constructor
2) Non Private attributes 
3) Non private methods 


**IMPORTANT** -> 
whenever we create an onject of the sutdent class , first it looks for the constructor in the student class , if it finds one , it executes the child's constructor and does not go to the parents constructor ,
but if it does not find the constructor in the child class it will go to the parent class and execute the constructor of the parent class

object of the child class cannot access the private attributes and the methods of the parent class 
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

method overriding : 
if we have a method in the child class , which has the same name as the method in the parent class .
and if we create a child object and execute the method , then the method in the CHILD class will be executed.
this is the thing similar to the previous point :
i.e if parent and child both have constructor in them , then the childs constructor will be executed and the code will never execute the parents constructor.
like-wise if same methods are present in both the child and parent class , then the method in the child class will be executed.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

super keyword : 
the super keyword is used to call the methods of parent class from the child class.
super() is not meant to access the parents attributes

thus from the child class we can do : super().parentmethod , to call the method in the parent class

thus when we are in the child class , we get the parent's initialized attributes by using super().__init__(other variable names) ,
and then if we want new variables for the child class , we can get them 

we cannot use the super keyword from outside the child class   

---------------------------------------------------------------------------------------------------------------------------------------
Inheritance summary:

1) A class can inherit from another class
2) Inheritence helps in code reuse
3) Constructors , attributes and methods get inherited to the child class.
4) The parent has no access to the child class
5) Private properties of the parent are not accessible directly to the child class
6) child class can override the attributes or methods , this is called as method overriding
7) super() is the keyword used to invoke the parent class's methods and constructor

---------------------------------------------------------------------------------------------------------------------------------------

Types of inheritence :

1) Single inheritence -> 1 parent and 1 child , and child inherits from parent
2) Multilevel inheritence -> A chain exists , like grandfather->father->child ,child can inherit from all the ancestors
3) Hierarchical inheritence -> One parent and multiple children 
4) Multiple Inheritence -> is not present in java (due to ambiguity), multiple parents for a child 
5) Hybrid Inheritence -> Combination of the above cases