classes and objects in python


OOP is Object oriented programming 

what problem does OOP solve ? 
-> the normal code we write is genral code (top to bottom),but when we use OOP concepts , we write more specific code ,thus OOP helps us to move from generality to specificity.

* OOP gives the programmer an ability to create its own data types -> this is important and is the main advantage of oop.

thus,

what is OOP ?
-> OOP is a programming paradigm (way of writing code) using which a programmer can create his own data types.
besides this , many other important concepts like abstraction , inheritance , encapsulation and polymorphism , help writing structerd code. 

IMPORTANT OOP principles : 
1> Classes and Objects
2> polymorphism
3> Encapsulation
4> Inheritance
5> Abstraction

----------------------------------------------------------------------------------------------------------------------------------
1> Class : 

what is Class in OOP? 
-> Class is a blueprint, it is a set of rules which are created , which must be followed by each object belonging to that class

eg -> consider there  is a course , there will be some structure/schedule of the course which will be followed throughout the course , and will be obeyed by each student in the course. 
thus,course is the class and each student enrolling in the course will be an object of that class.

other examples ->
class : car , objects : wagonR , swift , G wagon etc..

all the data types in python are built in classes , and when we create a variable using any datatype , python considers it as an object of that class 

---------------------------------------------------------------------------------------------------------------------------------
Class contains 2 things -> 
1> The data or property or attributes of the class 
2> Functions or behaviour of that class 

eg =>
for a class : course , 
the attributes are -> the curriculum , instructor , fees , exam schedule etc
the methods / functions are -> attending lectures , giving exams, asking doubts etc 

--------------------------------------------------------------------------------------------------------------------------------
Object -> 
Object is an instance of the class , 
for an class course: object is student , like wise for a class car the object is wagonR etc.

--------------------------------------------------------------------------------------------------------------------------------
basic implementation example -> 
if we create a new list "nums" , then nums will be the object of the class list, thus whenever we print "nums." , 
we see a dropdown of muliple options like append , clear , copy , sort etc 
these options are nothing but the methods / attributes of that class.

to create an object of a class we use the format -> objectname = classname()
to implement the attribute we use the format -> object.MethodName()
----------------------------------------------------------------------------------------------------------------------------------
a class cannot be executed , unless we do not execute the object beloning to that particular class.
eg -> a course will only be conducted if students enroll in it , if no student enrolls , then the properties and attributes of that course is useless . 
thus without an object the class cannot be executed
----------------------------------------------------------------------------------------------------------------------------------
In python there are 2 types of clasess -> 1) built in and 2) user defined classes 
----------------------------------------------------------------------------------------------------------------------------------
constructor ->it is a special function where variables are created for each instance
we do not need to call the constructor of a class manually , when we create an object for the class the constructor is called.

----------------------------------------------------------------------------------------------------------------------------------
Methods vs Fucntion : 
All the functions present inside the Class are called as METHODS and the functions present outside of the class are called as 
functions 

eg -> L = [1,2,3]
len(L) -> is a function 
L.append(4) -> is a method 

len(L) is a function because , when we do L. we do not see the option length
---------------------------------------------------------------------------------------------------------------------------------
any created class can be represented by a diagram 

![alt text](image.png)
----------------------------------------------------------------------------------------------------------------------------------
MAGIC METHODS / Dunder Methods 
magic methods are special methods , every magic methods has a super power , magic method's naming format is :
_methodname_ 

eg-> constructor -> _init_ is a magic method and its superpower is that it can be implemented without calling , it can be impemented by creating an object of the class 
----------------------------------------------------------------------------------------------------------------------------------
Detailed discussion on constructor : 
1) What is a constructor
-> Constructor is a method , but it is a special one , and we do not need to call it , it is triggered when the object is called.

2) what is the benifit of constructor ? 
-> since the code inside the constuctor is implemented whenever new instance is created , all the basic attributes and other basic implementations which are must for every object can be wirtten in the constructor , thus whenever we create a new object we do not need to repeat the things evertime , thus we follow the DRY principle.
Also all those things in the application whose control we dont want to give to the user will be present in the constructor . 

eg -> configuration related code (eg-> connecting to database)

3) we cannot rename constructor in python , the only name for the constructer in python is _init_


4) parameterized constructor and non parameterized constructors-> 
constructors which do not take any other parameter as input other than self is called as a non parameterized constructor 
and 
constructors which take other parameters as input other than self are the parameterized constructors 

eg - > 
non parameterized :  def _init_(self):

parameterized : def _init_(self,numerator,denominator)

----------------------------------------------------------------------------------------------------------------------------------
Concept of self :

self is a default parameter passed to every method present in the class eg -> def withdraw(self) , def change_pin(self) etc
also while calling methods , we need self everytime , eg : self.withdraw() , self.change_pin().
also in the constructor , when we declare somethings , we use self. eg -> self.pin , self.balance etc 

Golden Rule of Object Oriented Programming : 
Class has attributes (pin,balance) and methods(withdraw , setpin , change pin) , all these things can ONLY be accessed by the object of the class .
thus according to this golden rule : one method of the class cannot even call another method of the same class.
but in code , we can do so , 
thus self gives us this freedom to acess another method from the same method of the class . thus in the code , we used 
self.confirm_pin to access the confirm_pin method from other methods of the same class.

self actually is the object of the class. 
when we create an object the location of the self and the object is same , this proves that self is nothing but the current instance i.e the current object 

if incase we do not write self as a parameter while creating a method , when we create an object and call that method , we get an error saying : TypeError: method() takes 0 positional arguments but 1 was given
this error occurs because , whenever an method is called , python's functionality will naturally pass the object to the function , and since self is not present in the method , we get the above error.
----------------------------------------------------------------------------------------------------------------------------------
we know that once an object of a class is created , it can access all the attributes and methods of the given class , and if we call a method which does not exist in the class , we get an error. 

**But we can also create or update an attribute for the object from outside of the class.**

so we can add attributes dynamically , but not call the methods which dont exist.

this behaviour of updating or creating from outside the class , is only valid for the attributes of the class and not for the methods.
----------------------------------------------------------------------------------------------------------------------------------
Concept of Reference variables: 

1> What is a reference variable ? 
-> 
while creating an object for a class , we usually do :
variable = Classname()  eg -> p1 = person().

now when we do :  p1 = person() , we say that p1 is an object of class person.
but in reality , p1 is a variable which just stores the address of the object created by calling  person().

thus : p1 is just a reference variable

thus , if we just call person() , an object will still be created at some address in the memory. 

and when we do p1 = person() , p1 stores the address where the object is created in the memory.
so we can also do : 
p1 = person()       -> p1 stores the address of the object created
p2 = p1             -> p2 equals p1 , thus both point to the same object in the memory

thus if p2 is changed , p1 will also get changed and vice versa , as they both point to the same thing in the memory.
this behaviour can be risky 

Thus: 
1) Reference variables hold references to the objects 
2) We can create objects without reference variables as well
3) An object can have multiple reference variables 
4) assigning a new reference variable to an existing object does not create a new object


objects of user defined classes are mutable , whever any changes are made , they are made in place on the same address