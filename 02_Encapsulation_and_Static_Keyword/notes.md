before encapsulation ->

what is an instance variable : 
the variables which have different values for different object , is called as an instance variable.
Thus , in an constructor , all the variables are having self in them are instance variables , as they hold different values for 
different objects

----------------------------------------------------------------------------------------------------------------------------------
Encapsulation -> One of the core pillars of OOP

What is the need of encapsulation / what problem does encapsulation solve ?
-> 
once a class is made , it will have some attributes and methods in it. 
now when we create an object , eg -> obj1 = classname()  , and do "obj1." we can see a dropdown containing all the methods and attributes,
now after creating an object we can chage the value of the attributes / variables from outside of the class which can cause a lot of problem . 
thus to ensure safety and not allow attributes to be changed from outside of the class , we make the variables PRIVATE.
 
in python we use __ infront of the variable name to make it private. 

eg -> self.__pin

we can even make methods private by using __ infornt of its name.

once a variable / method has been made private , we do not see these in the dropdown after "obj1.".

----------------------------------------------------------------------------------------------------------------------------------
what happens internally on creating a private variable  

whenever we make a private variable , in memory the name of the variable changes , and is updated in the format : _classsname__variablename

thus self.__pin is now _Atm__pin

thus the variable has been renamed. 

now when we change the value of this private variable from outside , the changes are made to the variable which does not exist as the name has changed when we made the private variable.
the code will completely run on the new name.


thus changes made to __pin from outside of the class wont affect the program as the program does not run on __pin , instead it runs on _Atm__pin

thus even if the value of the __attribute is changed , nothing will happen as code runs on _classname__varaiblename.


BUT
**if we change the value of private variable using the name in format _classname__varaiblename from outside the class , we can change the value of the private varaible**

thus in python , nothing is truly private. 
*because python is an programming language made for adults.*
----------------------------------------------------------------------------------------------------------------------------------
when a private variable is created its accessibility is not available outside the class, but inside the class we will can use the variable.
so the other methods of the same class can use the private variable. 

thus to allow controlled access from outside the class , we use *getter and setter methods* 

getter is used to read / return the value of the private variable
setter is used to update./ modify the value of the oprivate variable 


using setter we can still change the value of the attributes , but not directly , we do it through a method.
thus inside setter method we apply necessary checks and constraints , which would give the controlled access
---------------------------------------------------------------------------------------------------------------------------------
Encapsulation definition : 
Encapsulation is an OOP concept in which variables are made private to prevent direct modification from outside the class, and controlled access to those variables is provided through methods such as getters and setters.

----------------------------------------------------------------------------------------------------------------------------------

Collection of objects : 
we can create multiple objects and put them into a list / tuple / dictionary

----------------------------------------------------------------------------------------------------------------------------------

Static Keyword : 
                            
if we want to set up an counter in our class , eg -> acountnumber in the atm class
which is expected to be incremented by 1 as new account is created .
thus we will setup this variable in the constructor , so that whenever a new object is created the account number will be incremented by 1 

now we cannot implement this using an instance variable because , if an instance variable is used , for every object the count will be starting from 0 

thus we need a static variable.
the value of the static variable is same for all the objects and for instance variables it is different for each object

we declare a static variable outside the class.
also , when we have to call the static variabe we do it in the format : classname.variablename

while using the static variable we use the class-name , and while using the instance variable , we use the object name (self).

We can also change the value of static variable from outside the class,
thus to avoid this , we make the static variable private , and use getter and setter if we want to use it in a controlled manner.

thus if we make a getter method for an static variable , it will return classname.variablename , thus even if we do not pass "self" as a parameter to such method , it is completely okay. 
but while accessing such methods , we should access them using the class name and not the variable name .
and such methods are called as static method , and we use static method decorator 