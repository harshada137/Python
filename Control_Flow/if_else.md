## **1️⃣ `if` Statement (Basic Conditional)**

### **Purpose:**

The `if` statement **checks a condition** (True or False) and runs code **only if the condition is True**.
If the condition is False, Python simply **skips the block**.

### **Syntax:**

```python
if condition:
    # code block (indented)
```

### **Rules:**

1. The code under `if` **must be indented** (Python uses indentation to define blocks).
2. The condition must evaluate to **True or False**.

### **Example:**

```python
temperature = 30

if temperature > 25:
    print("It's hot today!")
```

**Output:**

```
It's hot today!
```

* Here, `temperature > 25` is `True`, so the block runs.
* If `temperature = 20`, nothing would print.

---

### ✅ **Key Points:**

* You can have multiple `if` statements **independently**:

```python
x = 10
y = 5

if x > y:
    print("x is bigger than y")
if y > 0:
    print("y is positive")
```

**Output:**

```
x is bigger than y
y is positive
```

* Both conditions are checked **separately**, unlike `elif`.

---

## **2️⃣ `if-else` Statement**

### **Purpose:**

* Runs one block if the condition is True
* Runs another block if the condition is False

### **Syntax:**

```python
if condition:
    # executes if condition is True
else:
    # executes if condition is False
```

### **Example:**

```python
age = 16

if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult yet.")
```

**Output:**

```
You are not an adult yet.
```

Here:

* `age >= 18` → False
* So Python executes the `else` block.

---

### ✅ **Key Points:**

1. `else` **does not take a condition** — it only runs when **all previous conditions fail**.
2. `if-else` ensures **one of the two blocks always runs**.

---

## **3️⃣ `elif` Statement (Multiple Conditions)**

### **Purpose:**

* Short for **“else if”**
* Allows you to check **multiple conditions in sequence**
* Stops checking further as soon as **one condition is True**

### **Syntax:**

```python
if condition1:
    # block1
elif condition2:
    # block2
elif condition3:
    # block3
else:
    # block4 (optional)
```

### **Flow Logic:**

1. Python checks `if` → True? Execute block → skip rest
2. Else, check `elif1` → True? Execute block → skip rest
3. Else, check `elif2` → True? Execute block → skip rest
4. If none True → `else` block executes

### **Example:**

```python
marks = 82

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: F")
```

**Output:**

```
Grade: B
```

* Python checks:

  1. `marks >= 90` → False
  2. `marks >= 75` → True ✅ → Executes block and **stops checking**
  3. `marks >= 50` → Skipped

---

### ✅ **Key Points:**

* You can have **any number of `elif` statements**.
* `else` is optional.
* Python checks **conditions top to bottom**.

---

## **4️⃣ Practical Example (Combining All)**

```python
temperature = 28
humidity = 80

if temperature > 35:
    print("It's extremely hot!")
elif temperature > 25 and humidity > 70:
    print("It's hot and humid.")
elif temperature > 25:
    print("It's warm.")
else:
    print("It's cool.")
```

**Output:**

```
It's hot and humid.
```

* Here, we combined `and` logical operator → more complex conditions.
* Only the **first True condition executes**.

---

## **5️⃣ Visual Flow (Mental Diagram)**

```
Start
  |
  v
Check `if condition1`
  |---True--> Execute block1 --> END
  |
  v
Check `elif condition2`
  |---True--> Execute block2 --> END
  |
  v
Check `elif condition3`
  |---True--> Execute block3 --> END
  |
  v
Else
  |--> Execute else block --> END
```

---

## **6️⃣ Common Mistakes to Avoid**

1. **No colon** after `if`, `elif`, or `else` → SyntaxError

```python
if x > 5   # ❌ Missing colon
```

2. **Wrong indentation** → Python will throw `IndentationError`

```python
if x > 5:
print("Hello")  # ❌ Not indented
```

3. **Using multiple independent `if` when you meant `elif`**

```python
marks = 80

if marks >= 90:
    print("A")
if marks >= 75:
    print("B")  # ❌ Both can run, should be elif
```

---

### **7️⃣ Summary**

| Statement | When to Use                     | Execution Flow                                           |
| --------- | ------------------------------- | -------------------------------------------------------- |
| `if`      | Single condition to check       | Runs only if True, else skip                             |
| `if-else` | Two possible outcomes           | Runs True block if True, else False block                |
| `elif`    | Multiple conditions in sequence | Checks in order, first True block executes, rest skipped |


