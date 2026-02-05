# 1️⃣ Input / Output in Python

## What is Input?

**Input** means taking data **from the user** while the program is running.

### `input()` function

```python
name = input("Enter your name: ")
```

🔹 Always returns **string type**

```python
age = input("Enter age: ")
print(type(age))   # <class 'str'>
```

---

### Taking Numeric Input

We use **type casting** with `input()`.

```python
age = int(input("Enter age: "))
salary = float(input("Enter salary: "))
```

---

## What is Output?

**Output** means displaying data to the user.

### `print()` function

```python
print("Hello Python")
```

---

### Printing Variables

```python
name = "Harshada"
print(name)
```

---

### Multiple Values

```python
a = 10
b = 20
print(a, b)
```

---

### Using Separator

```python
print(1, 2, 3, sep="-")
# Output: 1-2-3
```

---

### Using `end`

```python
print("Hello", end=" ")
print("World")
# Output: Hello World
```

---

### Formatted Output

#### Using f-string (Recommended)

```python
name = "Harshada"
age = 22
print(f"My name is {name} and age is {age}")
```

---

# 2️⃣ Operators in Python

## What are Operators?

**Operators** are symbols used to **perform operations on values or variables**.

Example:

```python
a = 10 + 5
```

---

## Types of Operators in Python


## 1. Arithmetic Operators

Used for mathematical calculations.

| Operator | Meaning        |
| -------- | -------------- |
| `+`      | Addition       |
| `-`      | Subtraction    |
| `*`      | Multiplication |
| `/`      | Division       |
| `%`      | Modulus        |
| `//`     | Floor Division |
| `**`     | Power          |

```python
a = 10
b = 3

print(a + b)   # 13
print(a % b)   # 1
print(a ** b)  # 1000
```

---

## 2. Assignment Operators

Used to assign values.

| Operator | Example |
| -------- | ------- |
| `=`      | x = 10  |
| `+=`     | x += 5  |
| `-=`     | x -= 5  |
| `*=`     | x *= 2  |
| `/=`     | x /= 2  |

```python
x = 10
x += 5
print(x)  # 15
```

---

## 3. Comparison (Relational) Operators

Used to compare values.
Returns **True or False**.

| Operator | Meaning          |
| -------- | ---------------- |
| `==`     | Equal            |
| `!=`     | Not equal        |
| `>`      | Greater          |
| `<`      | Less             |
| `>=`     | Greater or equal |
| `<=`     | Less or equal    |

```python
print(10 > 5)   # True
print(10 == 5)  # False
```

---

## 4. Logical Operators

Used with conditions.

| Operator | Meaning        |
| -------- | -------------- |
| `and`    | Both true      |
| `or`     | Any true       |
| `not`    | Reverse result |

```python
a = 10
b = 5

print(a > 5 and b < 10)  # True
```

---

## 5. Identity Operators

Check **same object in memory**.

| Operator | Meaning          |
| -------- | ---------------- |
| `is`     | Same object      |
| `is not` | Different object |

```python
a = 10
b = 10
print(a is b)   # True
```

---

## 6. Membership Operators

Check presence in sequence.

| Operator | Meaning    |
| -------- | ---------- |
| `in`     | Exists     |
| `not in` | Not exists |

```python
nums = [1, 2, 3]
print(2 in nums)      # True
print(5 not in nums)  # True
```

---

## 7. Bitwise Operators (Basic)

Operate on binary values.

| Operator | Meaning     |    |
| -------- | ----------- | -- |
| `&`      | AND         |    |
| `        | `           | OR |
| `^`      | XOR         |    |
| `~`      | NOT         |    |
| `<<`     | Left shift  |    |
| `>>`     | Right shift |    |

```python
print(5 & 3)   # 1
```

---

# 🔑 Important Notes

* `input()` → always **string**
* Use **type casting** for calculations
* Operators are heavily used in **conditions, loops, logic**

---

## Quick Summary

* **Input** → `input()`
* **Output** → `print()`
* Operators perform actions on data
* Main operator types:

  * Arithmetic
  * Assignment
  * Comparison
  * Logical
  * Identity
  * Membership
  * Bitwise

---

