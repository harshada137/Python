# Naming Conventions in Python

Naming conventions are **standardized rules and guidelines** for naming variables, functions, classes, and other identifiers in Python. Following these conventions makes your code more readable, professional, and easier for others (and yourself) to understand.


---


## Why Naming Conventions Matter

```python
# Bad naming - hard to understand
x = 50
y = 20
z = x * y

# Good naming - clear and understandable
price_per_item = 50
quantity = 20
total_cost = price_per_item * quantity
```

The second example is immediately clear about what the code does!


---


## Mandatory Rules (Must Follow)

These are **strict rules** that Python enforces. Breaking them will cause errors.

### 1. **Must Start with Letter or Underscore**
```python
# Valid ✓
name = "John"
_private = 100
user1 = "Alice"

# Invalid ✗
1name = "John"      # Error: can't start with number
@username = "Bob"   # Error: can't start with @
```

### 2. **Only Letters, Numbers, and Underscores**
```python
# Valid ✓
user_name = "Alice"
user123 = "Bob"
_temp_value = 50

# Invalid ✗
user-name = "Alice"    # Error: hyphen not allowed
user.name = "Bob"      # Error: dot not allowed
user name = "Charlie"  # Error: space not allowed
user#1 = "Dave"        # Error: # not allowed
```

### 3. **Case Sensitive**
```python
age = 25
Age = 30
AGE = 35

print(age)   # 25
print(Age)   # 30
print(AGE)   # 35
# These are three different variables!
```

### 4. **Cannot Use Reserved Keywords**
Python has 35 reserved keywords that have special meanings:

```python
# Invalid ✗
class = "Math"      # Error: 'class' is a keyword
for = 10            # Error: 'for' is a keyword
if = True           # Error: 'if' is a keyword

# Valid ✓
class_name = "Math"
for_loop = 10
if_condition = True
```

**Python Keywords:**
```
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
```

You can check if a word is a keyword:
```python
import keyword
print(keyword.iskeyword("class"))  # True
print(keyword.iskeyword("name"))   # False
```

---


## Recommended Conventions (Should Follow)

