# Iterators in Python

## Introduction

An iterator is an object that allows you to traverse through the elements of a collection one item at a time.

Python automatically uses iterators in loops such as `for`.

An iterator remembers its current position and returns the next element whenever requested.

---

## How Iterators Work

An iterator implements two methods:

- `__iter__()`
- `__next__()`

When no elements remain, Python raises the `StopIteration` exception.

---

## Example

```python
numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
```

**Output**

```
10
20
```

---

## Advantages

- Efficient memory usage
- Processes data one element at a time
- Useful for large collections

---

## Key Points

- Every iterator is iterable.
- Iterators are consumed after use.
- `next()` retrieves the next item.
