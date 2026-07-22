# Custom Exceptions in Python

## Introduction

Python provides many built-in exceptions, but sometimes applications require their own error types.

A custom exception is a user-defined exception created by inheriting from the built-in `Exception` class.

Custom exceptions make programs easier to understand and maintain.

---

## Creating a Custom Exception

To create a custom exception:

1. Create a class.
2. Inherit from `Exception`.
3. Raise the exception when required.

---

## Example

```python
class AgeError(Exception):
    pass

age = -5

if age < 0:
    raise AgeError("Age cannot be negative")
```

**Output**

```
AgeError: Age cannot be negative
```

---

## Why Use Custom Exceptions?

- Makes error messages meaningful.
- Represents business-specific problems.
- Improves readability.
- Simplifies debugging.

---

## Key Points

- Every custom exception should inherit from `Exception`.
- Use meaningful class names.
- Raise custom exceptions only when necessary.
