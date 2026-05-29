# Matplotlib Notes

This repository contains notes and examples for **visualizing data using matplotlib**. It covers basic 2D plots, chart types, styling, saving figures, and advanced topics such as 3D plotting and subplots.

---

## Table of Contents

- [Matplotlib Notes](#matplotlib-notes)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Basic Plot Types](#basic-plot-types)
    - [2D Line Plot](#2d-line-plot)
    - [Bar Chart](#bar-chart)
    - [Scatter Plot](#scatter-plot)
    - [Histogram](#histogram)
    - [Pie Chart](#pie-chart)
  - [Changing Styles](#changing-styles)
  - [Saving Figures](#saving-figures)
  - [Advanced Matplotlib](#advanced-matplotlib)
    - [Colored Scatter Plots](#colored-scatter-plots)
    - [Changing Plot Size](#changing-plot-size)
    - [Annotations](#annotations)
    - [Horizontal and Vertical Lines](#horizontal-and-vertical-lines)
    - [Subplots](#subplots)
    - [3D Plots](#3d-plots)
    - [Heatmaps](#heatmaps)
    - [Plotting with Pandas](#plotting-with-pandas)
  - [Function Reference Table](#function-reference-table)
  - [References](#references)

---

## Overview

Matplotlib is a powerful library for data visualization in Python. It supports line plots, bar charts, scatter plots, histograms, and more. For more advanced use, matplotlib integrates well with 3D plotting and pandas.

---

## Basic Plot Types

### 2D Line Plot

```python
import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [2, 4, 1]

plt.plot(x, y)
plt.title("Line Plot")
plt.show()
```

---

### Bar Chart

```python
categories = ['A', 'B', 'C']
values = [10, 24, 36]

plt.bar(categories, values)
plt.title("Bar Chart")
plt.show()
```

---

### Scatter Plot

```python
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.show()
```

---

### Histogram

```python
data = [1, 2, 1, 3, 2, 4, 5, 6]

plt.hist(data, bins=4)
plt.title("Histogram")
plt.show()
```

---

### Pie Chart

```python
labels = ['A', 'B', 'C']
sizes = [30, 45, 25]

plt.pie(sizes, labels=labels)
plt.title("Pie Chart")
plt.show()
```

---

## Changing Styles

```python
plt.style.use('ggplot')
```

Try other styles like: `'seaborn'`, `'fivethirtyeight'`, `'classic'`

---

## Saving Figures

```python
plt.savefig("plot.png")
```

You can specify format, dpi, and transparent background.

---

## Advanced Matplotlib

### Colored Scatter Plots

```python
colors = [10, 20, 30]
plt.scatter(x, y, c=colors, cmap='viridis')
```

---

### Changing Plot Size

```python
plt.figure(figsize=(10, 5))
```

---

### Annotations

```python
plt.annotate("Max Point", xy=(2, 4), xytext=(3, 4.5),
             arrowprops=dict(facecolor='black'))
```

---

### Horizontal and Vertical Lines

```python
plt.axhline(y=2, color='red', linestyle='--')
plt.axvline(x=2, color='blue', linestyle='--')
```

---

### Subplots

```python
fig, axs = plt.subplots(1, 2)
axs[0].plot([1, 2, 3], [1, 4, 9])
axs[1].bar(['A', 'B'], [3, 7])
```

---

### 3D Plots

```python
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 3D Scatter
ax.scatter(x, y, [1, 3, 5])

# 3D Line
ax.plot(x, y, [0, 1, 2])

# 3D Surface
import numpy as np
X, Y = np.meshgrid(np.linspace(-5, 5, 30), np.linspace(-5, 5, 30))
Z = np.sin(np.sqrt(X**2 + Y**2))
ax.plot_surface(X, Y, Z, cmap='viridis')
```

---

### Heatmaps

```python
import seaborn as sns
import numpy as np

data = np.random.rand(4, 4)
sns.heatmap(data, annot=True, cmap='Blues')
```

---

### Plotting with Pandas

```python
import pandas as pd

df = pd.DataFrame({
    'x': [1, 2, 3],
    'y': [2, 4, 1]
})

df.plot(x='x', y='y', kind='line')
```

---

## Function Reference Table

| Function / Method               | Description                      |
| ------------------------------- | -------------------------------- |
| `plt.plot()`                    | 2D line plot                     |
| `plt.bar()`                     | Bar chart                        |
| `plt.scatter()`                 | Scatter plot                     |
| `plt.hist()`                    | Histogram                        |
| `plt.pie()`                     | Pie chart                        |
| `plt.style.use()`               | Change plot style                |
| `plt.savefig()`                 | Save figure                      |
| `plt.figure(figsize=())`        | Change figure size               |
| `plt.annotate()`                | Add annotation with arrow        |
| `plt.axhline() / plt.axvline()` | Draw horizontal or vertical line |
| `plt.subplots()`                | Create subplots                  |
| `ax.plot_surface()`             | 3D surface plot                  |
| `sns.heatmap()`                 | Create a heatmap (via Seaborn)   |
| `df.plot(kind=...)`             | Pandas integrated plotting       |

---

## References

* [Matplotlib Docs](https://matplotlib.org/stable/contents.html)
* [Pyplot Tutorial](https://matplotlib.org/stable/tutorials/introductory/pyplot.html)
* [3D Plotting](https://matplotlib.org/stable/gallery/mplot3d/index.html)
* [Seaborn Heatmaps](https://seaborn.pydata.org/generated/seaborn.heatmap.html)
* [Pandas Plotting](https://pandas.pydata.org/docs/user_guide/visualization.html)

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