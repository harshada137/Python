# Reading Files in Python

# Introduction

Reading files allows Python programs to retrieve stored information.

The data may include:

- Text
- Logs
- Configuration files
- Reports
- User data

Python provides several methods for reading files depending on your requirement.

---

# Opening a File

```python
file = open("notes.txt", "r")
```

This opens the file in read mode.

---

# read()

Reads the complete file.

Example:

```python
file = open("notes.txt", "r")
print(file.read())
file.close()
```

Suitable for small files.

---

# readline()

Reads only one line at a time.

Example:

```python
file = open("notes.txt", "r")
print(file.readline())
file.close()
```

Useful when processing line-by-line.

---

# readlines()

Reads all lines into a list.

Example:

```python
file = open("notes.txt", "r")
print(file.readlines())
file.close()
```

Each list element represents one line.

---

# Reading Using Loop

Large files should be processed line by line.

Example:

```python
file = open("notes.txt", "r")

for line in file:
    print(line)

file.close()
```

This is memory efficient.

---

# File Pointer

Python maintains a pointer indicating the current reading position.

Functions:

- `tell()` → current position
- `seek()` → move pointer

---

# Common Errors

## FileNotFoundError

Occurs when file doesn't exist.

## PermissionError

Occurs when access is denied.

---

# Best Practices

- Use `with` statement.
- Avoid reading huge files using `read()`.
- Process line by line whenever possible.

---

# Summary

- `read()` → Entire file
- `readline()` → One line
- `readlines()` → List of lines
- Loop → Best for large files
