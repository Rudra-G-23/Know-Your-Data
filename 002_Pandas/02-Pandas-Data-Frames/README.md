# Pandas DataFrame

This repository contains notes and examples related to working with **Pandas DataFrames** in Python. It covers how to create DataFrames, explore their attributes and methods, perform mathematical operations, and manipulate or filter data.

These notes are written in a way that helps anyone who is learning Pandas understand what each section or code file does.

---

## Table of Contents

- [Pandas DataFrame](#pandas-dataframe)
  - [Table of Contents](#table-of-contents)
  - [1. Creating DataFrames](#1-creating-dataframes)
    - [Using Lists](#using-lists)
    - [Using Dictionary](#using-dictionary)
    - [Using CSV Files](#using-csv-files)
  - [2. DataFrame Attributes \& Methods](#2-dataframe-attributes--methods)
  - [3. Mathematical Operations](#3-mathematical-operations)
  - [4. Selecting, Filtering \& Editing](#4-selecting-filtering--editing)
    - [Filtering a DataFrame](#filtering-a-dataframe)
    - [Adding a New Column](#adding-a-new-column)
  - [5. Function Reference Table](#5-function-reference-table)
  - [6. References](#6-references)
- [7. Connect with me](#7-connect-with-me)

---

## 1. Creating DataFrames

### Using Lists

Creating a DataFrame by passing nested lists.

### Using Dictionary

Creating a DataFrame using a dictionary where keys are column names.

### Using CSV Files

Loading a DataFrame from a CSV file using `pd.read_csv()`.

---

## 2. DataFrame Attributes & Methods

* `.shape` – Returns the number of rows and columns
* `.dtypes` – Displays the data types of columns
* `.index` – Returns the index (row labels)
* `.columns` – Returns the column labels
* `.values` – Returns the underlying data as a NumPy array
* `.head(n)` – Returns the first n rows
* `.tail(n)` – Returns the last n rows
* `.sample(n)` – Returns n random rows
* `.info()` – Summary including data types and memory usage
* `.describe()` – Summary statistics of numeric columns
* `.isnull()` – Detect missing values
* `.duplicated()` – Detect duplicate rows
* `.rename()` – Rename column or index labels

---

## 3. Mathematical Operations

* `.sum()` – Column-wise sum
* `.mean()` – Column-wise mean
* `.var()` – Column-wise variance

---

## 4. Selecting, Filtering & Editing

* `df.iloc[]` – Select by **index position** (rows/columns)

* `df.loc[]` – Select by **label** (row/column names)

* Select both row and column together:
  Example: `df.loc[1, 'column_name']` or `df.iloc[1, 2]`

* **Fancy Indexing** – Use a list or array to select specific rows or columns
  Example: `df.iloc[[0, 2, 4]]`

### Filtering a DataFrame

Apply conditions to filter rows:
Example: `df[df['column'] > 50]`

### Adding a New Column

Use assignment:
Example: `df['new_column'] = df['existing_column'] * 2`

---

## 5. Function Reference Table

| Function         | Purpose                             | Example                         |
| ---------------- | ----------------------------------- | ------------------------------- |
| `pd.DataFrame()` | Create a DataFrame                  | `pd.DataFrame(data)`            |
| `.shape`         | Get shape of DataFrame              | `df.shape`                      |
| `.dtypes`        | Get data types of each column       | `df.dtypes`                     |
| `.head(n)`       | Show first n rows                   | `df.head(5)`                    |
| `.tail(n)`       | Show last n rows                    | `df.tail(5)`                    |
| `.sample(n)`     | Randomly sample n rows              | `df.sample(3)`                  |
| `.info()`        | Summary of DataFrame                | `df.info()`                     |
| `.describe()`    | Summary stats for numerical columns | `df.describe()`                 |
| `.iloc[]`        | Select by position                  | `df.iloc[0, 1]`                 |
| `.loc[]`         | Select by label                     | `df.loc[0, 'column_name']`      |
| `.isnull()`      | Check for null values               | `df.isnull().sum()`             |
| `.duplicated()`  | Find duplicate rows                 | `df.duplicated()`               |
| `.rename()`      | Rename labels                       | `df.rename(columns={'A': 'B'})` |
| `.sum()`         | Column-wise sum                     | `df.sum()`                      |
| `.mean()`        | Column-wise mean                    | `df.mean()`                     |
| `.var()`         | Column-wise variance                | `df.var()`                      |


---

## 6. References
* Thank you to My Dear Nitish Sir 🙏💝 [CampusX](https://www.youtube.com/playlist?list=PLKnIA16_RmvbAlyx4_rdtR66B7EHX5k3z)
* [Pandas Official Documentation](https://pandas.pydata.org/docs/)
* [Pandas API Reference](https://pandas.pydata.org/docs/reference/index.html)

---
# 7. Connect with me  

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