
## **1. Indexing**

Indexing is used to **access a single character** in a string.

### Rules:

* Indexing starts from **0** for the first character.
* Negative indexing starts from **-1** for the last character, -2 for the second last, and so on.

### Example:

```python
text = "Hello, World!"
```

* Positive indexing:

```
H  e  l  l  o  ,     W  o  r  l  d  !
0  1  2  3  4  5  6  7  8  9 10 11 12
```

* Negative indexing:

```
H  e  l  l  o  ,     W  o  r  l  d  !
-13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
```

**Access characters:**

```python
print(text[0])   # H
print(text[7])   # W
print(text[-1])  # !
print(text[-5])  # r
```

✅ Key point: Indexing **returns a single character**.

---

## **2. Slicing**

Slicing is used to **access a part (substring) of a string**.

### Syntax:

```python
string[start:stop:step]
```

* `start` → index where slice starts (inclusive)
* `stop` → index where slice ends (exclusive)
* `step` → how many steps to jump (optional, default = 1)

### Examples:

```python
text = "Hello, World!"

# Get "Hello"
print(text[0:5])   # H e l l o (index 0 to 4)

# Get "World"
print(text[7:12])  # W o r l d (index 7 to 11)

# From beginning to index 4
print(text[:5])    # H e l l o

# From index 7 to end
print(text[7:])    # W o r l d !

# Using step
print(text[::2])   # H l o W r d  (every 2nd character)

# Reverse the string
print(text[::-1])  # !dlroW ,olleH
```

✅ Key points:

* The `stop` index is **not included** in the result.
* Omitting `start` or `stop` means slicing from beginning or till end.
* Step allows you to skip characters or reverse the string.

---

### **Summary Table**

| Concept           | Syntax          | Example      | Output        |
| ----------------- | --------------- | ------------ | ------------- |
| Indexing          | `string[i]`     | `text[1]`    | e             |
| Slicing           | `string[i:j]`   | `text[0:5]`  | Hello         |
| Slicing with step | `string[i:j:k]` | `text[::2]`  | HloWrd        |
| Negative indexing | `string[-i]`    | `text[-1]`   | !             |
| Reverse string    | `string[::-1]`  | `text[::-1]` | !dlroW ,olleH |

