# Writing Files in Python

# Introduction

Writing allows a Python program to store data permanently.

Examples include:

- Saving reports
- Creating log files
- Exporting data
- Configuration files

Writing is performed using `write()` or `writelines()`.

---

# Write Mode

```python
file = open("notes.txt", "w")
```

Characteristics:

- Creates file if absent.
- Overwrites existing content.

---

# write()

Writes a string.

Example:

```python
file = open("notes.txt", "w")
file.write("Learning Python")
file.close()
```

---

# writelines()

Writes multiple strings.

Example:

```python
file = open("notes.txt", "w")
file.writelines(["Python\n", "Linux\n"])
file.close()
```

---

# Difference

| write() | writelines() |
|----------|--------------|
| Single string | Multiple strings |
| One call | List/Tuple |

---

# Important Notes

- `write()` returns number of characters written.
- Newline (`\n`) must be added manually.

---

# Best Practices

- Be careful with `w` mode.
- Always close the file.
- Prefer `with`.

---

# Summary

- `w` overwrites file.
- `write()` writes one string.
- `writelines()` writes multiple strings.
