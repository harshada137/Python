# 🔹 What are Nested Conditions in Python?

**Nested conditions** mean placing one `if` (or `if-else`) statement inside another `if` (or `else`) block.

In simple words:
👉 When a condition depends on another condition, we use **nested if statements**.

---

# 1️⃣ Basic Syntax

```python
if condition1:
    # Block 1
    if condition2:
        # Block 2
    else:
        # Block 3
else:
    # Block 4
```

* First, `condition1` is checked.
* If it is `True`, then `condition2` is checked.
* If `condition1` is `False`, the outer `else` block executes.

---

# 2️⃣ Simple Example

### Example 1: Number Checking

```python
num = 10

if num > 0:
    print("Number is positive")
    
    if num % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")
else:
    print("Number is negative")
```

### 🔎 How it works:

* First condition: `num > 0` → True
* Then inner condition: `num % 2 == 0` → True
* Output:

```
Number is positive
Number is even
```

---

# 3️⃣ Real-Life Example

### Example 2: Login System

```python
username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login Successful")
    else:
        print("Incorrect Password")
else:
    print("Username not found")
```

### Explanation:

* First check: Is username correct?
* If yes → Check password.
* If username is wrong → No need to check password.

👉 This is practical logic used in authentication systems.

---

# 4️⃣ Multiple Nested Levels

You can nest more than one level.

```python
marks = 85

if marks >= 50:
    print("Pass")
    
    if marks >= 75:
        print("Distinction")
        
        if marks >= 90:
            print("Excellent")
```

### Output:

```
Pass
Distinction
```

⚠️ But too many nested levels make code hard to read.

---

# 5️⃣ Nested `if-elif-else`

```python
age = 25
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to vote")
    else:
        print("Not a citizen")
else:
    print("Underage")
```

---

# 6️⃣ Flow Diagram Logic

Think of it like:

```
Check Condition 1
    ├── True → Check Condition 2
    │           ├── True → Do Something
    │           └── False → Do Something Else
    └── False → Do Another Thing
```

---

# 7️⃣ Why Use Nested Conditions?

✔ When decision depends on another decision
✔ Used in:

* Login systems
* Menu-driven programs
* Validation checks
* Role-based access
* Cloud/DevOps condition-based automation

---

# 8️⃣ Common Mistakes

### ❌ 1. Wrong Indentation

```python
if x > 0:
print("Positive")   # ❌ Error
```

Python depends on indentation.

---

### ❌ 2. Too Many Nesting Levels

Bad Practice:

```python
if a:
    if b:
        if c:
            if d:
                print("Too deep")
```

👉 Better to simplify using logical operators.

---

# 9️⃣ Alternative to Nested Conditions (Using Logical Operators)

Instead of:

```python
if age >= 18:
    if citizen:
        print("Eligible")
```

You can write:

```python
if age >= 18 and citizen:
    print("Eligible")
```

✅ Cleaner
✅ More readable
✅ Preferred in real projects

---

# 🔟 When NOT to Use Nested Conditions?

If conditions are independent, use:

* `elif`
* `and`, `or`
* Functions
* Dictionary mapping

---

# 🧠 Summary

| Concept          | Meaning                         |
| ---------------- | ------------------------------- |
| Nested Condition | `if` inside another `if`        |
| Purpose          | Multi-level decision making     |
| Risk             | Reduces readability if too deep |
| Alternative      | Use logical operators           |

---

# 🚀 Interview Definition

**Nested conditions in Python refer to placing one conditional statement inside another conditional block to implement multi-level decision-making logic. They are commonly used when one condition must be evaluated only after another condition evaluates to true.**


* Give interview-based tricky questions
* Or connect this with real DevOps/Linux automation examples 😊
