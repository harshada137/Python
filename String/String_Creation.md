## 🔹 String Creation in Python

### 1️⃣ What is a String in Python?

A **String** in Python is a sequence of characters enclosed in quotes.

Strings are:

* Ordered
* Immutable (cannot be changed after creation)
* Indexed
* Iterable

In Python, strings are objects of the built-in `str` class.

---

### 2️⃣ Ways to Create a String in Python

---

## ✅ 1. Using Single Quotes

```python
s = 'Hello'
```

Used for simple text.

---

## ✅ 2. Using Double Quotes

```python
s = "Hello"
```

Single and double quotes behave the same.

Useful when string contains an apostrophe:

```python
s = "It's Python"
```

---

## ✅ 3. Using Triple Quotes (Multi-line Strings)

```python
s = """This is
a multi-line
string"""
```

Used for:

* Multi-line text
* Docstrings

---

## ✅ 4. Using str() Constructor

```python
s = str(123)   # '123'
```

Converts other data types into string.

---

## ✅ 5. Using String Formatting

### 🔹 f-Strings (Recommended – Python 3.6+)

```python
name = "Harshada"
s = f"My name is {name}"
```

Most efficient and readable method.

---

### 🔹 format() Method

```python
s = "My name is {}".format("Harshada")
```

---

### 🔹 % Formatting (Old Style)

```python
s = "My name is %s" % "Harshada"
```

---

## ✅ 6. Using join() Method

```python
words = ["Hello", "World"]
s = " ".join(words)
```

Used to combine multiple strings efficiently.

---

## ✅ 7. Using Concatenation

```python
s = "Hello" + " " + "World"
```

Creates a new string object.

---

## 🔹 Important Concept: String Immutability

Once created, a string **cannot be modified**.

Example:

```python
s = "Hello"
s[0] = "h"   # ❌ Error
```

Instead, a new string is created:

```python
s = "h" + s[1:]
```

---

## 🔹 Memory Optimization (Interning Concept)

Python optimizes small and frequently used strings by storing them in a shared memory pool (string interning).

Example:

```python
a = "hello"
b = "hello"
print(a is b)  # True (may share memory)
```

---

## 🔹 Summary

String creation methods:

* Single quotes
* Double quotes
* Triple quotes
* str() constructor
* f-strings
* format()
* Concatenation
* join()

Key Points:

* Strings are immutable
* Strings are objects of `str`
* Every modification creates a new string
* f-strings are preferred in modern Python


