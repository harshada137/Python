# Import Statements in Python

## What is an Import Statement?

An **import statement** is used to bring code from another module into your Python program. It allows you to access functions, classes, and variables defined in other modules without rewriting the code.

---

# Why Use Import Statements?

- Reuse existing code
- Access Python's built-in libraries
- Keep programs organized
- Reduce duplicate code
- Improve readability and maintainability

---

# Syntax of Import Statements

## 1. Import an Entire Module

Imports the complete module. Members are accessed using the module name.

```python
import math

print(math.sqrt(36))
```

Output:

```
6.0
```

---

## 2. Import Specific Objects

Imports only the required functions or variables from a module.

```python
from math import sqrt, pi

print(sqrt(49))
print(pi)
```

---

## 3. Import with an Alias

An alias provides a shorter name for a module.

```python
import math as m

print(m.factorial(5))
```

---

## 4. Import Everything

Imports all public members of a module into the current namespace.

```python
from math import *

print(sqrt(64))
```

> **Note:** This approach is generally discouraged because it can lead to naming conflicts and reduces code readability.

---

# How Python Processes an Import

When an `import` statement is executed, Python:

1. Checks if the module is already loaded.
2. Searches for the module in the module search path.
3. Loads the module if found.
4. Makes its contents available to the program.

---

# Commonly Imported Built-in Modules

| Module | Purpose |
|---------|----------|
| `math` | Mathematical functions |
| `random` | Random number generation |
| `os` | Operating system utilities |
| `sys` | System-specific functions |
| `datetime` | Date and time handling |
| `json` | Working with JSON data |

---

# Best Practices

- Import only the modules you need.
- Use aliases for long module names when appropriate.
- Avoid using `from module import *`.
- Place all import statements at the beginning of the file.

---

# Summary

- Import statements allow you to use code from other modules.
- `import module` imports the entire module.
- `from module import object` imports selected objects.
- `import module as alias` creates a shorter name for the module.
- `from module import *` imports all public members but should generally be avoided.
- Proper use of imports improves code organization, readability, and reusability.
