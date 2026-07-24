# Inheritance in Python

## Introduction

Inheritance allows one class to inherit the properties and methods of another class.

The existing class is called the **Parent (Base) Class**, while the new class is called the **Child (Derived) Class**.

Inheritance promotes code reusability.

---

## Benefits

- Reuse existing code.
- Reduce duplication.
- Extend existing functionality.

---

## Example

```python
class Animal:

    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    pass

dog = Dog()

dog.sound()
```

**Output**

```
Animal makes sound
```

---

## Types of Inheritance

- Single
- Multiple
- Multilevel
- Hierarchical
- Hybrid

---

## Key Points

- Child class inherits parent members.
- Existing functionality can be reused.
- Supports code extensibility.
