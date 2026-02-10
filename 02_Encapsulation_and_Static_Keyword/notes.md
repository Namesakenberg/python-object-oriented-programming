# Encapsulation in Python

## Before Encapsulation

### What is an Instance Variable?

Variables which have different values for different objects are called **instance variables**.

Thus, in a constructor, all the variables that have `self` in them are instance variables because they hold different values for different objects.

---

## Encapsulation — One of the Core Pillars of OOP

### What is the Need for Encapsulation?

Once a class is created, it will have some attributes and methods.

When we create an object:

```
obj1 = classname()
```

and type `obj1.`, we see a dropdown containing all the methods and attributes.

After creating an object, we can change the value of the attributes/variables from outside the class, which can cause problems.

Thus, to ensure safety and prevent attributes from being changed externally, we make the variables **private**.

In Python, we use `__` in front of the variable name to make it private.

**Example:**

```
self.__pin
```

We can even make methods private by using `__` in front of their names.

Once a variable/method has been made private, we do not see these in the dropdown after `obj1.`.

---

## What Happens Internally When Creating a Private Variable?

Whenever we make a private variable, in memory the name of the variable changes and is updated in the format:

```
_classname__variablename
```

**Example:**

```
self.__pin  →  _Atm__pin
```

Thus, the variable has been renamed.

When we try to change the value of this private variable from outside, the changes are made to a variable that does not exist because the name has changed.

The code runs on the new name.

Therefore, changes made to `__pin` from outside the class will not affect the program because the program runs on `_Atm__pin`.

Even if the value of the `__attribute` is changed, nothing will happen since the code runs on `_classname__variablename`.

---

## BUT — Important Note

**If we change the value of a private variable using the name in the format `_classname__variablename` from outside the class, we CAN change the value of the private variable.**

Thus, in Python, nothing is truly private.

*Because Python is a programming language made for adults.*

---

## Accessibility of Private Variables

When a private variable is created, it is not accessible outside the class, but it can still be used inside the class.

Other methods of the same class can access the private variable.

To allow controlled access from outside the class, we use **getter and setter methods**.

* **Getter:** Used to read/return the value of the private variable.
* **Setter:** Used to update/modify the value of the private variable.

Using a setter, we can still change the value of attributes — but not directly. Instead, we do it through a method.

Inside the setter method, we apply necessary checks and constraints to provide controlled access.

---

## Encapsulation Definition

Encapsulation is an OOP concept in which variables are made private to prevent direct modification from outside the class, and controlled access to those variables is provided through methods such as getters and setters.

---

## Collection of Objects

We can create multiple objects and store them inside a:

* List
* Tuple
* Dictionary

---

## Static Keyword

If we want to set up a counter in our class (for example, `accountnumber` in an ATM class) which increments by 1 whenever a new account is created, we cannot implement this using an instance variable.

Why?

Because if an instance variable is used, the count will start from 0 for every object.

Thus, we need a **static variable**.

---

### Static vs Instance Variable

* **Static variable:** Same value for all objects.
* **Instance variable:** Different value for each object.

We declare a static variable **outside the constructor but inside the class**, and when calling it, we use the format:

```
classname.variablename
```

* While using a static variable → use the **class name**.
* While using an instance variable → use the **object name (`self`)**.

---

## Can Static Variables Be Changed from Outside?

Yes, static variables can be changed from outside the class.

To avoid this, we make the static variable private and use getters and setters for controlled access.

If we create a getter method for a static variable, it will return:

```
classname.variablename
```

Even if we do not pass `self` as a parameter to such methods, it is completely okay.

However, while accessing such methods, we should use the **class name** and not the variable name.

Such methods are called **static methods**, and we use the **static method decorator**.
