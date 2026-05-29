# Pandas DateTime Notes

This repository contains notes and examples related to handling date and time data using the `pandas` library in Python. It covers common DateTime objects, accessor methods, and functions provided by pandas to manipulate and analyze time-related data efficiently.

## Table of Contents

- [Pandas DateTime Notes](#pandas-datetime-notes)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Fetching DateTime Attributes](#fetching-datetime-attributes)
  - [Key DateTime Objects](#key-datetime-objects)
    - [Timestamp Object](#timestamp-object)
    - [DatetimeIndex Object](#datetimeindex-object)
  - [DateTime Functions](#datetime-functions)
    - [`pd.to_datetime()`](#pdto_datetime)
    - [`pd.date_range()`](#pddate_range)
  - [dt Accessor](#dt-accessor)
  - [Function Reference Table](#function-reference-table)
  - [References](#references)

---

## Overview

Working with dates and times is a common task in data analysis. Pandas provides built-in support for:

* Converting strings or numerical data to DateTime format.
* Extracting parts like year, month, day, etc.
* Creating and manipulating ranges of time.
* Vectorized operations on datetime-like series using the `.dt` accessor.

---

## Fetching DateTime Attributes

Once a datetime object is created, you can extract various components:

```python
import pandas as pd

dt = pd.to_datetime("2023-06-14 15:45:00")

# Accessing attributes
dt.year      # 2023
dt.month     # 6
dt.day       # 14
dt.hour      # 15
dt.minute    # 45
dt.second    # 0
```

---

## Key DateTime Objects

### Timestamp Object

A single point in time.

```python
ts = pd.Timestamp("2024-05-01 13:20:00")
```

* Represents a specific moment.
* Can access individual time units (`ts.year`, `ts.hour`, etc).

### DatetimeIndex Object

Used for indexing time series data.

```python
idx = pd.to_datetime(["2023-01-01", "2023-01-02"])
```

* Efficient indexing and slicing by date/time.
* Useful for time series datasets.

---

## DateTime Functions

### `pd.to_datetime()`

Converts various inputs (like strings or lists) to `datetime64` type.

```python
pd.to_datetime("2023-06-14")
pd.to_datetime(["2023-06-14", "2023-07-01"])
```

### `pd.date_range()`

Creates a range of dates with specified frequency.

```python
pd.date_range(start="2023-01-01", end="2023-01-07", freq="D")
```

Useful `freq` options:

* `"D"`: Day
* `"H"`: Hour
* `"M"`: Month-end
* `"MS"`: Month-start

---

## dt Accessor

Allows vectorized operations on series of datetime objects.

```python
dates = pd.to_datetime(["2023-06-14", "2024-01-01"])
series = pd.Series(dates)

series.dt.year     # [2023, 2024]
series.dt.month    # [6, 1]
series.dt.day_name()  # ['Wednesday', 'Monday']
```

---

## Function Reference Table

| Function or Attribute | Description                        | Example                                  |
| --------------------- | ---------------------------------- | ---------------------------------------- |
| `pd.to_datetime()`    | Converts string/list to datetime   | `pd.to_datetime("2023-01-01")`           |
| `pd.date_range()`     | Creates range of dates             | `pd.date_range(start="2023", periods=3)` |
| `Timestamp`           | Represents a single date/time      | `pd.Timestamp("2023-06-14 10:00")`       |
| `DatetimeIndex`       | Index of datetime values           | `pd.to_datetime([...])`                  |
| `.dt.year`            | Extracts year from datetime series | `series.dt.year`                         |
| `.dt.month`           | Extracts month                     | `series.dt.month`                        |
| `.dt.day`             | Extracts day of the month          | `series.dt.day`                          |
| `.dt.hour`            | Extracts hour                      | `series.dt.hour`                         |
| `.dt.minute`          | Extracts minute                    | `series.dt.minute`                       |
| `.dt.second`          | Extracts second                    | `series.dt.second`                       |
| `.dt.day_name()`      | Gets day name                      | `series.dt.day_name()`                   |

---

## References

* [Pandas DateTime Documentation](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html)
* [to\_datetime()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html)
* [date\_range()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.date_range.html)
* [Timestamp](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Timestamp.html)
* [DatetimeIndex](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DatetimeIndex.html)
* [dt accessor](https://pandas.pydata.org/pandas-docs/stable/reference/series.html#datetimelike-properties)

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

