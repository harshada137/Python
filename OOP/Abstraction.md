# Abstraction in Python

## Introduction

Abstraction means hiding implementation details while showing only the essential features to the user.

Python provides abstraction using the `abc` module.

Abstract classes cannot be instantiated directly.

---

## Why Use Abstraction?

- Hides unnecessary implementation.
- Improves code readability.
- Enforces a common interface.

---

## Example

```python
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
```

---

## Advantages

- Better maintainability
- Cleaner design
- Standardized implementation

---

## Key Points

- Uses the `abc` module.
- Abstract classes contain abstract methods.
- Child classes must implement abstract methods.
