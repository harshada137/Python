# Web Scraping (Basics) in Python

## Introduction

Web scraping is the process of extracting information from websites automatically.

Python provides libraries such as **BeautifulSoup** and **Requests** to retrieve and parse web pages.

Web scraping is commonly used for data collection, research, and monitoring websites.

---

## Basic Process

1. Send a request to a webpage.
2. Receive the HTML content.
3. Parse the HTML.
4. Extract the required information.

---

## Example

```python
import requests

response = requests.get("https://example.com")

print(response.status_code)
```

**Output**

```
200
```

---

## Common Libraries

- requests
- BeautifulSoup
- lxml
- Selenium (for dynamic websites)

---

## Advantages

- Automated data collection.
- Saves time.
- Useful for market research and analytics.

---

## Key Points

- Always respect a website's terms of service and robots.txt.
- BeautifulSoup is commonly used for parsing HTML.
- Selenium is preferred for websites that use JavaScript heavily.
