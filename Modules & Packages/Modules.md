# Python Modules

## What is a Module?

A **module** is a Python file (`.py`) that contains functions, classes, and variables. Modules help organize code into reusable and manageable files.

For example:

- `math.py`
- `random.py`
- `my_module.py`

---

# Why Use Modules?

- Improve code reusability
- Keep projects organized
- Avoid writing the same code repeatedly
- Make debugging and maintenance easier

---

# Types of Modules

## 1. Built-in Modules

These modules come pre-installed with Python.

Common examples:

- `math`
- `random`
- `datetime`
- `os`
- `sys`

### Example

```python
import math

print(math.sqrt(25))
```

Output:

```
5.0
```

---

## 2. User-Defined Modules

You can create your own module by writing Python code in a `.py` file.

Example:

**my_module.py**

```python
def greet(name):
    return f"Hello, {name}!"
```

Use it in another file:

```python
import my_module

print(my_module.greet("Harsha"))
```

---

# Importing Modules

Python provides multiple ways to import modules.

## Import Entire Module

```python
import math
```

Access members using:

```python
math.pi
math.sqrt(16)
```

---

## Import Specific Functions

```python
from math import sqrt, pi
```

Now use them directly:

```python
print(sqrt(49))
```

---

## Import with Alias

Aliases make long module names shorter.

```python
import numpy as np
```

Example:

```python
arr = np.array([1, 2, 3])
```

---

# The `dir()` Function

The `dir()` function lists all attributes and functions available in a module.

Example:

```python
import math

print(dir(math))
```

---

# Module Search Path

When a module is imported, Python searches in the following order:

1. Current directory
2. Standard library
3. Installed third-party packages
4. Directories listed in `sys.path`

---

# The `__name__` Variable

Every Python module contains a special variable called `__name__`.

- If the file is run directly, `__name__ == "__main__"`
- If the file is imported, `__name__` is the module name.

Example:

```python
if __name__ == "__main__":
    print("This file is executed directly.")
```

---

# Popular Built-in Modules

| Module | Purpose |
|---------|----------|
| `math` | Mathematical operations |
| `random` | Generate random values |
| `os` | Operating system functions |
| `sys` | Python interpreter utilities |
| `datetime` | Date and time operations |
| `statistics` | Statistical calculations |

---

# Advantages of Modules

- Promote code reuse
- Improve readability
- Simplify maintenance
- Reduce duplicate code
- Organize large projects effectively

---

# Summary

- A module is a Python file containing reusable code.
- Python supports built-in and user-defined modules.
- Modules are imported using the `import` statement.
- Specific functions can be imported using `from ... import`.
- Aliases simplify module names.
- `dir()` displays module contents.
- `__name__` helps identify whether a file is run directly or imported.
