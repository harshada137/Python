# Types of Errors in Python

## Introduction

While writing Python programs, errors are inevitable. Errors occur when Python is unable to execute a statement correctly. Understanding different types of errors helps developers identify problems quickly and write more reliable code.

Python errors are broadly classified into three categories:

1. Syntax Errors
2. Runtime Errors (Exceptions)
3. Logical Errors

---

## 1. Syntax Errors

A syntax error occurs when the Python interpreter finds code that violates Python's grammar rules. These errors are detected before the program starts executing.

### Characteristics

- Program does not run.
- Must be fixed before execution.
- Usually caused by missing symbols, incorrect indentation, or spelling mistakes.

### Example

```python
if True
    print("Hello")
```

**Output**

```
SyntaxError: expected ':'
```

---

## 2. Runtime Errors (Exceptions)

Runtime errors occur while the program is running. The syntax is correct, but something unexpected happens during execution.

Some common runtime errors include:

- ZeroDivisionError
- TypeError
- ValueError
- IndexError
- KeyError
- FileNotFoundError

### Example

```python
number = 10 / 0
```

**Output**

```
ZeroDivisionError: division by zero
```

---

## 3. Logical Errors

Logical errors occur when the program executes successfully but produces incorrect output.

These are the hardest errors to identify because Python does not display an error message.

### Example

```python
length = 10
width = 5

# Wrong formula
area = 2 * (length + width)

print(area)
```

The program runs successfully, but the formula calculates the perimeter instead of the area.

---

## Summary

| Error Type | Occurs When | Program Executes |
|------------|------------|------------------|
| Syntax Error | Python grammar is incorrect | No |
| Runtime Error | Error occurs during execution | Stops at error |
| Logical Error | Wrong logic is used | Yes |

---

## Key Points

- Syntax errors prevent execution.
- Runtime errors occur during execution and generate exceptions.
- Logical errors produce incorrect results without showing any error.
- Understanding error types makes debugging much easier.
