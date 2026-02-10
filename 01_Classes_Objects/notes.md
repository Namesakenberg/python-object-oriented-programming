# Classes and Objects in Python

## OOP (Object-Oriented Programming)

**What problem does OOP solve?**

The normal code we write is general code (top to bottom), but when we use OOP concepts, we write more specific code. Thus, OOP helps us move from generality to specificity.

**OOP gives the programmer the ability to create their own data types — this is the main advantage of OOP.**

---

## What is OOP?

OOP is a programming paradigm (way of writing code) using which a programmer can create their own data types.

Besides this, important concepts like **abstraction, inheritance, encapsulation, and polymorphism** help in writing structured code.

---

## Important OOP Principles

1. Classes and Objects
2. Polymorphism
3. Encapsulation
4. Inheritance
5. Abstraction

---

## 1) Class

### What is a Class in OOP?

A class is a blueprint. It is a set of rules which must be followed by each object belonging to that class.

**Example:**

Consider a course. There will be some structure/schedule of the course which will be followed throughout and obeyed by each student.

* **Class:** Course
* **Objects:** Students enrolling in the course

**Other Example:**

* **Class:** Car
* **Objects:** WagonR, Swift, G-Wagon, etc.

All the data types in Python are built-in classes, and when we create a variable using any datatype, Python considers it an object of that class.

---

## What Does a Class Contain?

A class contains two things:

1. **Data / Properties / Attributes**
2. **Functions / Behavior (Methods)**

**Example — Class: Course**

**Attributes:**

* Curriculum
* Instructor
* Fees
* Exam schedule

**Methods / Functions:**

* Attending lectures
* Giving exams
* Asking doubts

---

## Object

An object is an instance of a class.

* For class **Course → Object is Student**
* For class **Car → Object is WagonR**, etc.

---

## Basic Implementation Example

If we create a new list:

```
nums = []
```

Then `nums` is an object of the class `list`.

When we type `nums.` we see options like `append`, `clear`, `copy`, `sort`, etc.
These are the **methods/attributes** of that class.

**Creating an object:**

```
objectname = classname()
```

**Accessing a method:**

```
object.MethodName()
```

---

## Can a Class Be Executed Without an Object?

A class cannot be executed unless we execute the object belonging to that class.

**Example:**
A course will only be conducted if students enroll in it. Without students, the properties and attributes of the course are useless.

Thus, without an object, the class cannot be executed.

---

## Types of Classes in Python

1. Built-in classes
2. User-defined classes

---

## Constructor

A constructor is a special function where variables are created for each instance.

We do **not** need to call the constructor manually. When we create an object for the class, the constructor is automatically called.

---

## Methods vs Functions

All functions present inside a class are called **methods**, while functions outside a class are called **functions**.

**Example:**

```
L = [1, 2, 3]
len(L)      # function
L.append(4) # method
```

`len(L)` is a function because when we type `L.` we do not see the option `length`.

---

## Class Representation Diagram

![Class Diagram](image.png)

---

## Magic Methods / Dunder Methods

Magic methods are special methods. Every magic method has a “superpower”.

**Naming format:**

```
_methodname_
```

**Example:**

* Constructor → `_init_`

Its superpower is that it is implemented automatically when an object is created.

---

## Detailed Discussion on Constructor

### 1) What is a Constructor?

A constructor is a method, but a special one. It is triggered automatically when the object is created.

---

### 2) Benefit of Constructor

Since the code inside the constructor runs whenever a new instance is created:

* Basic attributes required for every object can be written once.
* Prevents repetition → follows the **DRY principle**.
* Control is maintained over critical application components.

**Example:** Configuration-related code such as connecting to a database.

---

### 3) Can We Rename a Constructor?

No. The only name for the constructor in Python is `_init_`.

---

### 4) Parameterized vs Non-Parameterized Constructors

**Non-parameterized constructor:**

```
def _init_(self):
```

**Parameterized constructor:**

```
def _init_(self, numerator, denominator):
```

---

## Concept of `self`

`self` is a default parameter passed to every method present in the class.

**Examples:**

```
def withdraw(self)
def change_pin(self)
```

When calling methods internally:

```
self.withdraw()
self.change_pin()
```

In constructors:

```
self.pin
self.balance
```

---

## Golden Rule of Object-Oriented Programming

A class has attributes (pin, balance) and methods (withdraw, set_pin, change_pin). These things can **ONLY** be accessed by the object of the class.

Technically, one method of a class should not call another directly.

However, `self` gives us the freedom to access another method from the same class.

**Example:**

```
self.confirm_pin
```

---

## What is `self` Actually?

`self` is the object of the class — the current instance.

When we create an object, the memory location of `self` and the object is the same.

---

## What Happens If We Don’t Use `self`?

If `self` is not written as a parameter while creating a method and we call that method using an object, we get:

```
TypeError: method() takes 0 positional arguments but 1 was given
```

This happens because Python automatically passes the object to the method.

---

## Dynamic Attribute Creation

Once an object is created, it can access all attributes and methods of the class.

**But we can also create or update attributes from outside the class.**

* Attributes can be added dynamically.
* Methods **cannot** be added dynamically.

---

## Concept of Reference Variables

### What is a Reference Variable?

When creating an object:

```
p1 = Person()
```

We say `p1` is an object, but in reality, `p1` is a variable that stores the **address of the object** created by `Person()`.

Thus, `p1` is a reference variable.

---

### Key Points

1. Reference variables hold references to objects.
2. Objects can be created without reference variables.
3. An object can have multiple reference variables.
4. Assigning a new reference variable does NOT create a new object.

**Example:**

```
p1 = Person()
p2 = p1
```

Both `p1` and `p2` point to the same memory location.

If one changes, the other reflects the change — this behavior can be risky.

---

## Mutability of User-Defined Objects

Objects of user-defined classes are **mutable**.

Whenever changes are made, they are performed **in place on the same memory address.**
