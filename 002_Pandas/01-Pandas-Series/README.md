# 📘 Pandas Series - Quick Reference Guide

A concise guide to working with **Pandas Series**, including creation, methods, math operations, indexing, and more.

---

## 1. Table of Contents

- [📘 Pandas Series - Quick Reference Guide](#-pandas-series---quick-reference-guide)
  - [1. Table of Contents](#1-table-of-contents)
  - [2. What is Pandas](#2-what-is-pandas)
    - [2.1 Pandas Series](#21-pandas-series)
    - [2.2 Importing Pandas](#22-importing-pandas)
  - [3. Creating a Series Methods](#3-creating-a-series-methods)
    - [3.1 Series from Lists](#31-series-from-lists)
    - [3.2 Series from Dict](#32-series-from-dict)
    - [3.3 Series Attributes](#33-series-attributes)
    - [3.4 Series using read\_csv](#34-series-using-read_csv)
  - [4. Series Methods](#4-series-methods)
    - [4.1 head() \& tail()](#41-head--tail)
    - [4.2 sample()](#42-sample)
    - [4.3 value\_counts()](#43-value_counts)
    - [4.4 sort\_values()](#44-sort_values)
    - [4.5 sort\_index()](#45-sort_index)
  - [5. Series Math Methods](#5-series-math-methods)
    - [5.1 count](#51-count)
    - [5.2 product() \& sum()](#52-product--sum)
    - [5.3 mean / median / std / mode / var](#53-mean--median--std--mode--var)
    - [5.4 describe()](#54-describe)
  - [6. Series Indexing \& Slicing](#6-series-indexing--slicing)
    - [6.1 Normal Indexing](#61-normal-indexing)
    - [6.2 Negative Indexing](#62-negative-indexing)
    - [6.3 Fancy Indexing](#63-fancy-indexing)
    - [6.4 Editing Series](#64-editing-series)
    - [6.5 Copy \& Views](#65-copy--views)
  - [7. Series with Python Functionalities](#7-series-with-python-functionalities)
    - [7.1 len / type / dir / sorted](#71-len--type--dir--sorted)
    - [7.2 Type Conversion](#72-type-conversion)
    - [7.3 Membership Operator](#73-membership-operator)
    - [7.4 Looping](#74-looping)
    - [7.5 Broadcasting](#75-broadcasting)
    - [7.6 Relational](#76-relational)
    - [7.7 Boolean Indexing on Series](#77-boolean-indexing-on-series)
    - [7.8 Plotting Graphs on Series](#78-plotting-graphs-on-series)
  - [8. Important Series Methods](#8-important-series-methods)
    - [8.1 astype](#81-astype)
    - [8.2 between](#82-between)
    - [8.3 clip](#83-clip)
    - [8.4 drop\_duplicates](#84-drop_duplicates)
    - [8.5 duplicated](#85-duplicated)
    - [8.6 count](#86-count)
    - [8.7 isin](#87-isin)
    - [8.8 fillna](#88-fillna)
    - [8.9 dropna](#89-dropna)
    - [8.10 apply \& lambda](#810-apply--lambda)
    - [8.11 copy](#811-copy)
- [9. Function Reference Table](#9-function-reference-table)
- [10. Thank you 💝](#10-thank-you-)

---

## 2. What is Pandas

### 2.1 Pandas Series

Pandas Series is a one-dimensional labeled array capable of holding any data type.

### 2.2 Importing Pandas

```python
import pandas as pd
```

---

## 3. Creating a Series Methods

### 3.1 Series from Lists

```python
pd.Series([1, 2, 3])
```

### 3.2 Series from Dict

```python
pd.Series({'a': 1, 'b': 2})
```

### 3.3 Series Attributes

```python
s.index
s.values
s.dtype
s.size
```

### 3.4 Series using read\_csv

```python
pd.read_csv('file.csv')['column_name']
```

---

## 4. Series Methods

### 4.1 head() & tail()

```python
s.head()
s.tail()
```

### 4.2 sample()

```python
s.sample(3)
```

### 4.3 value\_counts()

```python
s.value_counts()
```

### 4.4 sort\_values()

```python
s.sort_values()
```

### 4.5 sort\_index()

```python
s.sort_index()
```

---

## 5. Series Math Methods

### 5.1 count

```python
s.count()
```

### 5.2 product() & sum()

```python
s.product()
s.sum()
```

### 5.3 mean / median / std / mode / var

```python
s.mean()
s.median()
s.std()
s.mode()
s.var()
```

### 5.4 describe()

```python
s.describe()
```

---

## 6. Series Indexing & Slicing

### 6.1 Normal Indexing

```python
s[2]
```

### 6.2 Negative Indexing

```python
s[-1]
```

### 6.3 Fancy Indexing

```python
s[[1, 3, 5]]
```

### 6.4 Editing Series

```python
s[1] = 100
```

### 6.5 Copy & Views

```python
copy = s.copy()
```

---

## 7. Series with Python Functionalities

### 7.1 len / type / dir / sorted

```python
len(s)
type(s)
dir(s)
sorted(s)
```

### 7.2 Type Conversion

```python
s.astype(int)
```

### 7.3 Membership Operator

```python
10 in s.values
```

### 7.4 Looping

```python
for val in s:
    print(val)
```

### 7.5 Broadcasting

```python
s + 10
```

### 7.6 Relational

```python
s > 5
```

### 7.7 Boolean Indexing on Series

```python
s[s > 5]
```

### 7.8 Plotting Graphs on Series

```python
s.plot()
```

---

## 8. Important Series Methods

### 8.1 astype

```python
s.astype(float)
```

### 8.2 between

```python
s[s.between(10, 20)]
```

### 8.3 clip

```python
s.clip(lower=5, upper=15)
```

### 8.4 drop\_duplicates

```python
s.drop_duplicates()
```

### 8.5 duplicated

```python
s.duplicated()
```

### 8.6 count

```python
s.count()
```

### 8.7 isin

```python
s.isin([1, 2, 3])
```

### 8.8 fillna

```python
s.fillna(0)
```

### 8.9 dropna

```python
s.dropna()
```

### 8.10 apply & lambda

```python
s.apply(lambda x: x * 2)
```

### 8.11 copy

```python
s_copy = s.copy()
```

---

# 9. Function Reference Table

| Function            | Description                               | Documentation Link                                                                                    |
| ------------------- | ----------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `head()`            | Returns the first n rows                  | [link](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.head.html)            |
| `tail()`            | Returns the last n rows                   | [link](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.tail.html)            |
| `sample()`          | Returns random items                      | [link](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.sample.html)          |
| `value_counts()`    | Returns counts of unique values           | [link](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.value_counts.html)    |
| `sort_values()`     | Sorts the series by values                | [link](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.sort_values.html)     |
| `sort_index()`      | Sorts the series by index                 | [link](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.sort_index.html)      |
| `count()`           | Number of non-NA/null observations        | [link](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.count.html)           |
| `product()`         | Product of values                         | [link](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.prod.html)            |
| `sum()`             | Sum of values                             | [link](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.sum.html)             |
| `mean()`            | Mean of values                            | [link](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.mean.html)            |
| `median()`          | Median of values                          | [link](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.median.html)          |
| `std()`             | Standard deviation                        | [link](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.std.html)             |
| `mode()`            | Mode of values                            | [link](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.mode.html)            |
| `var()`             | Variance of values                        | [link](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.var.html)             |
| `describe()`        | Summary statistics                        | [link](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.describe.html)        |
| `astype()`          | Cast Series to specified dtype            | [link](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.astype.html)          |
| `between()`         | Check if values between two numbers       | [link](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.between.html)         |
| `clip()`            | Trim values at specified input thresholds | [link](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.clip.html)            |
| `drop_duplicates()` | Remove duplicate values                   | [link](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.drop_duplicates.html) |
| `duplicated()`      | Mark duplicate rows                       | [link](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.duplicated.html)      |
| `isin()`            | Check whether elements are in values      | [link](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.isin.html)            |
| `fillna()`          | Fill NA/NaN values                        | [link](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.fillna.html)          |
| `dropna()`          | Remove missing values                     | [link](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.dropna.html)          |
| `apply()`           | Apply a function element-wise             | [link](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.apply.html)           |
| `copy()`            | Make a copy of the Series                 | [link](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.copy.html)            |


---

# 10. Thank you 💝
Thank you to My Dear Nitish Sir 🙏 [CampusX](https://www.youtube.com/playlist?list=PLKnIA16_RmvbAlyx4_rdtR66B7EHX5k3z)

---

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=30&duration=6000&pause=1000&color=5E17EB&center=true&vCenter=true&width=435&lines=Rudra+Prasad+Bhuyan;Data+Lover;Data+Science+Enthusiast" alt="Typing Effect" />
</p>


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

<p align="center">
  <a href="https://github.com/Rudra-G-23/Data-Science-Roadmap">
    <img src="https://img.shields.io/badge/Data_Science_My_journey -Explore-red?style=for-the-badge" alt="Data Science Roadmap Badge"/>
  </a>
  <a href="https://github.com/Rudra-G-23/data-science-projects">
    <img src="https://img.shields.io/badge/Data_Science_Projects-View-green?style=for-the-badge" alt="Data Science Projects Badge"/>
  </a>
</p>

---