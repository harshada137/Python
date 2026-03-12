
### **What is a string method?**

A **string method** is a **built-in function that you can use on a string** to do something useful, like changing letters, checking content, or splitting text.

* Every string in Python **automatically has these methods**.
* You **use them with a dot `.` after the string**.

---

### **Example**

```python
text = "hello world"

# Method to make all letters uppercase
print(text.upper())   # Output: "HELLO WORLD"

# Method to check if all characters are letters
print(text.isalpha())  # Output: False (because of the space)
```

✅ Key points:

1. Methods **act on the string**.
2. They **return a new result**; original string doesn’t change unless you save it.
3. They are **like tools** to do common tasks easily.

---

Think of it like this:

* `"hello".upper()` → “hey Python, make this string uppercase”
* `"123".isdigit()` → “hey Python, is this string a number?”
---
