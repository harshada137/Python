# CSV Files in Python

# Introduction

CSV stands for **Comma-Separated Values**.

CSV files are widely used for storing tabular data.

Example:

```
Name,Age,City
Alice,22,Pune
Bob,25,Mumbai
```

Python provides the built-in `csv` module for handling CSV files.

---

# Why CSV?

Common uses:

- Excel data
- Reports
- Database exports
- Data analysis
- Machine Learning datasets

---

# Import Module

```python
import csv
```

---

# Reading CSV

Example:

```python
import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
```

Each row is returned as a list.

---

# Writing CSV

Example:

```python
import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Age"])
    writer.writerow(["Alice", 22])
```

---

# CSV Reader vs Writer

| Reader | Writer |
|----------|----------|
| Reads rows | Writes rows |
| Returns list | Accepts list |

---

# Why newline=""?

Without it, Windows may insert blank lines between rows.

Using

```python
newline=""
```

prevents this issue.

---

# Best Practices

- Always use `with`.
- Import the `csv` module.
- Use `newline=""` while writing.
- Validate data before writing.

---

# Summary

- CSV stores tabular data.
- `csv.reader()` reads rows.
- `csv.writer()` writes rows.
- Always use `with`.
