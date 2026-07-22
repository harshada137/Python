# Class and Object in Python

## Introduction

A **class** is a blueprint for creating objects.

An **object** is an instance of a class.

Think of a class as a template and objects as the actual items created using that template.

---

## Class

A class defines:

- Attributes (variables)
- Methods (functions)

---

## Object

An object contains its own data and can use the methods defined inside the class.

---

## Syntax

```python
class ClassName:
    pass

obj = ClassName()
```

---

## Example

```python
class Student:
    name = "Harsha"

student1 = Student()

print(student1.name)
```

**Output**

```
Harsha
```

---

## Key Points

- One class can create multiple objects.
- Objects access class members using the dot (`.`) operator.
- Classes improve code organization and reusability.
