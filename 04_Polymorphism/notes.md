# Polymorphism in Python

## What is Polymorphism?

Polymorphism means **"having multiple faces"**.

It refers to a concept where the **same thing behaves differently under different situations**.

---

## Main Concepts in Polymorphism

Polymorphism is mainly associated with three concepts:

1. Method Overriding
2. Method Overloading
3. Operator Overloading

---

## 1) Method Overriding

Method overriding occurs in **inheritance**.

When a child class defines a method with the **same name** as a method in the parent class, the child’s method overrides the parent’s method.

When the method is called using a child object, the **child class method executes**.

---

## 2) Method Overloading

Method overloading occurs when a **single class has multiple methods with the same name**, but the methods behave differently depending on the input parameters.

---

### Example Use Case

If a class has two methods named `area`:

* One method takes **radius** as input
* Another method takes **length and breadth** as input

Different `area` methods execute depending on the input provided.

---

### What Problem Does Method Overloading Solve?

Method overloading makes the code:

* Cleaner
* Easier to read
* More intuitive

---

### Important Note

**Method overloading does NOT work in Python.**

---

## 3) Operator Overloading

Operator overloading occurs when the **same operator behaves differently for different data types**.

---

### Example: `+` Operator

* Used with integers → performs addition
* Used with strings → performs concatenation
* Used with lists → performs merging

Thus, the same operator exhibits different behavior depending on the operands.

---

## Summary

* Polymorphism allows the same interface to have different behavior
* Method overriding works through inheritance
* Method overloading improves readability but is not supported in Python
* Operator overloading enables operators to work differently with different data types
