# Polymorphism in Python

## Introduction

Polymorphism means **"many forms."**

The same method can behave differently depending on the object that calls it.

Python supports polymorphism through method overriding and built-in functions.

---

## Example

```python
class Dog:

    def sound(self):
        print("Bark")

class Cat:

    def sound(self):
        print("Meow")

animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()
```

**Output**

```
Bark
Meow
```

---

## Advantages

- Flexible code
- Better maintainability
- Easy code extension

---

## Key Points

- Same interface, different implementations.
- Commonly achieved using method overriding.
