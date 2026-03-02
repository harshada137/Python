## 📘 Dictionary in Python (In Detail)

A **Dictionary** in Python is a built-in data structure used to store **key–value pairs**.

It is:

* ✅ **Mutable** (can be changed)
* ✅ **Unordered** (in older versions)
* ✅ **Ordered (Python 3.7+)**
* ✅ Keys must be **unique**
* ✅ Keys must be **immutable** (string, number, tuple)

---

# 🔹 1. Creating a Dictionary

### ✅ Method 1: Using Curly Braces `{}`

```python
student = {
    "name": "Harshada",
    "age": 22,
    "course": "B.Tech"
}
print(student)
```

---

### ✅ Method 2: Using `dict()` Constructor

```python
student = dict(name="Harshada", age=22, course="B.Tech")
print(student)
```

---

# 🔹 2. Accessing Values

### ✅ Using Key

```python
print(student["name"])
```

⚠️ If key does not exist → **Error**

---

### ✅ Using `get()` (Safe Method)

```python
print(student.get("name"))
print(student.get("marks", "Not Found"))
```

✔ No error if key not found.

---

# 🔹 3. Adding & Updating Values

### ✅ Add New Key

```python
student["city"] = "Nagpur"
```

### ✅ Update Existing Key

```python
student["age"] = 23
```

---

# 🔹 4. Removing Items

### ✅ `pop()`

```python
student.pop("age")
```

### ✅ `popitem()` (Removes last item)

```python
student.popitem()
```

### ✅ `del`

```python
del student["course"]
```

### ✅ `clear()` (Removes all items)

```python
student.clear()
```

---

# 🔹 5. Looping Through Dictionary

### ✅ Loop Through Keys

```python
for key in student:
    print(key)
```

### ✅ Loop Through Values

```python
for value in student.values():
    print(value)
```

### ✅ Loop Through Key-Value Pairs

```python
for key, value in student.items():
    print(key, value)
```

---

# 🔹 6. Dictionary Methods

| Method     | Description             |
| ---------- | ----------------------- |
| `keys()`   | Returns all keys        |
| `values()` | Returns all values      |
| `items()`  | Returns key-value pairs |
| `update()` | Update dictionary       |
| `pop()`    | Remove specific key     |
| `clear()`  | Remove all items        |
| `copy()`   | Create shallow copy     |

---

# 🔹 7. Nested Dictionary

Dictionary inside another dictionary.

```python
students = {
    "student1": {"name": "Harshada", "age": 22},
    "student2": {"name": "Riya", "age": 21}
}

print(students["student1"]["name"])
```

---

# 🔹 8. Dictionary with List

```python
data = {
    "names": ["Harshada", "Riya", "Amit"],
    "marks": [85, 90, 88]
}
```

---

# 🔹 9. Dictionary Comprehension

Used to create dictionary in one line.

```python
squares = {x: x*x for x in range(1, 6)}
print(squares)
```

Output:

```
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

---

# 🔹 10. Important Concepts

## ✅ 1. Keys Must Be Immutable

✔ Allowed:

```python
{1: "one"}
{"name": "Harshada"}
(1, 2): "tuple"
```

❌ Not Allowed:

```python
{[1,2]: "list"}   # Error
```

---

## ✅ 2. Duplicate Keys Not Allowed

```python
data = {"a": 1, "a": 2}
print(data)
```

Output:

```
{'a': 2}
```

(Last value overwrites previous one)

---

# 🔹 11. Time Complexity (Very Important for Interviews)

| Operation | Average Time |
| --------- | ------------ |
| Access    | O(1)         |
| Insert    | O(1)         |
| Delete    | O(1)         |
| Search    | O(1)         |

👉 Python dictionary uses **Hash Table** internally.

---

# 🔹 12. Real-World Example (Very Important)

### ✅ Counting Frequency of Elements

```python
text = "apple banana apple mango banana apple"
words = text.split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)
```

Output:

```
{'apple': 3, 'banana': 2, 'mango': 1}
```

---

# 🔹 13. Difference: Dictionary vs List

| Feature           | List        | Dictionary |
| ----------------- | ----------- | ---------- |
| Store data as     | Index-based | Key-value  |
| Access using      | Index       | Key        |
| Duplicate allowed | Yes         | Keys: No   |
| Mutable           | Yes         | Yes        |

---

# 🎯 Interview-Ready Definition

> A dictionary in Python is a mutable, ordered (Python 3.7+) data structure that stores data in key-value pairs. It uses a hash table internally, providing O(1) average time complexity for insert, delete, and lookup operations.


Just tell me 😊
