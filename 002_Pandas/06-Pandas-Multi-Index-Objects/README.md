# Understanding MultiIndex Objects in Pandas

This repository explains how to **create, manipulate, and use MultiIndex objects** in pandas. MultiIndex enables handling and analyzing **multi-dimensional data** in a clean and structured way using hierarchical indexing. This guide covers key functions, concepts, and real-world use cases.

---

## Table of Contents

- [Understanding MultiIndex Objects in Pandas](#understanding-multiindex-objects-in-pandas)
  - [Table of Contents](#table-of-contents)
  - [Introduction to Indexing](#introduction-to-indexing)
  - [Creating MultiIndex](#creating-multiindex)
    - [From Tuples](#from-tuples)
    - [From Product](#from-product)
    - [From Series or DataFrame](#from-series-or-dataframe)
  - [Working with MultiIndex DataFrames](#working-with-multiindex-dataframes)
    - [Selecting Data](#selecting-data)
    - [Sorting Index](#sorting-index)
    - [Swapping Levels](#swapping-levels)
  - [MultiIndex from Columns](#multiindex-from-columns)
  - [Reshaping MultiIndex DataFrames](#reshaping-multiindex-dataframes)
    - [Stack and Unstack](#stack-and-unstack)
    - [Long vs Wide Data with `melt`](#long-vs-wide-data-with-melt)
  - [Pivot Tables and Aggregations](#pivot-tables-and-aggregations)
  - [Multi-Dimensional Data and Plotting](#multi-dimensional-data-and-plotting)
  - [Function Reference Table](#function-reference-table)
  - [Official Documentation](#official-documentation)

---

## Introduction to Indexing

The **index** in pandas uniquely identifies each row. A **MultiIndex** (also called a hierarchical index) allows multiple levels of indexing, giving pandas the ability to handle higher-dimensional data in a 2D DataFrame.

---

## Creating MultiIndex

### From Tuples

```python
index = pd.MultiIndex.from_tuples([('A', 1), ('A', 2), ('B', 1)])
```

### From Product

```python
index = pd.MultiIndex.from_product([['A', 'B'], [1, 2]])
```

### From Series or DataFrame

If a DataFrame has multiple index-like columns:

```python
df.set_index(['col1', 'col2'], inplace=True)
```

---

## Working with MultiIndex DataFrames

### Selecting Data

* Access rows using `.loc` with tuples:

```python
df.loc[('A', 1)]
```

* Slicing:

```python
df.loc['A']
df.loc[('A', slice(None))]
```

### Sorting Index

```python
df.sort_index(level=0)
```

### Swapping Levels

```python
df.swaplevel(0, 1)
```

---

## MultiIndex from Columns

Columns can also have multiple levels of headers:

```python
df.columns = pd.MultiIndex.from_tuples([('Sales', 'Q1'), ('Sales', 'Q2')])
```

Useful for summarizing grouped statistics or pivoted tables.

---

## Reshaping MultiIndex DataFrames

### Stack and Unstack

* Convert columns into rows (`stack`) and vice versa (`unstack`):

```python
df.stack()
df.unstack()
```

This is how MultiIndex allows reshaping data without losing structure.

### Long vs Wide Data with `melt`

* Use `melt()` to transform wide-format data to long format:

```python
pd.melt(df, id_vars=["id"], var_name="variable", value_name="value")
```

Great for preparing data for analysis or visualization.

---

## Pivot Tables and Aggregations

* Use `pivot_table()` with aggregation functions for grouped summaries:

```python
df.pivot_table(index=['A'], columns=['B'], values='C', aggfunc='sum')
```

You can build multi-dimensional pivot tables with multiple index/column levels.

---

## Multi-Dimensional Data and Plotting

* After organizing data with MultiIndex, use `.groupby().plot()` or pivoted data to generate layered charts.

```python
df.groupby(['region', 'year'])['sales'].sum().unstack().plot(kind='bar')
```

---

## Function Reference Table

| Function / Attribute         | Description                              | Example                                 |
| ---------------------------- | ---------------------------------------- | --------------------------------------- |
| `pd.MultiIndex.from_tuples`  | Create index from list of tuples         | `pd.MultiIndex.from_tuples([('A', 1)])` |
| `pd.MultiIndex.from_product` | Cartesian product of iterables for index | `pd.MultiIndex.from_product(...)`       |
| `df.set_index()`             | Set multiple columns as index            | `df.set_index(['col1', 'col2'])`        |
| `.loc[]`                     | Access rows by tuple index               | `df.loc[('A', 1)]`                      |
| `.sort_index()`              | Sort by index levels                     | `df.sort_index(level=1)`                |
| `.swaplevel()`               | Swap index levels                        | `df.swaplevel(0, 1)`                    |
| `.stack()` / `.unstack()`    | Reshape data by index ↔ columns          | `df.stack()`                            |
| `pd.melt()`                  | Convert wide → long format               | `pd.melt(df, ...)`                      |
| `.pivot_table()`             | Create summarized tables                 | `df.pivot_table(...)`                   |

---

## Official Documentation

* [MultiIndex / Advanced Indexing](https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html#multiindex-advanced-indexing)
* [Indexing and Selecting Data](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html)
* [Reshaping with Stack/Unstack](https://pandas.pydata.org/pandas-docs/stable/user_guide/reshaping.html#reshaping-by-stacking-and-unstacking)
* [Pivot Tables](https://pandas.pydata.org/pandas-docs/stable/user_guide/reshaping.html#pivot-tables)
* [Melt Function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.melt.html)

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
