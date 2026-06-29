# Python Lambda Functions

## What is a Lambda Function?

A **lambda function** is a small, anonymous (nameless) function in Python that can have any number of arguments but only **one expression**. It is commonly used for short, simple operations where defining a full function using `def` is unnecessary.

The result of the expression is automatically returned, so there is no need to use the `return` keyword.



## Syntax

```python
lambda arguments: expression
```

- `lambda` is the keyword used to create an anonymous function.
- `arguments` are the input parameters.
- `expression` is the operation to be performed.
- The value of the expression is returned automatically.



## Why Use Lambda Functions?

Lambda functions are useful because they:

- Make the code shorter and more readable for simple operations.
- Eliminate the need to define a separate function using `def`.
- Are commonly used with functions like `map()`, `filter()`, and `sorted()`.
- Can be passed as arguments to other functions.



## How Lambda Functions Work

1. Python reads the `lambda` keyword.
2. It accepts the input arguments.
3. The expression is evaluated.
4. The result of the expression is returned automatically.

Unlike regular functions, lambda functions cannot contain multiple statements or complex logic.



## Difference Between `def` Function and Lambda Function

| Regular Function (`def`) | Lambda Function |
|---------------------------|-----------------|
| Has a function name. | Anonymous (no name required). |
| Can contain multiple statements. | Can contain only one expression. |
| Uses the `return` keyword. | Returns the result automatically. |
| Better for complex logic. | Best for short and simple operations. |



## Example 1: Lambda Function to Add Two Numbers

```python
add = lambda a, b: a + b

result = add(10, 20)

print(result)
```

**Output**

```
30
```

**Explanation**

- The lambda function accepts two arguments.
- It adds them together.
- The result is returned automatically and stored in the variable `result`.

---

## Example 2: Using Lambda with `sorted()`

```python
students = [
    ("Harshada", 85),
    ("Amit", 92),
    ("Priya", 78)
]

sorted_students = sorted(students, key=lambda student: student[1])

print(sorted_students)
```

**Output**

```python
[('Priya', 78), ('Harshada', 85), ('Amit', 92)]
```

**Explanation**

- The `sorted()` function sorts the list.
- The lambda function returns the second element (marks) from each tuple.
- The list is sorted in ascending order based on marks.



## Limitations of Lambda Functions

- Can contain only one expression.
- Cannot include loops, multiple statements, or complex logic.
- Less readable when the expression becomes too long.
- Not suitable for large or reusable functions.



## When Should You Use Lambda Functions?

Use lambda functions when:

- The function is small and simple.
- It is needed only once.
- It is being passed as an argument to another function.
- You want concise and readable code.

Avoid lambda functions when:

- The function contains multiple statements.
- The logic is complex.
- The function needs documentation or frequent reuse.



## Important Points

- Lambda functions are anonymous functions.
- They can accept any number of arguments.
- They contain only one expression.
- The expression's result is returned automatically.
- They are widely used with `map()`, `filter()`, `reduce()`, and `sorted()`.
- For complex operations, regular functions (`def`) are preferred.



## Summary

Lambda functions provide a concise way to create small, anonymous functions in Python. They are ideal for simple operations, especially when used with built-in functions like `map()`, `filter()`, and `sorted()`. While they make code shorter and cleaner, regular functions should be used whenever the logic becomes more complex or requires multiple statements.
