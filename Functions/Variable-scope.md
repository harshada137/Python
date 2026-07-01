# Variable Scope in Python

## Introduction

Variable scope defines the region of a program where a variable can be accessed. Python determines the visibility and lifetime of variables based on where they are created. Understanding variable scope helps avoid naming conflicts and makes programs easier to maintain.



## Types of Variable Scope

Python follows the **LEGB Rule** to resolve variable names:

| Scope | Description |
|--------|-------------|
| **L - Local** | Variables declared inside a function. Accessible only within that function. |
| **E - Enclosing** | Variables in the local scope of an enclosing (nested) function. |
| **G - Global** | Variables declared outside all functions. Accessible throughout the module. |
| **B - Built-in** | Names that are predefined by Python, such as `print()`, `len()`, and `range()`. |



## 1. Local Scope

A variable created inside a function is called a **local variable**. It exists only while the function is executing.

### Example

```python
def greet():
    message = "Hello, World!"
    print(message)

greet()
```

**Output**

```text
Hello, World!
```

> The variable `message` cannot be accessed outside the `greet()` function.



## 2. Global Scope

A variable declared outside any function belongs to the **global scope** and can be accessed anywhere in the program.

### Example

```python
language = "Python"

def display():
    print(language)

display()
print(language)
```

**Output**

```text
Python
Python
```



## 3. Modifying Global Variables

To modify a global variable inside a function, use the `global` keyword.

### Example

```python
count = 10

def update():
    global count
    count = 20

update()
print(count)
```

**Output**

```text
20
```



## 4. Enclosing Scope (Nested Functions)

When one function is defined inside another, the inner function can access variables from the outer function.

### Example

```python
def outer():
    message = "Welcome"

    def inner():
        print(message)

    inner()

outer()
```

**Output**

```text
Welcome
```

---

## 5. Built-in Scope

Python provides several built-in functions that are available everywhere.

### Example

```python
numbers = [5, 10, 15]

print(len(numbers))
print(max(numbers))
```

**Output**

```text
3
15
```



## The LEGB Rule

When Python encounters a variable, it searches in the following order:

1. **Local Scope**
2. **Enclosing Scope**
3. **Global Scope**
4. **Built-in Scope**

If the variable is not found in any of these scopes, Python raises a `NameError`.



## Best Practices

- Use **local variables** whenever possible.
- Minimize the use of **global variables**.
- Use descriptive variable names.
- Avoid modifying global variables unless necessary.
- Keep variable scope as limited as possible for better readability and maintainability.



## Theory Notes

- Variable scope determines **where a variable can be accessed** within a program.
- Python resolves variable names using the **LEGB (Local → Enclosing → Global → Built-in)** rule.
- Local variables exist only during function execution, while global variables remain available throughout the module.
- The `global` keyword allows modification of global variables inside functions.
- Nested functions can access variables from their enclosing functions, enabling closures and better code organization.



## Summary

Variable scope is an essential concept in Python that controls the visibility and lifetime of variables. Understanding Local, Enclosing, Global, and Built-in scopes helps write cleaner, safer, and more maintainable code while preventing unexpected variable conflicts.
