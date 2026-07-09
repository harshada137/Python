# User-defined Modules

## What are User-defined Modules?

A **user-defined module** is a Python file (`.py`) created by the programmer to organize code into reusable components.

Instead of writing the same code repeatedly in different programs, you can place related functions, variables, or classes in a separate Python file and import it whenever needed.

A user-defined module helps make programs cleaner, easier to understand, and easier to maintain.

---

## Why Use User-defined Modules?

As a project grows, writing all the code in a single file becomes difficult to manage.

Using modules helps you:

- Reuse code in multiple programs
- Organize related functions together
- Make debugging easier
- Improve readability
- Reduce duplicate code
- Simplify maintenance

---

## Creating a User-defined Module

A user-defined module is simply a Python file.

For example:

```
calculator.py
```

Inside this file, you can write functions, variables, or classes.

---

## Using a User-defined Module

Once the module is created, it can be imported into another Python file.

**Syntax**

```python
import module_name
```

or

```python
from module_name import function_name
```

---

## Ways to Import a Module

### 1. Import the entire module

```python
import calculator
```

You must use the module name before calling its functions.

---

### 2. Import a specific function

```python
from calculator import add
```

Now the function can be used directly.

---

### 3. Import with an alias

```python
import calculator as calc
```

This gives the module a shorter name.

---

## Example

### calculator.py

```python
def add(a, b):
    return a + b
```

### main.py

```python
import calculator

print(calculator.add(10, 20))
```

**Output**

```
30
```

---

## Advantages

- Promotes code reuse
- Makes programs modular
- Improves readability
- Easier to test and debug
- Makes large projects easier to manage
- Reduces code duplication

---

## Limitations

- Too many modules can make a project harder to navigate.
- Incorrect imports may cause errors.
- Circular imports should be avoided.

---

## Best Practices

- Give modules meaningful names.
- Keep related functions in the same module.
- Avoid writing unnecessary code in the global scope.
- Add comments or documentation for important functions.
- Keep modules focused on a single purpose.

---

## Difference Between Built-in and User-defined Modules

| Built-in Modules | User-defined Modules |
|------------------|----------------------|
| Provided by Python | Created by the programmer |
| No installation required | Created as `.py` files |
| Used for common tasks | Used for project-specific tasks |
| Available after Python installation | Must be created before use |

---

## Summary

- A user-defined module is a Python file created by the programmer.
- It helps organize code into reusable components.
- Modules are imported using the `import` statement.
- They improve code organization, readability, and maintenance.
- User-defined modules are widely used in medium and large Python projects.
