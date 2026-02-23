## 🔹 Set in Python

A **set** in Python is a **built-in data structure** used to store **multiple unique elements** in a single variable.

It is:

* ✅ **Unordered**
* ✅ **Mutable**
* ❌ **No duplicate values**
* ❌ **No indexing**

---

# 📌 1️⃣ Creating a Set

### Using Curly Braces

```python
my_set = {1, 2, 3, 4}
print(my_set)
```

### Using `set()` Constructor

```python
my_set = set([1, 2, 2, 3])
print(my_set)   # Output: {1, 2, 3}
```

👉 Duplicate values are automatically removed.

---

# 📌 2️⃣ Properties of Set

### 🔹 Unordered

Elements do not maintain insertion order.

```python
s = {10, 20, 30}
print(s)  # Order may vary
```

---

### 🔹 Unique Elements

```python
s = {1, 1, 2, 3}
print(s)   # {1, 2, 3}
```

---

### 🔹 No Indexing

```python
s = {1, 2, 3}
print(s[0])  # ❌ Error
```

Sets do not support:

* Indexing
* Slicing

---

# 📌 3️⃣ Adding Elements

### Add Single Element

```python
s = {1, 2}
s.add(3)
print(s)
```

### Add Multiple Elements

```python
s.update([4, 5])
print(s)
```

---

# 📌 4️⃣ Removing Elements

### remove()

Removes specific element (error if not found)

```python
s.remove(2)
```

### discard()

Does not raise error if element not present

```python
s.discard(10)
```

### pop()

Removes random element

```python
s.pop()
```

### clear()

Removes all elements

```python
s.clear()
```

---

# 📌 5️⃣ Set Operations (Very Important 🔥)

Let:

```python
A = {1, 2, 3}
B = {3, 4, 5}
```

---

## 🔹 Union (Combine both sets)

```python
A.union(B)
# or
A | B
```

Output:

```
{1, 2, 3, 4, 5}
```

---

## 🔹 Intersection (Common elements)

```python
A.intersection(B)
# or
A & B
```

Output:

```
{3}
```

---

## 🔹 Difference

```python
A.difference(B)
# or
A - B
```

Output:

```
{1, 2}
```

---

## 🔹 Symmetric Difference

```python
A.symmetric_difference(B)
# or
A ^ B
```

Output:

```
{1, 2, 4, 5}
```

---

# 📌 6️⃣ Checking Membership

```python
if 2 in A:
    print("Yes")
```

---

# 📌 7️⃣ Frozen Set (Immutable Set)

A **frozenset** is an immutable version of set.

```python
fs = frozenset([1, 2, 3])
```

❌ Cannot add or remove elements.

Used when:

* You need a set as dictionary key
* You want immutable collection

---

# 📌 8️⃣ Why Use Set?

Use set when:

* Removing duplicates
* Fast membership testing
* Mathematical set operations
* Comparing collections

---

# 📌 9️⃣ Time Complexity

| Operation | Average Time       |
| --------- | ------------------ |
| Add       | O(1)               |
| Remove    | O(1)               |
| Search    | O(1)               |
| Union     | O(len(A) + len(B)) |

👉 Sets are implemented using **hash tables**.

---

# 🎯 Difference Between List and Set

| Feature    | List | Set |
| ---------- | ---- | --- |
| Ordered    | ✅    | ❌   |
| Duplicates | ✅    | ❌   |
| Indexing   | ✅    | ❌   |
| Mutable    | ✅    | ✅   |
