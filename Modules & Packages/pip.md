# pip

## What is pip?

**pip** stands for **"Pip Installs Packages."** It is Python's official package manager used to install, update, remove, and manage third-party Python packages.

Many useful libraries are not included with Python. These external libraries can be downloaded and installed using pip.

pip is installed automatically with most modern versions of Python.

---

## Why Do We Need pip?

Python provides many built-in modules, but sometimes we need additional functionality such as:

- Data analysis
- Web development
- Machine learning
- Artificial Intelligence
- Automation
- Data visualization
- Database connectivity

Instead of writing everything from scratch, we can install ready-made packages using pip.

---

## Features of pip

- Installs third-party packages
- Updates installed packages
- Removes packages
- Displays installed packages
- Shows package information
- Installs specific package versions
- Manages package dependencies
- Downloads packages from the Python Package Index (PyPI)

---

## What is PyPI?

**PyPI (Python Package Index)** is the official online repository for Python packages.

Thousands of free packages are available on PyPI, and pip downloads packages from there.

Website:

```
https://pypi.org
```

---

## Basic pip Commands

### 1. Install a Package

```bash
pip install requests
```

---

### 2. Install a Specific Version

```bash
pip install requests==2.31.0
```

---

### 3. Upgrade a Package

```bash
pip install --upgrade requests
```

---

### 4. Uninstall a Package

```bash
pip uninstall requests
```

---

### 5. View Installed Packages

```bash
pip list
```

---

### 6. Show Package Information

```bash
pip show requests
```

---

### 7. Check pip Version

```bash
pip --version
```

---

### 8. Search for Help

```bash
pip help
```

---

### 9. Freeze Installed Packages

This command lists all installed packages and their versions.

```bash
pip freeze
```

It is commonly used to create a requirements file.

---

### 10. Install Packages from a Requirements File

```bash
pip install -r requirements.txt
```

This installs all packages listed in the file.

---

## What is `requirements.txt`?

A `requirements.txt` file stores the names and versions of packages required by a project.

Example:

```text
requests==2.31.0
numpy==2.0.0
pandas==2.2.2
```

It helps other developers install the exact dependencies needed for the project.

---

## Example

Install a package:

```bash
pip install requests
```

Use it in Python:

```python
import requests
```

---

## Advantages of pip

- Easy to use
- Saves development time
- Installs packages in seconds
- Automatically installs required dependencies
- Supports version management
- Makes project setup simple
- Works on Windows, Linux, and macOS

---

## Limitations

- Requires an internet connection to install packages (unless using local files).
- Installing incompatible versions may cause dependency conflicts.
- Some packages require additional system libraries.

---

## Best Practices

- Keep pip updated.
- Use virtual environments for projects.
- Store dependencies in `requirements.txt`.
- Install only the packages your project needs.
- Regularly update packages to receive bug fixes and security improvements.

---

## Built-in Modules vs Third-party Packages

| Built-in Modules | Third-party Packages |
|------------------|----------------------|
| Come with Python | Installed using pip |
| No installation required | Must be downloaded |
| Examples: `math`, `os`, `random` | Examples: `numpy`, `pandas`, `requests` |
| Available immediately | Available after installation |

---

## Summary

- `pip` is Python's package manager.
- It is used to install, update, and remove third-party packages.
- Packages are downloaded from the Python Package Index (PyPI).
- `requirements.txt` helps share project dependencies.
- pip is an essential tool for Python development and is widely used in almost every Python project.
