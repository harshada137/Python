# with Statement in Python

# Introduction

Managing files manually requires calling `close()`.

Forgetting to close files can cause:

- Memory leaks
- Locked files
- Resource wastage

Python solves this using the `with` statement.

---

# Syntax

```python
with open("notes.txt", "r") as file:
    print(file.read())
```

No need to call:

```python
file.close()
```

Python closes the file automatically.

---

# Advantages

- Cleaner code
- Automatic resource management
- Exception safe
- Recommended by Python

---

# Example

```python
with open("notes.txt", "w") as file:
    file.write("Python")
```

---

# How It Works

The file is automatically closed after leaving the `with` block, even if an exception occurs.

---

# Best Practices

Always use `with` unless there is a special reason not to.

---

# Summary

- Automatic closing
- Cleaner code
- Prevents resource leaks
- Pythonic approach
