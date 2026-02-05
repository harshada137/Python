## What is Type Casting in Python?

**Type Casting** means **converting one data type into another data type**.

Example:

```python
a = "10"      # string
b = int(a)    # converted to integer
```

Here, `"10"` → `10`

---

## Why do we need Type Casting?

1. User input is always **string**
2. Perform mathematical operations
3. Convert data for compatibility
4. Data processing & validation

```python
x = input("Enter number: ")
print(type(x))   # str
```

To calculate:

```python
x = int(input("Enter number: "))
print(x + 5)
```

---

## Types of Type Casting

### 1. Implicit Type Casting (Automatic)

Python converts **automatically**.

```python
a = 10       # int
b = 2.5      # float
c = a + b
print(c)     # 12.5
print(type(c))  # float
```

✔ Happens when no data loss
✔ Lower type → higher type

Order:

```
int → float → complex
```

---

### 2. Explicit Type Casting (Manual)

Programmer converts **manually** using functions.

---

## Common Type Casting Functions

---

### `int()`

Converts to integer.

```python
int(10.5)     # 10
int("20")     # 20
```

❌ Invalid:

```python
int("10.5")   # Error
int("abc")    # Error
```

---

### `float()`

Converts to float.

```python
float(10)       # 10.0
float("3.14")   # 3.14
```

---

### `str()`

Converts to string.

```python
str(100)      # "100"
str(3.14)     # "3.14"
```

---

### `bool()`

Converts to boolean.

```python
bool(0)        # False
bool(1)        # True
bool("")       # False
bool("Hi")     # True
```

Rule:

* **0, 0.0, "", None → False**
* Everything else → True

---

### `list()`, `tuple()`, `set()`

Convert between collections.

```python
list("abc")        # ['a', 'b', 'c']
tuple([1, 2, 3])   # (1, 2, 3)
set([1, 1, 2, 3])  # {1, 2, 3}
```

---

### `dict()`

Converts key–value pairs.

```python
dict([(1, 'a'), (2, 'b')])
```

---

## Type Casting with User Input

```python
a = int(input("Enter a number: "))
b = float(input("Enter decimal: "))
print(a + b)
```

---

## Common Errors in Type Casting

```python
int("10.5")  # ❌ ValueError
```

Correct:

```python
int(float("10.5"))  # ✅ 10
```

---

## Checking Type After Casting

```python
x = float(5)
print(type(x))  # <class 'float'>
```

---

## Difference Between Implicit & Explicit Casting

| Implicit       | Explicit           |
| -------------- | ------------------ |
| Automatic      | Manual             |
| Done by Python | Done by programmer |
| No data loss   | Risk of data loss  |

---

## Real-World Example

```python
price = "100"
qty = 2

total = int(price) * qty
print(total)
```

---

## Summary

* Type casting = converting one data type to another
* Python supports **implicit & explicit casting**
* Use built-in functions like `int()`, `float()`, `str()`, `bool()`
* Important for user input & calculations

---

