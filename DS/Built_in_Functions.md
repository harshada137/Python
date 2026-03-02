# 📌 Built-in Functions in Python

**Built-in functions** are pre-defined functions available in Python without importing any module.

You can use them directly.

---

## 🔹 1. Commonly Used Built-in Functions

### ✅ Type & Information Functions

```python
type(10)        # <class 'int'>
id("hello")     # memory address
len([1,2,3])    # 3
```

---

### ✅ Input & Output Functions

```python
print("Hello")
name = input("Enter name: ")
```

---

### ✅ Type Conversion Functions

```python
int("10")       # 10
float("3.14")   # 3.14
str(100)        # "100"
list((1,2,3))   # [1,2,3]
tuple([1,2])    # (1,2)
set([1,1,2])    # {1,2}
```

---

### ✅ Mathematical Functions

```python
abs(-5)         # 5
round(3.456, 2) # 3.46
pow(2,3)        # 8
min(1,2,3)      # 1
max(1,2,3)      # 3
sum([1,2,3])    # 6
```

---

### ✅ Iteration Functions

```python
range(5)        
enumerate(["a","b"])
zip([1,2], [3,4])
```

---

### ✅ Logical Functions

```python
all([True, True])      # True
any([False, True])     # True
```

---

### ✅ Sorting Functions

```python
sorted([3,1,2])     # [1,2,3]
```

---

### ✅ Object Related Functions

```python
dir(list)
help(print)
isinstance(10, int)
```

---

# 🎯 Important Built-in Functions for Interviews

| Function      | Purpose                    |
| ------------- | -------------------------- |
| `len()`       | Returns length             |
| `type()`      | Returns data type          |
| `id()`        | Returns memory address     |
| `sum()`       | Adds elements              |
| `sorted()`    | Returns sorted list        |
| `enumerate()` | Returns index + value      |
| `zip()`       | Combines iterables         |
| `map()`       | Apply function to iterable |
| `filter()`    | Filter elements            |
| `eval()`      | Evaluate expression        |
| `exec()`      | Execute code               |

---


# 🔹 What is Mutable?

**Mutable objects can be changed after creation.**

Memory location stays same when modified.

### ✅ Examples of Mutable Types:

* List
* Dictionary
* Set
* Bytearray

---

### Example:

```python
a = [1,2,3]
print(id(a))

a.append(4)
print(id(a))   # Same memory location
```

✔ The object is modified, not replaced.

---

# 🔹 What is Immutable?

**Immutable objects cannot be changed after creation.**

If modified, a new object is created in memory.

### ✅ Examples of Immutable Types:

* int
* float
* string
* tuple
* frozenset
* bool

---

### Example:

```python
x = 10
print(id(x))

x = 20
print(id(x))   # Different memory location
```

✔ A new object is created.

---

# 🔹 Important Example (Very Common in Interviews)

### String Example (Immutable)

```python
s = "hello"
s[0] = "H"   # ❌ Error
```

You cannot modify string characters.

---

### Tuple Example (Immutable)

```python
t = (1,2,3)
t[0] = 10   # ❌ Error
```

---

# 🔹 Special Case (Very Important)

Tuple is immutable, but if it contains mutable object:

```python
t = ([1,2,3], 4)
t[0].append(5)
print(t)
```

✔ Works because list inside tuple is mutable.

---

# 🔹 Memory Concept (Interview Level)

Immutable:

* New object created on modification
* Safer
* Faster for hash-based collections

Mutable:

* Modified in-place
* Efficient for large data modifications

---

# 🔹 Why Immutability is Important?

* Used as dictionary keys
* Used in sets
* Improves security
* Prevents accidental changes

Example:

```python
d = {(1,2): "value"}  # Allowed
```

But:

```python
d = {[1,2]: "value"}  # ❌ Error
```

---

# 🔥 Difference Table

| Feature                | Mutable         | Immutable       |
| ---------------------- | --------------- | --------------- |
| Can change value?      | Yes             | No              |
| Memory location        | Same            | New created     |
| Examples               | list, dict, set | int, str, tuple |
| Can be dictionary key? | No              | Yes             |

---

# 🎯 Interview-Ready Definition

> Mutable objects can be modified after creation without changing their memory location, while immutable objects cannot be modified and any change results in the creation of a new object.

