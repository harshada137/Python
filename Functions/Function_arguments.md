# Function Arguments in Python

## Introduction

Function arguments are values passed to a function when it is called. They allow functions to receive input data and perform operations based on that data.

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Harsha")
```

In this example:

* `name` is a parameter.
* `"Harsha"` is an argument.

---

# Types of Function Arguments in Python

## 1. Positional Arguments

Arguments are assigned to parameters based on their position.

```python
def student(name, age):
    print(f"Name: {name}, Age: {age}")

student("Harsha", 22)
```

**Output:**

```text
Name: Harsha, Age: 22
```

### Important

The order of arguments must match the order of parameters.

```python
student(22, "Harsha")
```

**Output:**

```text
Name: 22, Age: Harsha
```

---

## 2. Keyword Arguments

Arguments are passed using parameter names.

```python
def student(name, age):
    print(f"Name: {name}, Age: {age}")

student(age=22, name="Harsha")
```

**Output:**

```text
Name: Harsha, Age: 22
```

### Benefits

* Improves readability
* Order does not matter

---

## 3. Default Arguments

Parameters can have default values that are used when no argument is provided.

```python
def greet(name="Guest"):
    print(f"Hello, {name}")

greet()
greet("Harsha")
```

**Output:**

```text
Hello, Guest
Hello, Harsha
```

### Use Cases

* Optional settings
* Configuration values
* Default behavior

---

## 4. Variable-Length Positional Arguments (*args)

When the number of arguments is unknown, use `*args`.

```python
def add_numbers(*numbers):
    print(sum(numbers))

add_numbers(10, 20)
add_numbers(10, 20, 30, 40)
```

**Output:**

```text
30
100
```

### How It Works

```python
def show(*args):
    print(args)

show(1, 2, 3)
```

**Output:**

```text
(1, 2, 3)
```

`*args` stores values as a tuple.

---

## 5. Variable-Length Keyword Arguments (**kwargs)

When the number of keyword arguments is unknown, use `**kwargs`.

```python
def display_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

display_info(name="Harsha", age=22, city="Mumbai")
```

**Output:**

```text
name: Harsha
age: 22
city: Mumbai
```

### How It Works

```python
def show(**kwargs):
    print(kwargs)

show(name="John", age=25)
```

**Output:**

```text
{'name': 'John', 'age': 25}
```

`**kwargs` stores values as a dictionary.

---

## Combining Different Types of Arguments

Python allows combining multiple argument types in a single function.

```python
def employee(name, department="IT", *skills, **details):
    print("Name:", name)
    print("Department:", department)
    print("Skills:", skills)
    print("Details:", details)

employee(
    "Harsha",
    "DevOps",
    "AWS",
    "Kubernetes",
    experience=3,
    location="Mumbai"
)
```

**Output:**

```text
Name: Harsha
Department: DevOps
Skills: ('AWS', 'Kubernetes')
Details: {'experience': 3, 'location': 'Mumbai'}
```

---

# Argument vs Parameter

| Parameter                               | Argument                             |
| --------------------------------------- | ------------------------------------ |
| Variable defined in function definition | Value passed during function call    |
| Placeholder for data                    | Actual data supplied to the function |

### Example

```python
def add(a, b):  # a and b are parameters
    return a + b

add(10, 20)     # 10 and 20 are arguments
```

---

# Rules for Function Arguments

### Correct Order

When defining a function, parameters should generally follow this order:

```python
def function_name(
    positional,
    default_value="default",
    *args,
    **kwargs
):
    pass
```

### Example

```python
def example(a, b=10, *args, **kwargs):
    print(a, b, args, kwargs)
```

---

# Practical Examples

## Calculator Function

```python
def multiply(a, b):
    return a * b

print(multiply(5, 4))
```

**Output:**

```text
20
```

---

## Flexible Sum Function

```python
def total(*numbers):
    return sum(numbers)

print(total(10, 20))
print(total(10, 20, 30, 40, 50))
```

**Output:**

```text
30
150
```

---

## User Profile Function

```python
def create_profile(**user):
    for key, value in user.items():
        print(f"{key}: {value}")

create_profile(
    name="Harsha",
    role="DevOps Engineer",
    country="India"
)
```

---

# Best Practices

1. Use meaningful parameter names.
2. Provide default values when appropriate.
3. Use keyword arguments for better readability.
4. Use `*args` only when the number of inputs is unknown.
5. Use `**kwargs` for flexible configuration options.
6. Keep the number of parameters reasonable.
7. Document expected arguments using docstrings.

---

# Summary

Function arguments allow data to be passed into functions, making them flexible and reusable. Python supports several types of arguments:

* **Positional Arguments** – Based on order.
* **Keyword Arguments** – Based on parameter names.
* **Default Arguments** – Use predefined values when no argument is provided.
* **`*args`** – Accept multiple positional arguments.
* **`**kwargs`** – Accept multiple keyword arguments.

Understanding these argument types is essential for writing scalable, reusable, and professional Python code.
