# Pandas String Methods (`str`)

This repository contains notes and examples for working with **string data in Pandas Series**. The focus is on using the `.str` accessor to apply string operations efficiently on entire Series objects.

## Table of Contents

- [Pandas String Methods (`str`)](#pandas-string-methods-str)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Commonly Used String Methods](#commonly-used-string-methods)
  - [Working with Series String Data](#working-with-series-string-data)
  - [Function Reference Table](#function-reference-table)
  - [Regex with String Methods](#regex-with-string-methods)
  - [Using `apply()` with Custom Functions](#using-apply-with-custom-functions)
  - [References](#references)

---

## Overview

Pandas provides vectorized string functions through the `.str` accessor, which allows you to perform operations on each element in a string Series without using loops. These functions are similar to Python’s built-in string methods but designed for performance and ease of use with pandas.

---

## Commonly Used String Methods

Here are some commonly used `.str` functions:

* `.lower()`, `.upper()`, `.title()`, `.capitalize()`: Change case
* `.strip()`, `.lstrip()`, `.rstrip()`: Remove whitespace
* `.replace()`: Replace substrings
* `.startswith()`, `.endswith()`: Check string boundaries
* `.contains()`: Check if a pattern exists in each string
* `.isdigit()`, `.isalpha()`: Check character type
* `.len()`: String length
* `.split()`, `.get()`, `.join()`: Working with substrings
* `.extract()`, `.findall()`: Use with regular expressions

---

## Working with Series String Data

```python
import pandas as pd

data = pd.Series(["  Hello World ", "Pandas is POWERFUL", "123abc", "  data Science "])

# Lowercase
data.str.lower()

# Strip whitespace
data.str.strip()

# Replace
data.str.replace(" ", "_")

# Check if starts with "p"
data.str.lower().str.startswith("p")

# Check for digits
data.str.isdigit()
```

---

## Function Reference Table

| Function                | Description                                     | Example                         |
| ----------------------- | ----------------------------------------------- | ------------------------------- |
| `.str.lower()`          | Converts to lowercase                           | `series.str.lower()`            |
| `.str.upper()`          | Converts to uppercase                           | `series.str.upper()`            |
| `.str.title()`          | Capitalizes each word                           | `series.str.title()`            |
| `.str.strip()`          | Removes leading/trailing whitespace             | `series.str.strip()`            |
| `.str.replace(a, b)`    | Replaces substring `a` with `b`                 | `series.str.replace(" ", "_")`  |
| `.str.startswith(x)`    | Checks if string starts with `x`                | `series.str.startswith("a")`    |
| `.str.endswith(x)`      | Checks if string ends with `x`                  | `series.str.endswith(".com")`   |
| `.str.contains(x)`      | Checks if `x` is in the string (supports regex) | `series.str.contains("data")`   |
| `.str.isdigit()`        | Checks if string is numeric                     | `series.str.isdigit()`          |
| `.str.isalpha()`        | Checks if all characters are alphabetic         | `series.str.isalpha()`          |
| `.str.len()`            | Returns string length                           | `series.str.len()`              |
| `.str.extract(pattern)` | Extracts using regex group                      | `series.str.extract(r"(\d+)")`  |
| `.str.findall(pattern)` | Finds all regex matches                         | `series.str.findall(r"\d+")`    |
| `.str.split()`          | Splits string by delimiter                      | `series.str.split(" ")`         |
| `.str.get(n)`           | Gets element at position `n` after split        | `series.str.split().str.get(0)` |

---

## Regex with String Methods

Many string methods support regular expressions for advanced pattern matching:

```python
series = pd.Series(["email123@gmail.com", "hello@domain.net", "no_email"])

# Extract username
series.str.extract(r"(^[\w]+)")

# Check if string contains '@'
series.str.contains(r"@", regex=True)
```

---

## Using `apply()` with Custom Functions

If built-in methods don’t cover a specific use case, you can use `.apply()` with custom functions:

```python
def custom_function(x):
    return x[::-1]  # Reverse the string

series.apply(custom_function)
```

Or with `lambda`:

```python
series.apply(lambda x: x.upper() if isinstance(x, str) else x)
```

---

## References

* [Pandas String Methods Documentation](https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html)
* [String Handling with `.str`](https://pandas.pydata.org/pandas-docs/stable/reference/series.html#string-handling)
* [Python Regular Expressions](https://docs.python.org/3/library/re.html)

---

* Thank you to My Dear Nitish Sir 🙏💝 [CampusX](https://www.youtube.com/playlist?list=PLKnIA16_RmvbAlyx4_rdtR66B7EHX5k3z)


<!-- Typing -->
<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=30&duration=6000&pause=1000&color=5E17EB&center=true&vCenter=true&width=435&lines=Rudra+Prasad+Bhuyan;Data+Lover;Data+Science+Enthusiast" alt="Typing Effect" />
</p>

<!-- Social Media Links-->
<p align="center">
  <a href="https://github.com/Rudra-G-23">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Badge"/>
  </a>
  <a href="https://www.linkedin.com/in/rudra-prasad-bhuyan-44a388235">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Badge"/>
  </a>
  <a href="https://www.kaggle.com/rudraprasadbhuyan">
    <img src="https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white" alt="Kaggle Badge"/>
  </a>
</p>

<!-- Two My favorite Repo Links -->
<p align="center">
  <a href="https://github.com/Rudra-G-23/Data-Science-Roadmap">
    <img src="https://img.shields.io/badge/Data_Science_My_journey -Explore-red?style=for-the-badge" alt="Data Science Roadmap Badge"/>
  </a>
  <a href="https://github.com/Rudra-G-23/Data-Science-Projects-Portflio">
    <img src="https://img.shields.io/badge/Data_Science_Projects-View-green?style=for-the-badge" alt="Data Science Projects Badge"/>
  </a>
</p>

---
