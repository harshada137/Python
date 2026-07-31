# API Handling in Python

## Introduction

An API (Application Programming Interface) allows different applications to communicate with each other.

Python commonly uses the `requests` library to send HTTP requests and receive responses from APIs.

Most modern applications, cloud platforms, and web services expose APIs for developers.

---

## Common HTTP Methods

- GET – Retrieve data
- POST – Send data
- PUT – Update data
- DELETE – Remove data

---

## Example

```python
import requests

response = requests.get("https://api.github.com")

print(response.status_code)
```

**Output**

```
200
```

---

## Applications

- Access weather APIs
- AWS automation
- GitHub API
- Payment gateways
- AI APIs
- REST services

---

## Key Points

- The `requests` library is widely used.
- APIs usually exchange data in JSON format.
- API handling is essential for automation and cloud development.
