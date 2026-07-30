# Generators in Python

## Introduction

Generators are a special type of iterator that generate values one at a time instead of storing all values in memory.

They use the `yield` keyword instead of `return`.

Generators are useful when working with large datasets because they consume very little memory.

---

## Syntax

```python
def function():
    yield value
```

---

## Example

```python
def numbers():
    yield 1
    yield 2
    yield 3

for num in numbers():
    print(num)
```

**Output**

```
1
2
3
```

---

## Advantages

- Memory efficient
- Faster for large datasets
- Values are generated only when needed

---

## Key Points

- Uses the `yield` keyword.
- Returns one value at a time.
- Every generator is an iterator.
