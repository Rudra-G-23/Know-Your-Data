
# GroupBy: Attributes and Methods in Pandas

This repository contains practical notes, examples, and exercises focused on **pandas GroupBy objects**. It's designed to help you understand how to group data efficiently and apply various aggregation and transformation operations using core attributes and methods.

---

## Table of Contents

- [GroupBy: Attributes and Methods in Pandas](#groupby-attributes-and-methods-in-pandas)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [GroupBy Basics](#groupby-basics)
    - [Creating GroupBy Objects](#creating-groupby-objects)
    - [Common Use Cases](#common-use-cases)
  - [Core GroupBy Attributes \& Methods](#core-groupby-attributes--methods)
    - [`len()`](#len)
    - [`size()`](#size)
    - [`first()` / `last()`](#first--last)
    - [`nth(n)`](#nthn)
    - [`get_group() vs Filtering`](#get_group-vs-filtering)
    - [`groups`](#groups)
    - [`describe()`](#describe)
    - [`sample()`](#sample)
    - [`nunique()`](#nunique)
  - [GroupBy in Practice](#groupby-in-practice)
    - [Real-world Scenarios](#real-world-scenarios)
    - [Looping over Groups](#looping-over-groups)
  - [Hands-on Exercises](#hands-on-exercises)
    - [Real-World Datasets](#real-world-datasets)
    - [Q\&A Format](#qa-format)
  - [Function Reference Table](#function-reference-table)
  - [Official Documentation](#official-documentation)

---

## Introduction

Grouping data is a powerful and common task when analyzing data. In pandas, `groupby()` allows you to split a DataFrame into groups, apply functions to each group independently, and combine the results. This repository helps you understand both the core logic and practical application of grouping data.

---

## GroupBy Basics

### Creating GroupBy Objects

You can group data using one or more columns:

```python
df.groupby("column_name")
df.groupby(["col1", "col2"])
```

### Common Use Cases

* Summarizing grouped data
* Analyzing patterns per category
* Filtering, transforming, or aggregating data by segment

---

## Core GroupBy Attributes & Methods

### `len()`

Returns the total number of groups created.

```python
len(df.groupby("column"))
```

### `size()`

Returns the number of items in each group.

```python
df.groupby("column").size()
```

### `first()` / `last()`

Returns the first or last row of each group.

```python
df.groupby("column").first()
df.groupby("column").last()
```

### `nth(n)`

Returns the nth row from each group.

```python
df.groupby("column").nth(2)
```

### `get_group() vs Filtering`

Retrieve a single group:

```python
df.groupby("column").get_group("value")
```

Filtering is more flexible, but `get_group()` is more direct for exact matches.

### `groups`

Returns a dictionary mapping group names to row indices.

```python
df.groupby("column").groups
```

### `describe()`

Generates descriptive statistics for each group.

```python
df.groupby("column").describe()
```

### `sample()`

Samples random rows from each group.

```python
df.groupby("column").sample(n=1)
```

### `nunique()`

Counts unique values per group.

```python
df.groupby("column").nunique()
```

---

## GroupBy in Practice

### Real-world Scenarios

* Analyzing customer behavior by region
* Summarizing sales by product category
* Measuring engagement metrics by user segments

### Looping over Groups

Iterate through grouped data:

```python
for name, group in df.groupby("column"):
    print(name)
    print(group.head())
```

---

## Hands-on Exercises

### Real-World Datasets

Includes practice on:

* E-commerce orders
* Employee data
* Survey results

### Q\&A Format

Each exercise is structured as a question (e.g., "Find the average salary by department") followed by the code and explanation.

---

## Function Reference Table

| Function / Attribute | Description              | Example                                |
| -------------------- | ------------------------ | -------------------------------------- |
| `len()`              | Number of groups         | `len(df.groupby("col"))`               |
| `size()`             | Size of each group       | `df.groupby("col").size()`             |
| `first()` / `last()` | First/last row per group | `df.groupby("col").first()`            |
| `nth(n)`             | nth item per group       | `df.groupby("col").nth(2)`             |
| `get_group()`        | Access group directly    | `df.groupby("col").get_group("value")` |
| `groups`             | Group name → indices     | `df.groupby("col").groups`             |
| `describe()`         | Descriptive stats        | `df.groupby("col").describe()`         |
| `sample()`           | Random sample            | `df.groupby("col").sample(n=1)`        |
| `nunique()`          | Unique counts            | `df.groupby("col").nunique()`          |

---

## Official Documentation

For deeper understanding, refer to:

* [pandas GroupBy Documentation](https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html)
* [pandas API Reference](https://pandas.pydata.org/pandas-docs/stable/reference/groupby.html)
---


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

