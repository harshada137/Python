## 📌 Tuple in Python

A **Tuple** in Python is a built-in data structure used to store multiple values in a single variable.

It is:

* ✅ **Ordered**
* ✅ **Indexed**
* ❌ **Immutable** (cannot be changed after creation)
* ✅ Allows duplicate values

---

# 1️⃣ Creating a Tuple

Tuples are created using **parentheses `()`**

```python
t = (10, 20, 30)
print(t)
```

You can also create without parentheses:

```python
t = 10, 20, 30
```

---

## 🔹 Single Element Tuple (Important)

You MUST use a comma:

```python
t = (5,)   # Correct
t = (5)    # Wrong → This is int, not tuple
```

---

# 2️⃣ Accessing Elements

Tuples are **indexed** (like lists).

```python
t = (100, 200, 300)

print(t[0])   # 100
print(t[1])   # 200
```

### 🔹 Negative Indexing

```python
print(t[-1])  # 300
```

---

# 3️⃣ Tuple is Immutable

You cannot modify, add, or remove elements.

```python
t = (1, 2, 3)
t[0] = 10   # ❌ Error
```

This gives:

```
TypeError: 'tuple' object does not support item assignment
```

---

# 4️⃣ Tuple with Different Data Types

```python
t = (10, "Harshada", 3.14, True)
```

Python allows mixed data types.

---

# 5️⃣ Tuple Packing & Unpacking

## 🔹 Packing

```python
t = 1, 2, 3
```

## 🔹 Unpacking

```python
a, b, c = t
print(a)  # 1
```

---

## 🔹 Using * (Star Unpacking)

```python
t = (1, 2, 3, 4, 5)

a, *b, c = t
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5
```

---

# 6️⃣ Tuple Methods

Tuples have only 2 built-in methods:

### 1️⃣ count()

```python
t = (1, 2, 2, 3)
print(t.count(2))  # 2
```

### 2️⃣ index()

```python
print(t.index(3))  # 3
```

---

# 7️⃣ Why Use Tuple Instead of List?

| Feature   | List | Tuple |
| --------- | ---- | ----- |
| Mutable   | ✅    | ❌     |
| Faster    | ❌    | ✅     |
| Safe Data | ❌    | ✅     |
| Methods   | Many | Few   |

---

## 🔹 When to Use Tuple?

* When data should not change
* Storing fixed records (like coordinates)
* Returning multiple values from functions
* Dictionary keys (because tuples are immutable)

---

# 8️⃣ Tuple as Dictionary Key

```python
d = {
    (1, 2): "Point A",
    (3, 4): "Point B"
}
```

Lists cannot be dictionary keys (because they are mutable).

---

# 9️⃣ Nested Tuple

```python
t = ((1, 2), (3, 4))
print(t[0][1])  # 2
```

---

# 🔟 Tuple vs List (Memory & Speed)

* Tuples use **less memory**
* Tuples are **faster** than lists
* Suitable for read-only data

---

# 🎯 Summary

A Tuple is:

* Ordered collection
* Immutable
* Indexed
* Allows duplicates
* Faster than list
* Has only two methods (`count()`, `index()`)

