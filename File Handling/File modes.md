# File Modes in Python

## Introduction

When working with files in Python, you must specify **how** you want to access the file. This is done using **file modes**.

The mode tells Python whether you want to:

- Read the file
- Write to the file
- Append data
- Create a new file
- Work with binary files
- Read and write together

The mode is passed as the second argument to the `open()` function.

```python
file = open("example.txt", "r")
```

Here:

- `example.txt` → filename
- `r` → mode

---

# Why File Modes Are Important

Python needs to know your intention before opening a file.

For example:

- Reading should not accidentally erase data.
- Writing should overwrite only when intended.
- Appending should preserve existing content.

Choosing the wrong mode may result in data loss.

---

# Common File Modes

| Mode | Meaning | File Must Exist | Creates File |
|------|----------|----------------|--------------|
| `r` | Read | Yes | No |
| `w` | Write | No | Yes |
| `a` | Append | No | Yes |
| `x` | Create new file | No | Yes |
| `r+` | Read & Write | Yes | No |
| `w+` | Write & Read | No | Yes |
| `a+` | Append & Read | No | Yes |
| `rb` | Read Binary | Yes | No |
| `wb` | Write Binary | No | Yes |
| `ab` | Append Binary | No | Yes |

---

# Read Mode (`r`)

- Default mode.
- Opens an existing file.
- Cannot modify the file.
- Raises `FileNotFoundError` if the file doesn't exist.

Example:

```python
file = open("notes.txt", "r")
print(file.read())
file.close()
```

---

# Write Mode (`w`)

- Creates a new file if it doesn't exist.
- Deletes all existing content if the file already exists.
- Starts writing from the beginning.

Example:

```python
file = open("notes.txt", "w")
file.write("Python")
file.close()
```

---

# Append Mode (`a`)

- Adds new data to the end.
- Existing content remains unchanged.
- Creates the file if it doesn't exist.

Example:

```python
file = open("notes.txt", "a")
file.write("\nLearning File Handling")
file.close()
```

---

# Exclusive Create (`x`)

Creates a file only if it doesn't already exist.

If the file exists:

```
FileExistsError
```

Example:

```python
file = open("newfile.txt", "x")
file.close()
```

---

# Binary Modes

Used for non-text files such as:

- Images
- Videos
- PDFs
- ZIP files

Examples:

```
rb
wb
ab
```

---

# Text vs Binary

Text Mode

- Human-readable
- Default mode

Binary Mode

- Stores raw bytes
- Used for multimedia files

---

# Best Practices

- Always choose the correct mode.
- Close files after use.
- Prefer using the `with` statement.
- Avoid using `w` unless overwriting is intended.

---

# Summary

- `r` → Read
- `w` → Write (overwrites)
- `a` → Append
- `x` → Create new file
- `+` → Read and write
- `b` → Binary mode
