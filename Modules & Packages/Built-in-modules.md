# Built-in Modules

## What are Built-in Modules?

Built-in modules are modules that come pre-installed with Python. They are included when you install Python, so you do **not** need to install them separately.

These modules provide ready-made functions and classes that help you perform common tasks like mathematical calculations, file handling, date and time operations, random number generation, and interaction with the operating system.

To use a built-in module, you simply import it into your program.

**Syntax:**
```python
import module_name
```

---

## Why Use Built-in Modules?

- Save development time
- Reduce the amount of code you need to write
- Provide reliable and tested functionality
- Improve code readability
- Make programs more efficient

---

## Common Built-in Modules

### 1. math
Used for mathematical operations.

Functions include:
- sqrt()
- ceil()
- floor()
- factorial()
- pow()

---

### 2. random
Used to generate random numbers and make random selections.

Functions include:
- randint()
- choice()
- random()
- shuffle()

---

### 3. datetime
Used to work with dates and time.

It helps you:
- Get the current date
- Get the current time
- Calculate date differences
- Format dates

---

### 4. os
Used to interact with the operating system.

Common uses:
- Create folders
- Delete files
- Rename files
- Get the current working directory

---

### 5. sys
Provides information about the Python interpreter.

Common uses:
- Command-line arguments
- Python version
- Exit a program
- System-specific information

---

## Importing Modules

Import an entire module:

```python
import math
```

Import only a specific function:

```python
from math import sqrt
```

Import with an alias:

```python
import datetime as dt
```

---

## Example

```python
import math

print(math.sqrt(49))
```

**Output**

```
7.0
```

---

## Advantages

- Already available with Python
- Easy to use
- Well-tested and reliable
- Saves development time
- Makes code shorter and cleaner

---

## Limitations

- Only provide common functionality
- Cannot solve every problem
- For advanced features, external packages may be required

---

## Summary

- Built-in modules come with Python.
- No installation is required.
- They are imported using the `import` keyword.
- They help perform common programming tasks quickly and efficiently.
