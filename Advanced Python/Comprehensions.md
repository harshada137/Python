# Comprehensions in Python

## Introduction

Comprehensions provide a concise and readable way to create collections such as lists, dictionaries, and sets.

Instead of writing multiple lines of code using loops, comprehensions allow the same task to be completed in a single line.

Python supports:

- List Comprehension
- Dictionary Comprehension
- Set Comprehension

---

## Syntax

### List Comprehension

```python
[expression for item in iterable]
```

---

## Example

```python
numbers = [1, 2, 3, 4, 5]

squares = [num ** 2 for num in numbers]

print(squares)
```

**Output**

```
[1, 4, 9, 16, 25]
```

---

## Advantages

- Less code
- Better readability
- Faster than traditional loops in many cases

---

## Key Points

- Best suited for simple transformations.
- Avoid overly complex comprehensions as they reduce readability.
