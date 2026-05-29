# Combining DataFrames with `pd.concat`, `append`, and MultiIndex Handling in Pandas

This repository covers how to **combine, append, and join DataFrames** using `pandas`. You'll learn how to use `pd.concat()` and `DataFrame.append()` effectively, handle MultiIndex, and access joined data with practical examples and exercises.

---

## Table of Contents

- [Combining DataFrames with `pd.concat`, `append`, and MultiIndex Handling in Pandas](#combining-dataframes-with-pdconcat-append-and-multiindex-handling-in-pandas)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Import Libraries and Dataset](#import-libraries-and-dataset)
  - [Combining DataFrames](#combining-dataframes)
    - [Using `pd.concat()`](#using-pdconcat)
    - [Using `df.append()`](#using-dfappend)
    - [Horizontal Concatenation](#horizontal-concatenation)
    - [Using `ignore_index`](#using-ignore_index)
  - [Working with MultiIndex](#working-with-multiindex)
    - [Creating MultiIndex DataFrame](#creating-multiindex-dataframe)
    - [Accessing with `iloc`](#accessing-with-iloc)
  - [Join Methods in Concatenation](#join-methods-in-concatenation)
    - [Inner Join](#inner-join)
    - [Outer Join](#outer-join)
    - [Right Join (not directly in concat, use merge)](#right-join-not-directly-in-concat-use-merge)
  - [Real-World Practice Questions](#real-world-practice-questions)
  - [Function Reference Table](#function-reference-table)
  - [Official Documentation](#official-documentation)

---

## Introduction

Combining DataFrames is a key step in many data analysis workflows. This guide focuses on:

* Vertical and horizontal concatenation
* Appending rows
* Managing indices
* Handling hierarchical (MultiIndex) structures
* Using different join strategies during concatenation

---

## Import Libraries and Dataset

Start with importing pandas and loading your datasets.

```python
import pandas as pd

# Example: loading multiple small DataFrames
df1 = pd.DataFrame(...)
df2 = pd.DataFrame(...)
```

---

## Combining DataFrames

### Using `pd.concat()`

Used to concatenate DataFrames **vertically (row-wise)** or **horizontally (column-wise)**.

```python
pd.concat([df1, df2])
pd.concat([df1, df2], axis=1)
```

### Using `df.append()`

Simple way to append rows (Note: deprecated since pandas 1.4.0).

```python
df1.append(df2)  # Not recommended in new code
```

### Horizontal Concatenation

Combining columns:

```python
pd.concat([df1, df2], axis=1)
```

### Using `ignore_index`

Reset the index after concatenation:

```python
pd.concat([df1, df2], ignore_index=True)
```

---

## Working with MultiIndex

### Creating MultiIndex DataFrame

```python
arrays = [
    ['A', 'A', 'B', 'B'],
    [1, 2, 1, 2]
]
index = pd.MultiIndex.from_arrays(arrays, names=('Group', 'Subgroup'))
df = pd.DataFrame({'data': [10, 20, 30, 40]}, index=index)
```

### Accessing with `iloc`

Use `iloc` to access rows by position:

```python
df.iloc[0]     # First row
df.iloc[1:3]   # Slice rows
```

---

## Join Methods in Concatenation

### Inner Join

Keeps only common columns or indices.

```python
pd.concat([df1, df2], join='inner')
```

### Outer Join

Includes all columns or indices, fills missing values with NaN.

```python
pd.concat([df1, df2], join='outer')
```

### Right Join (not directly in concat, use merge)

For `concat()`, right join is not directly supported; use `merge()` for more control.

---

## Real-World Practice Questions

Practice using datasets like employee records, sales logs, and customer tables.

Examples:

* Combine monthly sales reports into one DataFrame
* Append new product data to an existing inventory list
* Merge customer and order data side-by-side
* Create a MultiIndex to summarize sales by region and month
* Compare inner vs outer join results when columns differ

---

## Function Reference Table

| Function / Parameter        | Purpose                     | Example                             |
| --------------------------- | --------------------------- | ----------------------------------- |
| `pd.concat()`               | Combine along axis          | `pd.concat([df1, df2])`             |
| `df.append()`               | Append rows (deprecated)    | `df1.append(df2)`                   |
| `ignore_index=True`         | Reset index during concat   | `pd.concat(..., ignore_index=True)` |
| `axis=1`                    | Combine columns             | `pd.concat(..., axis=1)`            |
| `join='inner'`              | Inner join on columns/index | `pd.concat(..., join='inner')`      |
| `join='outer'`              | Outer join (default)        | `pd.concat(..., join='outer')`      |
| `pd.MultiIndex.from_arrays` | Create multi-level index    | See example above                   |
| `df.iloc[]`                 | Positional access           | `df.iloc[0]`                        |

---

## Official Documentation

* [pandas.concat()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html)
* [pandas MultiIndex](https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html#hierarchical-indexing-multiindex)
* [Appending and Joining DataFrames](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html)

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
