# Python `return` Statement

## What is the `return` Statement?

The `return` statement is used inside a function to send a value back to the place where the function was called. Once a `return` statement is executed, the function immediately stops executing, and the returned value becomes the result of the function call.

Unlike the `print()` function, which only displays output on the screen, `return` allows the returned value to be stored in a variable, used in expressions, or passed to another function.



## Syntax

```python
def function_name(parameters):
    # Function logic
    return value
```

- `return` is always written inside a function.
- The value after `return` can be a variable, expression, object, or multiple values.
- A function can have multiple `return` statements, but only one is executed during a single function call.



## Why Use `return`?

The `return` statement is useful because it:

- Sends the result of a function back to the caller.
- Makes functions reusable and modular.
- Allows the returned value to be stored and used later.
- Stops the execution of the function immediately.



## How `return` Works

1. The function is called.
2. The function executes its code.
3. When Python encounters a `return` statement:
   - The specified value is returned.
   - The function execution ends immediately.
4. The returned value can be assigned to a variable or used directly.



## Difference Between `return` and `print()`

| `return` | `print()` |
|----------|-----------|
| Sends a value back to the caller. | Displays output on the screen. |
| Can be stored in a variable. | Cannot be stored directly. |
| Ends the function execution. | Does not stop the function. |
| Used when a result needs to be reused. | Used for displaying information. |



## Example 1: Returning a Value

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

**Output**

```
30
```

**Explanation**

- The function calculates the sum of two numbers.
- The `return` statement sends the result (`30`) back to the caller.
- The returned value is stored in the variable `result`.



## Example 2: Returning Multiple Values

```python
def student():
    name = "Harshada"
    age = 22
    return name, age

name, age = student()

print(name)
print(age)
```

**Output**

```
Harshada
22
```

**Explanation**

- Python allows returning multiple values separated by commas.
- Internally, these values are returned as a tuple.
- They can be unpacked into separate variables.



## Important Points

- Every function returns a value.
- If no `return` statement is written, Python automatically returns `None`.
- A function can return numbers, strings, lists, dictionaries, objects, or even other functions.
- Code written after a `return` statement inside the same block is never executed.
- `return` makes functions reusable because the returned value can be used anywhere in the program.

---

## Summary

The `return` statement is one of the most important concepts in Python functions. It allows a function to produce a result that can be reused elsewhere in the program. Unlike `print()`, which only displays output, `return` makes functions flexible, modular, and suitable for real-world applications.
