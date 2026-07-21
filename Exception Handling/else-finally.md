# else and finally in Python Exception Handling

## Introduction

Along with `try` and `except`, Python provides two additional blocks:

- `else`
- `finally`

These blocks help organize exception handling and cleanup operations.

---

# else Block

The `else` block executes only when no exception occurs inside the `try` block.

### Syntax

```python
try:
    pass
except:
    pass
else:
    pass
```

### Example

```python
try:
    number = 10 / 2
except ZeroDivisionError:
    print("Division error")
else:
    print("Division successful")
```

**Output**

```
Division successful
```

---

# finally Block

The `finally` block executes regardless of whether an exception occurs.

It is mainly used for cleanup tasks such as:

- Closing files
- Closing database connections
- Releasing network resources

### Example

```python
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Error")
finally:
    print("Execution Finished")
```

**Output**

```
Error
Execution Finished
```

---

## Summary

| Block | Executes When |
|---------|--------------|
| try | Always |
| except | Only if an exception occurs |
| else | Only if no exception occurs |
| finally | Always |

---

## Key Points

- `else` executes only when the `try` block succeeds.
- `finally` always executes.
- `finally` is commonly used for resource cleanup.
