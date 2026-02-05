
## What are Data Types in Python?

A **data type** tells Python **what kind of data** a variable is holding and **what operations** can be performed on it.

Python is **dynamically typed**, which means:

* You don’t need to declare the data type explicitly
* Python automatically assigns the data type at runtime

```python
x = 10        # int
y = 3.5       # float
name = "ABC"  # str
```

---

## 1. Numeric Data Types

Used to store numbers.

### a) `int` (Integer)

Stores **whole numbers** (positive, negative, zero).

```python
a = 10
b = -25
c = 0
```

✔ No size limit
✔ Supports arithmetic operations

---

### b) `float`

Stores **decimal numbers**.

```python
pi = 3.14
price = 99.99
```

✔ Less precise than `int`
✔ Used in calculations involving fractions

---

### c) `complex`

Stores numbers with **real and imaginary parts**.

```python
z = 2 + 3j
```

* `z.real` → real part
* `z.imag` → imaginary part

Used in scientific and mathematical applications.

---

## 2. Text Data Type

### `str` (String)

Used to store **text or characters**.

```python
name = "Harshada"
msg = 'Python is easy'
```

✔ Can use **single or double quotes**
✔ Strings are **immutable** (cannot be changed)

```python
s = "Hello"
# s[0] = "h"  ❌ Error
```

---

## 3. Boolean Data Type

### `bool`

Stores **True or False** values.

```python
is_active = True
is_logged_in = False
```

✔ Mostly used in **conditions and loops**

```python
print(10 > 5)   # True
print(10 == 5)  # False
```

---

## 4. Sequence Data Types

Used to store **multiple values**.

---

### a) `list`

* Ordered
* Mutable (can change)
* Allows duplicate values

```python
numbers = [1, 2, 3, 4]
numbers.append(5)
```

✔ Most commonly used
✔ Can store mixed data types

```python
data = [1, "Python", 3.5, True]
```

---

### b) `tuple`

* Ordered
* Immutable (cannot change)
* Faster than list

```python
colors = ("red", "green", "blue")
```

✔ Used when data should not change
✔ Safer than list

---

### c) `range`

Used to generate a sequence of numbers.

```python
r = range(1, 6)
print(list(r))  # [1, 2, 3, 4, 5]
```

✔ Common in loops

---

## 5. Set Data Types

### a) `set`

* Unordered
* No duplicate values
* Mutable

```python
s = {1, 2, 3, 3}
print(s)  # {1, 2, 3}
```

✔ Used for **unique values**

---

### b) `frozenset`

* Same as set
* Immutable

```python
fs = frozenset([1, 2, 3])
```

✔ Used when data must not change

---

## 6. Mapping Data Type

### `dict` (Dictionary)

Stores data in **key–value pairs**.

```python
student = {
    "name": "Harshada",
    "age": 22,
    "course": "Python"
}
```

✔ Keys must be unique
✔ Values can be any data type

```python
print(student["name"])
```

---

## 7. None Data Type

### `NoneType`

Represents **no value** or **empty value**.

```python
result = None
```

✔ Often used as a placeholder
✔ Not the same as `0` or `False`

---

## 8. Checking Data Type

Use `type()` function:

```python
x = 10
print(type(x))   # <class 'int'>
```

---

## Summary Table

| Data Type | Example    |
| --------- | ---------- |
| int       | `10`       |
| float     | `3.14`     |
| complex   | `2+3j`     |
| str       | `"Python"` |
| bool      | `True`     |
| list      | `[1,2,3]`  |
| tuple     | `(1,2,3)`  |
| set       | `{1,2,3}`  |
| dict      | `{"a":1}`  |
| NoneType  | `None`     |