These are **strong recommendations** followed by the Python community (defined in PEP 8 - Python's style guide).

### 1. **snake_case for Variables and Functions**

Use lowercase letters with underscores separating words:

```python
# Variables
user_name = "Alice"
total_price = 99.99
is_active = True
student_count = 30
first_name = "John"

# Functions
def calculate_total():
    pass

def get_user_name():
    pass

def send_email_notification():
    pass
```

**Why snake_case?** It's the official Python convention and makes multi-word names very readable.

### 2. **PascalCase for Classes**

Use capital letters at the start of each word, no underscores:

```python
class Student:
    pass

class BankAccount:
    pass

class ShoppingCart:
    pass

class UserAuthentication:
    pass
```

### 3. **UPPER_CASE for Constants**

Use all uppercase letters with underscores:

```python
PI = 3.14159
MAX_SPEED = 120
DEFAULT_TIMEOUT = 30
DATABASE_URL = "localhost:5432"
GRAVITATIONAL_CONSTANT = 9.8

# Usage
circumference = 2 * PI * radius
```

Constants are values that shouldn't change throughout the program.

### 4. **Single Leading Underscore for Internal Use**

Indicates "internal use" or "private" (by convention):

```python
_internal_variable = 100
_temp_data = "processing"

def _internal_function():
    pass

class MyClass:
    def __init__(self):
        self._internal_attribute = 10  # "private" by convention
```

### 5. **Double Leading Underscore for Name Mangling**

Used in classes to avoid naming conflicts:

```python
class MyClass:
    def __init__(self):
        self.__private = 100  # Strongly "private"
```

### 6. **Double Leading and Trailing Underscores**

Reserved for special Python methods (magic methods):

```python
__init__()
__str__()
__len__()
__add__()

# Don't create your own names like this!
```

---


## Naming Style Comparison

Here's a quick reference of different naming styles:

| Style | Example | Used For |
|-------|---------|----------|
| snake_case | `user_name`, `total_price` | Variables, functions |
| PascalCase | `UserAccount`, `ShoppingCart` | Classes |
| UPPER_CASE | `MAX_VALUE`, `PI` | Constants |
| camelCase | `userName`, `totalPrice` | Not typical in Python |
| _leading_underscore | `_internal_var` | Internal/private |
| __double_leading | `__private_var` | Strongly private |


---


## Best Practices for Descriptive Names

### 1. **Be Descriptive and Clear**

```python
# Bad ✗
x = 25
a = "John"
temp = 100

# Good ✓
age = 25
student_name = "John"
temperature_celsius = 100
```

### 2. **Use Full Words, Not Abbreviations**

```python
# Bad ✗
usr_nm = "Alice"
qty = 50
prod_prc = 99.99

# Good ✓
user_name = "Alice"
quantity = 50
product_price = 99.99

# Acceptable abbreviations (widely understood)
id = 123
url = "https://example.com"
html = "<div></div>"
```

### 3. **Boolean Variables Should Sound Like Questions**

```python
# Good ✓
is_active = True
has_permission = False
can_edit = True
is_valid = False
should_update = True
```

### 4. **Use Meaningful Names for Lists and Collections**

```python
# Bad ✗
data = ["apple", "banana"]
items = [1, 2, 3]

# Good ✓
fruits = ["apple", "banana"]
student_scores = [85, 90, 78]
user_names = ["Alice", "Bob", "Charlie"]
```

### 5. **Avoid Single Letter Names (Except in Specific Cases)**

```python
# Bad ✗
for a in range(10):
    b = a * 2
    print(b)

# Good ✓
for number in range(10):
    doubled = number * 2
    print(doubled)

# Acceptable single letters
for i in range(10):        # Loop counters: i, j, k
    pass

x, y, z = 1, 2, 3         # Coordinates
e = 2.71828               # Mathematical constants
```

### 6. **Function Names Should Be Verbs**

```python
# Good ✓
def calculate_total():
    pass

def get_user_input():
    pass

def send_email():
    pass

def validate_password():
    pass

def update_database():
    pass
```

---


## Common Naming Patterns

### Counters and Indices
```python
count = 0
index = 0
student_count = 25
item_index = 3
```

### Temporary Variables
```python
temp = value
tmp_result = calculation()
```

### Maximum and Minimum
```python
max_value = 100
min_age = 18
maximum_score = 100
```

### File and Path Names
```python
file_name = "data.txt"
file_path = "/home/user/documents"
output_file = "results.csv"
```

---


## Real-World Examples

```python
# Student grade calculator
student_name = "Alice Johnson"
test_score = 85
homework_score = 92
participation_score = 88

total_score = test_score + homework_score + participation_score
average_score = total_score / 3
is_passing = average_score >= 60

# Constants
PASSING_GRADE = 60
MAX_SCORE = 100

# Function
def calculate_final_grade(test, homework, participation):
    total = test + homework + participation
    return total / 3

# Class
class StudentRecord:
    def __init__(self, name, score):
        self.student_name = name
        self.final_score = score
        self._grade_letter = None  # Internal use
```

---


## Summary Table

| Category | Convention | Example |
|----------|------------|---------|
| Variables | snake_case | `user_name`, `total_count` |
| Functions | snake_case | `get_data()`, `calculate_sum()` |
| Classes | PascalCase | `Student`, `BankAccount` |
| Constants | UPPER_CASE | `PI`, `MAX_SIZE` |
| Private | _leading | `_internal_var` |
| Magic methods | __double__ | `__init__`, `__str__` |


---


## Key Takeaways

1. **Follow Python's PEP 8 style guide** for consistency
2. **Use snake_case** for most variable and function names
3. **Use PascalCase** for class names
4. **Use UPPER_CASE** for constants
5. **Be descriptive** - clarity over brevity
6. **Avoid abbreviations** unless they're universally understood
7. **Make booleans sound like yes/no questions**
8. **Never use Python keywords** as variable names

Following these naming conventions will make your Python code professional, readable, and easier to maintain!
