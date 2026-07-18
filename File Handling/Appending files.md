# Appending Files in Python

# Introduction

Appending means adding new data without deleting existing content.

Python uses append mode (`a`) for this purpose.

---

# Why Append?

Useful for:

- Logs
- Reports
- User history
- Daily records

---

# Append Mode

```python
file = open("notes.txt", "a")
```

If file doesn't exist, Python creates it.

---

# Example

```python
file = open("notes.txt", "a")
file.write("\nPython File Handling")
file.close()
```

---

# Append vs Write

| Write | Append |
|--------|---------|
| Deletes old data | Keeps old data |
| Starts from beginning | Starts from end |

---

# Best Practices

- Use append for logs.
- Add `\n` when writing new entries.
- Use `with`.

---

# Summary

- Mode: `a`
- Preserves old data.
- Adds new data at end.
