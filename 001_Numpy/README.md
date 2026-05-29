# 📘 NumPy Fundamentals, Advanced Concepts & Tricks

A concise guide to mastering **NumPy**, one of the most powerful libraries for numerical computing in Python.

---

## 📌 Table of Contents

- [📘 NumPy Fundamentals, Advanced Concepts \& Tricks](#-numpy-fundamentals-advanced-concepts--tricks)
  - [📌 Table of Contents](#-table-of-contents)
  - [🧠 What is NumPy?](#-what-is-numpy)
  - [🛠️ Creating NumPy Arrays](#️-creating-numpy-arrays)
  - [🧾 Array Attributes](#-array-attributes)
  - [➕ Array Operations](#-array-operations)
  - [📊 Array Functions](#-array-functions)
  - [🔍 Indexing \& Slicing](#-indexing--slicing)
  - [🔁 Iteration](#-iteration)
  - [🔄 Reshaping Arrays](#-reshaping-arrays)
  - [🔗 Stacking \& Splitting](#-stacking--splitting)
- [🚀 NumPy Advanced](#-numpy-advanced)
  - [🔎 Advanced Indexing](#-advanced-indexing)
  - [📐 Broadcasting](#-broadcasting)
  - [🕳️ Working with Missing Values](#️-working-with-missing-values)
  - [🎲 Random Module](#-random-module)
  - [📈 Plotting Graphs](#-plotting-graphs)
- [🧰 NumPy Functions](#-numpy-functions)
- [📚 Resources](#-resources)

---

## 🧠 What is NumPy?

An introduction to NumPy and how it compares to standard Python data structures like lists.

* NumPy Arrays vs Python Sequences
* Benefits of using NumPy

---

## 🛠️ Creating NumPy Arrays

Learn different ways to create arrays:

* `np.array()`
* `np.arange()`
* `reshape()`
* `np.zeros()` & `np.ones()`
* `np.random.rand()`
* `np.linspace()`
* `np.identity()`

---

## 🧾 Array Attributes

Understand basic attributes of arrays:

* `ndim`
* `shape`
* `size`
* `itemsize`
* `dtype`

---

## ➕ Array Operations

Perform operations directly on arrays:

* Scalar Operations
* Relational Operations
* Vector Operations

---

## 📊 Array Functions

Common and useful functions:

* `np.round()`, `np.isin()`, comparison ops
* `min`, `max`, `sum`, `prod`
* `mean`, `median`, `std`, `var`
* Trigonometric: `sin`, `cos`, etc.
* `round()`, `floor()`, `ceil()`

---

## 🔍 Indexing & Slicing

Accessing array elements:

* Basic Indexing
* Slicing Techniques

---

## 🔁 Iteration

* Using `np.nditer()` for looping

---

## 🔄 Reshaping Arrays

Manipulate array shape:

* `np.reshape()`
* `np.transpose()`
* `ravel()`

---

## 🔗 Stacking & Splitting

Combining and breaking arrays:

**Stacking:**

* `np.hstack()`
* `np.vstack()`

**Splitting:**

* `np.hsplit()`
* `np.vsplit()`

---

# 🚀 NumPy Advanced

Deep dive into advanced usage:

## 🔎 Advanced Indexing

* Normal Indexing & Slicing
* Fancy Indexing
* Boolean Indexing

## 📐 Broadcasting

* What is Broadcasting?
* Broadcasting Rules
* Using broadcasting in math formulas

## 🕳️ Working with Missing Values

* `np.nan`
* `np.isnan()`

## 🎲 Random Module

* Generating random data

## 📈 Plotting Graphs

* Using meshgrids and visualizing arrays

---

# 🧰 NumPy Functions

Handy utilities and lesser-known functions:

| Function              | Description                                                          | Documentation Link                                                                        |
| --------------------- | -------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `np.append()`         | Append values to the end of an array.                                | [Link](https://numpy.org/doc/stable/reference/generated/numpy.append.html)                |
| `np.concatenate()`    | Join a sequence of arrays along an existing axis.                    | [Link](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html)           |
| `np.unique()`         | Find the unique elements of an array.                                | [Link](https://numpy.org/doc/stable/reference/generated/numpy.unique.html)                |
| `np.expand_dims()`    | Expand the shape of an array by adding a new axis.                   | [Link](https://numpy.org/doc/stable/reference/generated/numpy.expand_dims.html)           |
| `np.where()`          | Return elements chosen from `x` or `y` depending on condition.       | [Link](https://numpy.org/doc/stable/reference/generated/numpy.where.html)                 |
| `np.argmax()`         | Return indices of the maximum values along an axis.                  | [Link](https://numpy.org/doc/stable/reference/generated/numpy.argmax.html)                |
| `np.cumsum()`         | Return the cumulative sum of the elements along a given axis.        | [Link](https://numpy.org/doc/stable/reference/generated/numpy.cumsum.html)                |
| `np.percentile()`     | Compute the nth percentile of the given data.                        | [Link](https://numpy.org/doc/stable/reference/generated/numpy.percentile.html)            |
| `np.histogram()`      | Compute the histogram of a set of data.                              | [Link](https://numpy.org/doc/stable/reference/generated/numpy.histogram.html)             |
| `np.corrcoef()`       | Return Pearson product-moment correlation coefficients.              | [Link](https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html)              |
| `np.isin()`           | Test whether elements of `a` are present in `b`.                     | [Link](https://numpy.org/doc/stable/reference/generated/numpy.isin.html)                  |
| `np.flip()`           | Reverse the order of elements in an array along the given axis.      | [Link](https://numpy.org/doc/stable/reference/generated/numpy.flip.html)                  |
| `np.put()`            | Replaces specified elements of an array with given values.           | [Link](https://numpy.org/doc/stable/reference/generated/numpy.put.html)                   |
| `np.delete()`         | Return a new array with sub-arrays along an axis deleted.            | [Link](https://numpy.org/doc/stable/reference/generated/numpy.delete.html)                |
| `np.union1d()`        | Find the union of two arrays.                                        | [Link](https://numpy.org/doc/stable/reference/generated/numpy.union1d.html)               |
| `np.intersect1d()`    | Find the intersection of two arrays.                                 | [Link](https://numpy.org/doc/stable/reference/generated/numpy.intersect1d.html)           |
| `np.setdiff1d()`      | Find the set difference of two arrays.                               | [Link](https://numpy.org/doc/stable/reference/generated/numpy.setdiff1d.html)             |
| `np.setxor1d()`       | Find the set exclusive-or of two arrays.                             | [Link](https://numpy.org/doc/stable/reference/generated/numpy.setxor1d.html)              |
| `np.clip()`           | Clip (limit) the values in an array.                                 | [Link](https://numpy.org/doc/stable/reference/generated/numpy.clip.html)                  |
| `np.swapaxes()`       | Interchange two axes of an array.                                    | [Link](https://numpy.org/doc/stable/reference/generated/numpy.swapaxes.html)              |
| `np.random.uniform()` | Return random floats in the half-open interval \[low, high).         | [Link](https://numpy.org/doc/stable/reference/random/generated/numpy.random.uniform.html) |
| `np.count_nonzero()`  | Count the number of non-zero elements in an array.                   | [Link](https://numpy.org/doc/stable/reference/generated/numpy.count_nonzero.html)         |
| `np.allclose()`       | Return True if two arrays are element-wise equal within a tolerance. | [Link](https://numpy.org/doc/stable/reference/generated/numpy.allclose.html)              |
| `np.equal()`          | Return (a == b) element-wise.                                        | [Link](https://numpy.org/doc/stable/reference/generated/numpy.equal.html)                 |
| `np.array()`                                           | Create a NumPy array from a list or tuple.                        | [Link](https://numpy.org/doc/stable/reference/generated/numpy.array.html)                    |
| `np.arange()`                                          | Return evenly spaced values within a given interval.              | [Link](https://numpy.org/doc/stable/reference/generated/numpy.arange.html)                   |
| `reshape()`                                            | Give a new shape to an array without changing its data.           | [Link](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html)                  |
| `np.zeros()`                                           | Return a new array of given shape and type, filled with zeros.    | [Link](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html)                    |
| `np.ones()`                                            | Return a new array of given shape and type, filled with ones.     | [Link](https://numpy.org/doc/stable/reference/generated/numpy.ones.html)                     |
| `np.random.rand()`                                     | Return random values in a given shape.                            | [Link](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html)       |
| `np.linspace()`                                        | Return evenly spaced numbers over a specified interval.           | [Link](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)                 |
| `ndim`                                                 | Number of array dimensions.                                       | [Link](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.ndim.html)             |
| `shape`                                                | Tuple of array dimensions.                                        | [Link](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.shape.html)            |
| `size`                                                 | Number of elements in the array.                                  | [Link](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.size.html)             |
| `itemsize`                                             | Size in bytes of one element of the array.                        | [Link](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.itemsize.html)         |
| `dtype`                                                | Data type of the array's elements.                                | [Link](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.dtype.html)            |
| `np.round()`                                           | Round an array to the given number of decimals.                   | [Link](https://numpy.org/doc/stable/reference/generated/numpy.round.html)                    |
| `np.isin()`                                            | Test whether elements of a are present in b.                      | [Link](https://numpy.org/doc/stable/reference/generated/numpy.isin.html)                     |
| Comparison ops (`==`, `!=`, `<`, `>`, `<=`, `>=`)      | Element-wise comparison operators.                                | [Link](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#array-attributes) |
| `min`, `max`, `sum`, `prod`                            | Compute the minimum, maximum, sum, and product of array elements. | [Link](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#array-attributes) |
| `mean`, `median`, `std`, `var`                         | Compute the mean, median, standard deviation, and variance.       | [Link](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#array-attributes) |
| Trigonometric functions (`np.sin()`, `np.cos()`, etc.) | Compute trigonometric functions.                                  | [Link](https://numpy.org/doc/stable/reference/generated/numpy.sin.html)                      |
| `round()`, `floor()`, `ceil()`                         | Round, floor, and ceiling functions.                              | [Link](https://numpy.org/doc/stable/reference/generated/numpy.floor.html)                    |
| `np.identity()`                                        | Return the identity matrix.                                       | [Link](https://numpy.org/doc/stable/reference/generated/numpy.identity.html)                 |
| `np.reshape()`                                         | Give a new shape to an array without changing its data.           | [Link](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html)                  |
| `np.transpose()`                                       | Permute the dimensions of an array.                               | [Link](https://numpy.org/doc/stable/reference/generated/numpy.transpose.html)                |
| `np.hstack()`                                          | Stack arrays in sequence horizontally (column-wise).              | [Link](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html)                   |
| `np.vstack()`                                          | Stack arrays in sequence vertically (row-wise).                   | [Link](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html)                   |
| `np.hsplit()`                                          | Split an array into multiple sub-arrays horizontally.             | [Link](https://numpy.org/doc/stable/reference/generated/numpy.hsplit.html)                   |
| `np.vsplit()`                                          | Split an array into multiple sub-arrays vertically.               | [Link](https://numpy.org/doc/stable/reference/generated/numpy.vsplit.html)                   |
| `np.nan`                                               | Represents a Not-a-Number (NaN) value.                            | [Link](https://numpy.org/doc/stable/reference/constants.html#numpy.nan)                      |
| `np.isnan()`                                           | Test element-wise for NaN.                                        | [Link](https://numpy.org/doc/stable/reference/generated/numpy.isnan.html)                    |
| `ravel()`                                              | Return a flattened array.                                         | [Link](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.ravel.html)            |

---


# 📚 Resources
Thank you to my Dear Nitish Sir 🙏💝
https://www.youtube.com/playlist?list=PLKnIA16_RmvbAlyx4_rdtR66B7EHX5k3z