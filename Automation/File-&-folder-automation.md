# File & Folder Automation in Python

## Introduction

Python can automate common file and folder operations, eliminating the need to perform them manually.

Using modules such as `os` and `shutil`, Python can create, copy, move, rename, and delete files or directories.

This is especially useful for backup scripts, log management, and organizing files.

---

## Common Tasks

- Create folders
- Rename files
- Copy files
- Move files
- Delete files
- List directory contents

---

## Example

```python
import os

os.mkdir("Project")
```

This creates a new folder named **Project** in the current directory.

---

## Advantages

- Saves time.
- Reduces manual effort.
- Useful for backup and maintenance scripts.

---

## Key Points

- `os` handles directory operations.
- `shutil` provides advanced file operations like copy and move.
- Frequently used in automation and DevOps.
