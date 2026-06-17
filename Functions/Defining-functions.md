# Defining Functions in Python


## Introduction

A function is a reusable block of code that performs a specific task. Functions help make code modular, readable, and easier to maintain by avoiding repetition.

## Why Use Functions?

* Improve code reusability
* Reduce code duplication
* Enhance readability
* Simplify debugging and maintenance
* Enable modular programming

---

## Basic Function Syntax

```python
def function_name(parameters):
    """Optional docstring"""
    # Function body
    return value
```

### Example

```python
def greet():
    print("Hello, World!")

greet()
```

**Output:**

```text
Hello, World!
```

---

## Functions with Parameters

Parameters allow functions to accept input values.

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Harsha")
```

**Output:**

```text
Hello, Harsha!
```

---

## Functions with Multiple Parameters

```python
def add(a, b):
    result = a + b
    print(result)

add(10, 20)
```

**Output:**

```text
30
```

---

## Return Statement

The `return` statement sends a value back to the caller.

```python
def add(a, b):
    return a + b

sum_result = add(10, 20)
print(sum_result)
```

**Output:**

```text
30
```

---

## Default Parameters

Default values are used when an argument is not provided.

```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()
greet("Harsha")
```

**Output:**

```text
Hello, Guest!
Hello, Harsha!
```

---

## Keyword Arguments

Arguments can be passed using parameter names.

```python
def student(name, age):
    print(f"Name: {name}, Age: {age}")

student(age=22, name="Harsha")
```

**Output:**

```text
Name: Harsha, Age: 22
```

---

## Positional Arguments

Arguments are assigned based on their order.

```python
def multiply(a, b):
    return a * b

print(multiply(5, 4))
```

**Output:**

```text
20
```

---

## Variable-Length Arguments

### *args

Used to pass multiple positional arguments.

```python
def total(*numbers):
    return sum(numbers)

print(total(10, 20, 30, 40))
```

**Output:**

```text
100
```

### **kwargs

Used to pass multiple keyword arguments.

```python
def display_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

display_info(name="Harsha", age=22, city="Mumbai")
```

**Output:**

```text
name: Harsha
age: 22
city: Mumbai
```

---

## Function Scope

### Local Variables

Variables defined inside a function are accessible only within that function.

```python
def example():
    x = 10
    print(x)

example()
```

### Global Variables

Variables defined outside a function can be accessed globally.

```python
x = 100

def show():
    print(x)

show()
```

**Output:**

```text
100
```

---

## Lambda Functions

A lambda function is a small anonymous function.

### Syntax

```python
lambda arguments: expression
```

### Example

```python
square = lambda x: x ** 2

print(square(5))
```

**Output:**

```text
25
```

---

## Nested Functions

Functions can be defined inside other functions.

```python
def outer():
    def inner():
        print("Inside Inner Function")

    inner()

outer()
```

**Output:**

```text
Inside Inner Function
```

---

## Docstrings

Docstrings describe the purpose of a function.

```python
def add(a, b):
    """
    Returns the sum of two numbers.
    """
    return a + b
```

Access the docstring:

```python
print(add.__doc__)
```

---

## Type Hints

Type hints improve code readability and assist with static analysis.

```python
def add(a: int, b: int) -> int:
    return a + b

print(add(5, 10))
```

---

## Best Practices

1. Use descriptive function names.
2. Keep functions small and focused on a single task.
3. Use docstrings for documentation.
4. Return values instead of printing whenever possible.
5. Use type hints for better readability.
6. Avoid excessive global variables.
7. Follow PEP 8 naming conventions.

---

## Complete Example

```python
def calculate_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle.

    Args:
        length (float): Length of the rectangle.
        width (float): Width of the rectangle.

    Returns:
        float: Area of the rectangle.
    """
    return length * width

area = calculate_area(10.5, 5.0)
print(f"Area: {area}")
```

**Output:**

```text
Area: 52.5
```

---

## Summary

Python functions are fundamental building blocks that allow developers to organize code into reusable, maintainable, and efficient units. Understanding parameters, return values, scope, lambda expressions, and best practices is essential for writing clean and professional Python programs.

---

### Key Takeaways

* Functions are defined using the `def` keyword.
* Parameters allow data to be passed into functions.
* The `return` statement sends data back to the caller.
* `*args` and `**kwargs` support flexible argument handling.
* Lambda functions provide concise anonymous functions.
