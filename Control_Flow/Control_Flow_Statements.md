
# 1️⃣ `break` Statement

### 🔹 Definition:

The `break` statement is used to **immediately exit a loop**, even if the loop condition is still true.

It works inside:

* `for` loop
* `while` loop

### 🔹 Syntax:

```python
for variable in sequence:
    if condition:
        break
```

### 🔹 Example 1 (for loop):

```python
for i in range(1, 6):
    if i == 3:
        break
    print(i)
```

### 🔹 Output:

```
1
2
```

👉 When `i` becomes `3`, the loop stops immediately.

---

### 🔹 Example 2 (while loop):

```python
i = 1
while i <= 5:
    if i == 4:
        break
    print(i)
    i += 1
```

### 🔹 Output:

```
1
2
3
```

### ✅ When to use `break`?

* When you find what you're searching for.
* When a condition is met and no further looping is needed.
* To avoid unnecessary iterations.

---

# 2️⃣ `continue` Statement

### 🔹 Definition:

The `continue` statement **skips the current iteration** and moves to the next iteration of the loop.

It does NOT stop the loop completely.

### 🔹 Syntax:

```python
for variable in sequence:
    if condition:
        continue
```

### 🔹 Example:

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

### 🔹 Output:

```
1
2
4
5
```

👉 When `i == 3`, that iteration is skipped, but the loop continues.

---

### 🔹 Another Example:

Print only even numbers:

```python
for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i)
```

### 🔹 Output:

```
2
4
6
8
10
```

### ✅ When to use `continue`?

* To skip unwanted values.
* To filter data inside loops.
* To avoid deeply nested `if` statements.

---

# 3️⃣ `pass` Statement

### 🔹 Definition:

The `pass` statement does **nothing**.

It is used as a **placeholder** when a statement is required syntactically but you don’t want to write code yet.

### 🔹 Example 1:

```python
for i in range(5):
    pass
```

👉 The loop runs, but nothing happens.

---

### 🔹 Example 2 (Empty function):

```python
def my_function():
    pass
```

Without `pass`, Python will give an error because the function body cannot be empty.

---

### 🔹 Example 3 (Empty class):

```python
class MyClass:
    pass
```

---

### ✅ When to use `pass`?

* While writing code structure.
* When planning to implement later.
* In empty functions, classes, or conditions.

---

# 🔥 Difference Between break, continue, pass

| Statement  | Stops Loop? | Skips Iteration? | Does Nothing? |
| ---------- | ----------- | ---------------- | ------------- |
| `break`    | ✅ Yes       | ❌ No             | ❌ No          |
| `continue` | ❌ No        | ✅ Yes            | ❌ No          |
| `pass`     | ❌ No        | ❌ No             | ✅ Yes         |

---

# 💡 Simple Real-Life Analogy

Imagine you are reading a book:

* 📕 `break` → You close the book and stop reading completely.
* 📘 `continue` → You skip one page and continue reading.
* 📄 `pass` → You look at the page but do nothing.

---

**In Python, break, continue, and pass are control flow statements. They control how loops and blocks of code behave.**


