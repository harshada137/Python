## 🔹 `range()` in Python

### ✅ Definition

`range()` is a **built-in function** used to generate a sequence of numbers.
It is commonly used with `for` loops to repeat an action a specific number of times.

It does **not** create a list directly — it returns a **range object** (an iterable).

---

# 📌 Syntax

```python
range(start, stop, step)
```

It has **3 possible forms**:

---

## 1️⃣ `range(stop)`

* Starts from **0**
* Ends at **stop - 1**

### Example:

```python
for i in range(5):
    print(i)
```

### Output:

```
0
1
2
3
4
```

👉 It starts from 0 automatically.

---

## 2️⃣ `range(start, stop)`

* Starts from `start`
* Ends at `stop - 1`

### Example:

```python
for i in range(2, 6):
    print(i)
```

### Output:

```
2
3
4
5
```

👉 6 is not included.

---

## 3️⃣ `range(start, stop, step)`

* Starts from `start`
* Ends before `stop`
* Increases or decreases by `step`

### Example:

```python
for i in range(1, 10, 2):
    print(i)
```

### Output:

```
1
3
5
7
9
```

👉 Step = 2 means increase by 2 each time.

---

# 🔹 Negative Step (Reverse Counting)

```python
for i in range(10, 0, -1):
    print(i)
```

### Output:

```
10
9
8
7
6
5
4
3
2
1
```

👉 When step is negative, counting goes backward.

---

# 🔥 Important Points

✔ `range()` excludes the stop value
✔ Default start = 0
✔ Default step = 1
✔ Works only with integers
✔ Memory efficient (does not store all values at once)

---

# 🧠 Convert range to list

```python
print(list(range(5)))
```

### Output:

```
[0, 1, 2, 3, 4]
```

---

# ⚠ Common Mistakes

❌ `range(5, 1)` → No output
Because default step is +1 but start > stop.

Correct way:

```python
range(5, 1, -1)
```

---

# 💡 Real Life Example

If you want to print something 5 times:

```python
for i in range(5):
    print("Hello")
```

---

# 🎯 Interview-Level Explanation

`range()` is an immutable sequence type used for looping a specific number of times. It generates numbers lazily, meaning it produces values on demand rather than storing them in memory.


