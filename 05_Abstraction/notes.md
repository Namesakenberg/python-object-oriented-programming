# Abstraction in Python

## What is Abstraction?

Abstraction means **"hidden"**.

**Example:**
A laptop has many internal circuits and components, but to use a laptop, we do not need to know how those internal parts work.

---

## Abstraction Explained

Abstraction is about:

* Exposing only what is necessary
* Hiding implementation details
* Defining **what** a class must do, not **how** it does it

---

## Abstract Class

An **abstract class** is a class that has **at least one abstract method**.

---

## Abstract Method

An **abstract method** is a method in which **no code is written**.

The implementation of an abstract method is expected to be provided by the child classes.

---

## Example Use Case and Explanation

Consider a class `BankApp`.

This `BankApp` class is a **parent class**, and it has two child classes:

1. WebApp
2. MobileApp

---

### Role of the Parent Class (BankApp)

The `BankApp` class contains common code that is shared by both child classes.

**Example:**

* Database connectivity
* Common banking logic

---

### Making BankApp an Abstract Class

If we make the `BankApp` class an **abstract class**, it enforces a rule on the child classes:

> Before inheriting me, you must implement my abstract methods.

---

### Abstract Method Responsibility

The abstract method represents behavior that:

* Must exist in every child class
* Can have different implementations in different child classes

**Example:**

* Security authentication

---

### How This Works

* `BankApp` (abstract class) declares an abstract method like `security_authentication`
* The abstract method has **no implementation** in `BankApp`
* Both `WebApp` and `MobileApp` must implement this method
* Only after implementing the abstract method can they inherit and use other methods of `BankApp`

---

## Key Takeaway

* `BankApp` → Abstract class
* `security_authentication` → Abstract method
* `WebApp` and `MobileApp` → Concrete child classes

Abstract methods remain empty in the abstract class because their implementation depends on the specific behavior required in each child class.
