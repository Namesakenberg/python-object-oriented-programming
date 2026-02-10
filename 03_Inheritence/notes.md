# Class Relationships in Python

## Introduction

Whenever we build big systems, we have many classes, and these classes interact with each other.

Thus, classes have relationships among them.

There are **two main types of relationships**:

1. Aggregation
2. Inheritance

---

## 1) Aggregation

Aggregation represents a **"has-a" relationship**, where one class owns or uses another class.

### Example

If a class **Address** is used inside a class **Customer**, then:

* Customer **has an Address**
* Customer owns the Address

Such relationships are called **aggregation**.

---

### Code Concept (example.py)

The main class `Customer` has a field `address`.

The `address` itself is a complex entity, so the variable storing it is an **object of another class**.

To assign an address to a customer:

1. Create an object of the `Address` class
2. Pass this object as a parameter to the `Customer` class

In this way, the `Address` class is used inside the `Customer` class.

Thus, using aggregation, we can pass an **object of one class as a parameter to another class**.

---

### Aggregation Definition

Aggregation occurs when two classes exist and one class uses an object of another class (passed from outside). This forms a **has-a relationship**.

---

### Important Note on Private Variables

If we make the `pincode` variable of the `Address` class private, we will not be able to access it directly from the `Customer` class.

However, if we create a **getter method** in the `Address` class and call it inside the `Customer` class, we can still access the value.

---

## 2) Inheritance

Inheritance is inspired by the real world. It consists of a **parent class** and a **child class**.

An object created from the child class can access the **non-private attributes and methods** of the parent class.

The main objective of inheritance is **code reusability (DRY principle)**.

---

### Example Use Case

Consider an online teaching-learning platform like **Udemy**.

We initially define two classes:

**Student class methods:**

* Login
* Register
* Enroll
* Review

**Instructor class methods:**

* Login
* Register
* Create course
* Reply

Here, `Login` and `Register` are duplicated, violating the **DRY principle**.

---

### Improved Design Using Inheritance

Create a parent class:

* **User**

Create child classes:

* **Student** → Enroll, Review
* **Teacher** → Create course, Reply

Now, common functionality like `Login` and `Register` exists only in the parent class, resulting in cleaner and reusable code.

---

## What Gets Inherited from the Parent Class?

When a child class is created, it inherits:

1. Constructor
2. Non-private attributes
3. Non-private methods

---

### Important Constructor Behavior

When an object of the child class is created:

* Python first looks for a constructor in the **child class**
* If found, the child constructor is executed
* The parent constructor is NOT executed

If the child class does not have a constructor, Python executes the **parent class constructor**.

---

### Access Restrictions

* A child object **cannot access private attributes or methods** of the parent class directly.

---

## Method Overriding

If a child class has a method with the **same name** as a method in the parent class:

* The child’s method overrides the parent’s method
* When called using a child object, the **child’s method executes**

This behavior is similar to constructor overriding.

---

## `super` Keyword

The `super` keyword is used to call **parent class methods** from the child class.

`super()` is **not meant to access parent attributes directly**.

---

### Using `super()`

From the child class, we can:

* Call parent methods using:

  ```
  super().parent_method()
  ```

* Initialize parent attributes using:

  ```
  super().__init__(arguments)
  ```

After calling the parent constructor, we can define additional child-specific variables.

**Important:**

* `super()` cannot be used from outside the child class

---

## Inheritance Summary

1. A class can inherit from another class
2. Inheritance helps in code reuse
3. Constructors, attributes, and methods are inherited by the child class
4. Parent class has no access to the child class
5. Private properties of the parent are not accessible directly to the child
6. Child class can override parent methods (method overriding)
7. `super()` is used to invoke parent class methods and constructors

---

## Types of Inheritance

1. **Single Inheritance** → One parent and one child
2. **Multilevel Inheritance** → Chain of inheritance (Grandparent → Parent → Child)
3. **Hierarchical Inheritance** → One parent, multiple children
4. **Multiple Inheritance** → Multiple parents for a child (not supported in Java due to ambiguity)
5. **Hybrid Inheritance** → Combination of multiple inheritance types
