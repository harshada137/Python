# Exception Handling

Exception handling is a Python feature used to handle runtime errors gracefully without stopping the program. It allows you to catch unexpected errors, display meaningful messages, and continue execution when appropriate.

## Topics Covered

- Types of Errors
- `try` / `except`
- `else`
- `finally`
- `raise` keyword
- Custom Exceptions

## Why Use Exception Handling?

- Prevents program crashes
- Handles runtime errors gracefully
- Improves code reliability and readability
- Allows proper cleanup of resources (e.g., files, database connections)

## Example

```python
try:
    num = int(input("Enter a number: "))
    print(10 / num)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Invalid input.")
```

> This folder contains concise notes and examples covering Python exception handling concepts.
