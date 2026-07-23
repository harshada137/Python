# Methods in Python

## Introduction

Methods are functions defined inside a class.

They describe the behavior of an object.

Every instance method must include `self` as its first parameter.

---

## Types of Methods

1. Instance Method
2. Class Method
3. Static Method

Among these, instance methods are the most commonly used.

---

## Example

```python
class Student:

    def greet(self):
        print("Welcome!")

student = Student()

student.greet()
```

**Output**

```
Welcome!
```

---

## Key Points

- Methods define object behavior.
- Instance methods use `self`.
- Methods are called using objects.
