# raise Keyword in Python

## Introduction

The `raise` keyword is used to manually generate an exception.

Instead of waiting for Python to detect an error automatically, developers can raise exceptions whenever invalid conditions are detected.

---

## Syntax

```python
raise ExceptionType("Message")
```

---

## Why Use raise?

- Validate user input.
- Stop program execution when required.
- Enforce business rules.
- Generate meaningful error messages.

---

## Example

```python
age = -10

if age < 0:
    raise ValueError("Age cannot be negative")
```

**Output**

```
ValueError: Age cannot be negative
```

---

## Difference Between raise and try/except

| raise | try/except |
|--------|------------|
| Generates an exception | Handles an exception |
| Stops execution | Prevents program crash |
| Used for validation | Used for recovery |

---

## Key Points

- `raise` creates an exception manually.
- Any built-in or custom exception can be raised.
- Often used with input validation and custom exceptions.
