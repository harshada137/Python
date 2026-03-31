String formatting in Python means **inserting variables or values into a string in a clean and readable way**. It’s very important for printing dynamic output, logs, and user messages.

There are **3 main ways** to format strings in Python:

---

# 🔹 1. f-Strings (Formatted String Literals) — ✅ *Best & Modern*

Introduced in Python 3.6, this is the **most recommended way**.

### ✔ Syntax:

```python
name = "Harshada"
age = 22

print(f"My name is {name} and I am {age} years old")
```

### ✔ Output:

```
My name is Harshada and I am 22 years old
```

### ✔ Features:

* Direct variable usage inside `{ }`
* Very readable
* Supports expressions

```python
a = 5
b = 10
print(f"Sum is {a + b}")
```

### ✔ Formatting numbers:

```python
pi = 3.14159
print(f"Value of pi: {pi:.2f}")   # 2 decimal places
```

👉 Output:

```
Value of pi: 3.14
```

---

# 🔹 2. `.format()` Method (Older but Still Used)

### ✔ Syntax:

```python
name = "Harshada"
age = 22

print("My name is {} and I am {} years old".format(name, age))
```

### ✔ Output:

```
My name is Harshada and I am 22 years old
```

### ✔ Using indexes:

```python
print("My name is {0} and I am {1}".format(name, age))
```

### ✔ Using keywords:

```python
print("My name is {n} and I am {a}".format(n="Harshada", a=22))
```

---

# 🔹 3. `%` Formatting (Oldest Method)

### ✔ Syntax:

```python
name = "Harshada"
age = 22

print("My name is %s and I am %d years old" % (name, age))
```

### ✔ Output:

```
My name is Harshada and I am 22 years old
```

### ✔ Common specifiers:

* `%s` → string
* `%d` → integer
* `%f` → float

```python
pi = 3.14159
print("Pi value is %.2f" % pi)
```

---

# 🔹 Alignment & Spacing (Important for interviews)

### ✔ Using f-strings:

```python
name = "Harshada"

print(f"{name:<10}")   # Left aligned
print(f"{name:>10}")   # Right aligned
print(f"{name:^10}")   # Center aligned
```

---

# 🔹 Padding & Width

```python
num = 5
print(f"{num:05}")   # Output: 00005
```

---

# 🔹 Formatting Multiple Values

```python
name = "Harshada"
score = 95.567

print(f"{name} scored {score:.1f}% in exam")
```

---

# 🔹 Multiline Formatting

```python
name = "Harshada"
age = 22

text = f"""
Name: {name}
Age: {age}
"""
print(text)
```

---

# 🔹 Why f-Strings are Best

* Faster than other methods
* Cleaner syntax
* Easy to read
* Supports calculations inside `{}`

---

# 🔹 Summary

| Method       | Usage Level | Recommended  |
| ------------ | ----------- | ------------ |
| f-strings    | Modern      | ✅ Yes        |
| .format()    | Medium      | 👍 Sometimes |
| % formatting | Old         | ❌ No         |



