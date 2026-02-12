# 🔹 What is a `while` Loop in Python?

A **while loop** is used to execute a block of code **as long as a condition is True**.

Unlike `for` loop (which iterates over a sequence),
a `while` loop runs **based on a condition**.

---

# 🔹 Technical Definition

A `while` loop is a control flow statement that repeatedly executes a block of code while a specified Boolean condition evaluates to True.

---

# 🔹 Basic Syntax

```python
while condition:
    # block of code
```

### Important:

* Condition must return **True or False**
* Loop stops when condition becomes **False**
* Indentation is mandatory

---

# 🔹 Example 1: Simple Counter

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

### Output:

```
1
2
3
4
5
```

---

# 🔹 How It Works (Step-by-Step)

1. Check condition → `i <= 5`
2. If True → execute block
3. Increase `i`
4. Check condition again
5. Repeat
6. Stop when condition becomes False

---

# 🔹 Real-Life Explanation

Imagine:
You keep filling a water tank **while it is not full**.

Condition: tank_not_full
When tank becomes full → stop.

That’s exactly how `while` works.

---

# 🔹 Example 2: Infinite Loop

```python
while True:
    print("Hello")
```

⚠ This will run forever unless stopped manually (Ctrl + C)

Used in:

* Servers
* Monitoring scripts
* Automation tools
* Background processes

---

# 🔹 Using `break` in while loop

Stops loop immediately.

```python
i = 1

while i <= 5:
    if i == 3:
        break
    print(i)
    i += 1
```

Output:

```
1
2
```

---

# 🔹 Using `continue`

Skips current iteration.

```python
i = 0

while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
```

Output:

```
1
2
4
5
```

---

# 🔹 while with else

Just like for loop, while also supports `else`.

```python
i = 1

while i <= 3:
    print(i)
    i += 1
else:
    print("Loop finished")
```

Output:

```
1
2
3
Loop finished
```

👉 `else` runs only if loop ends normally (not by break).

---

# 🔹 Difference Between for and while

| for loop                | while loop         |
| ----------------------- | ------------------ |
| Used for iterables      | Used for condition |
| Fixed iterations        | Unknown iterations |
| Cleaner for collections | Flexible control   |

---

# 🔹 Internal Working (Important for Interviews)

A while loop:

1. Evaluates condition
2. If True → executes block
3. Goes back to condition
4. Stops when condition is False

Unlike `for`, it does NOT automatically increment anything.
You must manually update variables.

---

# 🔹 Common Mistake (Very Important ⚠)

### Forgetting to update condition

```python
i = 1
while i <= 5:
    print(i)
```

This becomes **infinite loop** because `i` never changes.

---

# 🔹 Practical Example (DevOps Style)

### Example: Retry until success

```python
attempt = 1

while attempt <= 3:
    print("Trying to connect...")
    attempt += 1
```

Used in:

* API retries
* Service health checks
* Deployment scripts
* Monitoring systems

---

# 🔹 Nested While Loop

```python
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(i, j)
        j += 1
    i += 1
```

Used in:

* Pattern problems
* Matrix logic
* Complex iterations

---

# 🔹 When to Use while Loop?

✔ When number of iterations is unknown
✔ When waiting for user input
✔ When monitoring something
✔ When condition-based repetition needed

Example:

```python
password = ""

while password != "admin":
    password = input("Enter password: ")
```

---

# 🔹 Summary

A `while` loop:

* Runs based on a condition
* Stops when condition becomes False
* Needs manual variable update
* Can use break, continue, else
* Can become infinite if not handled properly

