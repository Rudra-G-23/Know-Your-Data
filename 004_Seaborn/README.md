# Seaborn Roadmap

This repository contains categorized notes and examples for **Seaborn**, a Python data visualization library built on top of Matplotlib. It focuses on statistical plots and works well with pandas DataFrames.

---

## Table of Contents

- [Seaborn Roadmap](#seaborn-roadmap)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Types of Functions](#types-of-functions)
  - [Main Plot Categories](#main-plot-categories)
    - [1. Relational Plots](#1-relational-plots)
    - [2. Categorical Plots](#2-categorical-plots)
      - [Categorical Scatter Plots](#categorical-scatter-plots)
      - [Categorical Distribution Plots](#categorical-distribution-plots)
      - [Categorical Estimate Plots (show central tendency)](#categorical-estimate-plots-show-central-tendency)
    - [3. Distribution Plots](#3-distribution-plots)
    - [4. Regression Plots](#4-regression-plots)
    - [5. Matrix Plots](#5-matrix-plots)
    - [6. Multiplots](#6-multiplots)
  - [Function Reference Table](#function-reference-table)
  - [References](#references)

---

## Overview

Seaborn provides a high-level interface for drawing attractive and informative statistical graphics. It supports:

* **Automatic aggregation and statistical estimation**
* **Support for categorical and numeric data**
* **Built-in themes for consistent visuals**
* **Integration with pandas for plotting DataFrames directly**

---

## Types of Functions

Seaborn functions are grouped into two types:

| Function Type    | Description                                        |
| ---------------- | -------------------------------------------------- |
| **Figure-Level** | Create entire figure (can control facets/subplots) |
| **Axis-Level**   | Draw plot on a single matplotlib `Axes` object     |

**Examples:**

* `sns.relplot()` → Figure-level
* `sns.scatterplot()` → Axis-level

---

## Main Plot Categories

---

### 1. Relational Plots

Used to show relationships between **two or more variables** — often numerical.

| Function            | Type         | Description                       |
| ------------------- | ------------ | --------------------------------- |
| `sns.scatterplot()` | Axis-level   | Basic scatter plot                |
| `sns.lineplot()`    | Axis-level   | Line plot with confidence band    |
| `sns.relplot()`     | Figure-level | Wraps scatter or line with facets |

---

### 2. Categorical Plots

Used for comparing **categories** — grouped into three types:

#### Categorical Scatter Plots

* `sns.stripplot()`
* `sns.swarmplot()`

#### Categorical Distribution Plots

* `sns.boxplot()`
* `sns.violinplot()`

#### Categorical Estimate Plots (show central tendency)

* `sns.barplot()`
* `sns.pointplot()`
* `sns.countplot()`

---

### 3. Distribution Plots

Visualize **distributions** of a single variable or comparisons between variables.

| Function         | Description                    |
| ---------------- | ------------------------------ |
| `sns.histplot()` | Histogram                      |
| `sns.kdeplot()`  | Kernel density estimate plot   |
| `sns.displot()`  | Figure-level distribution plot |

---

### 4. Regression Plots

Plot relationships with **regression fits**.

| Function        | Type         | Description                            |
| --------------- | ------------ | -------------------------------------- |
| `sns.regplot()` | Axis-level   | Scatterplot with regression line       |
| `sns.lmplot()`  | Figure-level | Wraps `regplot` with FacetGrid support |

Both plot the best-fit line with confidence interval for `y ~ x`.

---

### 5. Matrix Plots

Used for **correlation, heatmaps, and clustering**.

| Function           | Description                     |
| ------------------ | ------------------------------- |
| `sns.heatmap()`    | Color-coded matrix              |
| `sns.clustermap()` | Dendrogram + heatmap clustering |

---

### 6. Multiplots

Used for combining multiple plots into a grid.

| Function          | Description                              |
| ----------------- | ---------------------------------------- |
| `sns.FacetGrid()` | Create multi-subplot grid from variables |
| `sns.PairGrid()`  | Matrix of plots for pairwise comparisons |
| `sns.pairplot()`  | Shortcut for common pairwise plots       |
| `sns.JointGrid()` | Combine scatterplot and histograms       |
| `sns.jointplot()` | Figure-level shortcut for JointGrid      |

---

## Function Reference Table

| Plot Type    | Axis-Level Functions                    | Figure-Level Functions                                        |
| ------------ | --------------------------------------- | ------------------------------------------------------------- |
| Relational   | `scatterplot`, `lineplot`               | `relplot`                                                     |
| Categorical  | `stripplot`, `boxplot`, `barplot`, etc. | `catplot` (wraps multiple)                                    |
| Distribution | `histplot`, `kdeplot`                   | `displot`                                                     |
| Regression   | `regplot`                               | `lmplot`                                                      |
| Matrix       | `heatmap`                               | `clustermap`                                                  |
| Multi-plot   | -                                       | `pairplot`, `jointplot`, `FacetGrid`, `PairGrid`, `JointGrid` |

---

## References

* [Seaborn API Reference](https://seaborn.pydata.org/api.html)
* [Tutorial & Examples](https://seaborn.pydata.org/tutorial.html)
* [Seaborn vs Matplotlib](https://seaborn.pydata.org/introduction.html)

---

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