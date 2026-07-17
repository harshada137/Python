# File Modes in Python

## Introduction

File modes determine how a file is opened. They define whether the file will be read, written, appended, or opened in binary mode.

## Common File Modes

| Mode | Description |
|------|-------------|
| `r` | Read mode (Default). Error if file doesn't exist. |
| `w` | Write mode. Creates a new file or overwrites existing content. |
| `a` | Append mode. Adds data to the end of the file. |
| `x` | Creates a new file. Error if file already exists. |
| `r+` | Read and write mode. |
| `w+` | Read and write. Overwrites existing content. |
| `a+` | Read and append mode. |
| `rb` | Read binary files. |
| `wb` | Write binary files. |
| `ab` | Append binary files. |

## Syntax

```python
file = open("example.txt", "r")
```

## Example

```python
file = open("notes.txt", "w")
file.write("Python File Handling")
file.close()
```

## Key Points

- Always choose the correct mode.
- `w` removes existing content.
- `a` preserves existing data.
- Binary modes are mainly used for images, videos, PDFs, etc.
