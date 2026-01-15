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

thus the variable has been renamed 

now when we change the value of this private variable from outside , the changes are made to the variable which does not exist as the name has changed when we made the private variable.
the code will completely run on the new name.


thus changes made to __pin from outside of the class wont affect the program as the program does not run on __pin , instead it runs on _Atm__pin

thus even if the value of the __attribute is changed , nothing will happen as code runs on _classname__varaiblename.


BUT
**if we change the value of private variable using the name in format _classname__varaiblename from outside the class , we can change the value of the private varaible**

thus in python , nothing is truly private. 
*because python is an programming language made for adults.*

