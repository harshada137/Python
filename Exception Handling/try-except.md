# try / except in Python

## Introduction

Python provides exception handling to prevent programs from crashing when runtime errors occur.

The `try` and `except` blocks allow us to catch errors and handle them gracefully.

Instead of terminating the program, Python executes the code inside the `except` block whenever an exception occurs.

---

## Syntax

```python
try:
    # Code that may generate an exception
except ExceptionType:
    # Code to handle the exception
```

---

## How it Works

1. Python executes the code inside the `try` block.
2. If no error occurs, the `except` block is skipped.
3. If an exception occurs, Python immediately jumps to the matching `except` block.
4. The program continues executing after the exception is handled.

---

## Example 1

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

**Output**

```
Cannot divide by zero.
```

---

## Example 2

```python
try:
    number = int("Hello")
except ValueError:
    print("Invalid integer.")
```

**Output**

```
Invalid integer.
```

---

## Advantages

- Prevents program crashes.
- Improves user experience.
- Makes debugging easier.
- Allows handling different exception types separately.

---

## Key Points

- Always place risky code inside the `try` block.
- Use `except` to handle expected runtime errors.
- Multiple `except` blocks can be used for different exceptions.
