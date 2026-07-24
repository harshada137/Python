# Encapsulation in Python

## Introduction

Encapsulation is the process of combining data and methods into a single unit (class) while restricting direct access to certain data.

It helps protect object data from accidental modification.

Python commonly uses private attributes with double underscores (`__`).

---

## Example

```python
class Student:

    def __init__(self):
        self.__marks = 95

student = Student()

print(student._Student__marks)
```

**Output**

```
95
```

---

## Advantages

- Data security
- Better code organization
- Prevents unauthorized access

---

## Key Points

- Private variables use `__variable`.
- Data should be accessed through methods whenever possible.
