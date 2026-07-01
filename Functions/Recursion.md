# Recursion in Python

## Introduction

Recursion is a programming technique in which a function calls itself to solve a problem. Instead of using loops, recursion breaks a complex problem into smaller, similar subproblems until a simple condition is reached. This stopping condition is known as the **base case**.



## How Recursion Works

A recursive function has two essential parts:

1. **Base Case** – Stops the recursion.
2. **Recursive Case** – Calls the function itself with a smaller or modified input.

Without a base case, recursion continues indefinitely and results in a `RecursionError`.



## Basic Syntax

```python
def function_name(parameters):
    if base_condition:
        return result
    return function_name(modified_parameters)
```



## Example 1: Print Numbers from 1 to N

```python
def print_numbers(n):
    if n == 0:
        return
    print_numbers(n - 1)
    print(n)

print_numbers(5)
```

**Output**

```text
1
2
3
4
5
```



## Example 2: Factorial Using Recursion

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
```

**Output**

```text
120
```



## Example 3: Fibonacci Series

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(6):
    print(fibonacci(i), end=" ")
```

**Output**

```text
0 1 1 2 3 5
```



## Example 4: Sum of First N Natural Numbers

```python
def sum_numbers(n):
    if n == 0:
        return 0
    return n + sum_numbers(n - 1)

print(sum_numbers(5))
```

**Output**

```text
15
```



## Advantages of Recursion

- Makes code simpler for problems that can be divided into smaller subproblems.
- Produces cleaner and more readable code for tree and graph traversals.
- Naturally fits divide-and-conquer algorithms.
- Reduces the need for complex loops in certain problems.



## Disadvantages of Recursion

- Uses more memory because each function call is stored on the call stack.
- Can be slower than iteration due to function call overhead.
- Deep recursion may cause a `RecursionError`.
- Some recursive solutions are less efficient if repeated calculations are involved.



## Common Applications

- Factorial calculation
- Fibonacci sequence
- Tree traversal
- Directory traversal
- Binary search
- Divide and conquer algorithms (Merge Sort, Quick Sort)
- Backtracking problems (Maze, Sudoku, N-Queens)



## Best Practices

- Always define a proper **base case**.
- Ensure each recursive call moves toward the base case.
- Avoid unnecessary recursive calls.
- Use iteration instead of recursion for very deep recursive problems when possible.
- Consider memoization for recursive problems with repeated calculations.



## Theory Notes

- Recursion is a technique where a function **calls itself** to solve smaller instances of the same problem.
- Every recursive function must have a **base case** to stop execution.
- Python stores each recursive call in the **call stack**, which is removed as functions return.
- Recursive solutions are elegant for hierarchical and divide-and-conquer problems but may consume more memory than iterative solutions.
- Choosing between recursion and iteration depends on the problem, readability, and performance requirements.



## Summary

Recursion is a powerful programming technique that simplifies problems by breaking them into smaller, self-similar tasks. A well-designed recursive function always contains a base case and a recursive case. While recursion improves code readability for many algorithms, it should be used carefully to avoid excessive memory usage and stack overflow errors.
