# Decorators in Python

## Introduction

A decorator is a function that adds new functionality to another function without modifying its original code.

Decorators are commonly used for logging, authentication, validation, timing, and access control.

Python uses the `@` symbol to apply decorators.

---

## Syntax

```python
@decorator_name
def function():
    pass
```

---

## Example

```python
def greet_decorator(func):

    def wrapper():
        print("Welcome")
        func()

    return wrapper

@greet_decorator
def greet():
    print("Hello")

greet()
```

**Output**

```
Welcome
Hello
```

---

## Advantages

- Reusable code
- Cleaner implementation
- Separates additional functionality from business logic

---

## Key Points

- Decorators wrap existing functions.
- Applied using the `@` symbol.
- Widely used in Flask, Django, and FastAPI.
