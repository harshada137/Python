# Constructor in Python

## Introduction

A constructor is a special method that automatically executes whenever an object is created.

In Python, the constructor is defined using the `__init__()` method.

It is commonly used to initialize object attributes.

---

## Syntax

```python
class ClassName:
    def __init__(self):
        pass
```

---

## Example

```python
class Student:

    def __init__(self, name):
        self.name = name

student = Student("Harsha")

print(student.name)
```

**Output**

```
Harsha
```

---

## Why Use Constructors?

- Initialize object data.
- Avoid writing separate initialization methods.
- Automatically execute during object creation.

---

## Key Points

- Constructor name is always `__init__()`.
- Executes automatically.
- Can accept parameters.
