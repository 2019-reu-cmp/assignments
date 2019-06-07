# `numpy` and `matplotlib`

Chris Seymour

`seymour.16@nd.edu`

June 6, 2018

---

# Goals

1. Learn about `np.array`s and what makes them more useful mathematical vectors/matrices
2. Be able to read data in from disk via `numpy`
2. Be able to make a line or scatter plot
3. Be able to make a histogram

---

# Review Homework

- Import `nothwind.txt` then separate by word
    + Try to count how many times each word appears
- Calculate the average sunspot form `sunspots.txt` 
    + Can you count the days who's number of sunspots fell with an arbitrary range?

---

# Day 04 Handout

5. Update dot product to use `zip` or `enumerate`

---

# Convention

```python
import numpy as np
import matplotlib.pyplot as plt
```

---

# Numpy

---

## Create an array

All of these create the same array:

```python
a = np.array([0, 1, 2])
b = np.arange(3)
c = np.linspace(0, 2, 3)
```

<!-- 
- Basic array is created with `numpy.array([0, 1, 2])` unless created directly
  with a special function

- Arrays work differently than lists when talking about math and slices
  - transposition `a.T`, dot products `a.dot(b)`, statistics `a.mean()`
  - fancy slices for matrix-like objects `a[:, 1]`

- Basic math operations are also included, but act on each element separately

- If you need random points, you should use `numpy.random.rand(r, c)` or
  `numpy.random.rand(n)` (if you just want a one-dimensional array)
   -->


---

## Random points

```python
from random import random
points = [[random(), random()] 
           for _ in range(100)]
```

```python
points = np.random.rand(100, 2)
```

How would you separate these out into *x* and *y* arrays?

---

### Aside

What is `_` in `for _ in range(100)` mean?

[https://dbader.org/blog/meaning-of-underscores-in-python](https://dbader.org/blog/meaning-of-underscores-in-python)

---

## Math with arrays

Basic math: `a + b`, `np.sqrt(a)`

Basic stats: `a.mean()`, `a.std()`

- for multidimensional arrays, specify an axis if necessary: `a.mean(axis=0)`

Linear Algebra: `a.dot(b)`, `np.cross(a, b)`

---

## Manipulating arrays

- Transpose with `a.T`
- Slices similar to lists, `a[:,1]`

---

## Read Data

- We can use our regular python version, or use `np.loadtxt()`
```python
a, b = np.loadtxt(filename, unpack=True)
```

---

# Let's plot!

---

# Basics plotting

```python
plt.figure('MyFirstFigure')
plt.plot(x, y)
plt.show()
```

Need help? [http://matplotlib.org/api/pyplot_api.html](http://matplotlib.org/api/pyplot_api.html)

<!-- 
- As an example, let's plot sin(x)/x over some range, just to see how numpy
  handles divide-by-zero:
  ```python
  import numpy
  import matplotlib.pyplot as plt

  x = numpy.linspace(-10, 10, 9999)  # to ensure zero is in the array
  y = numpy.sin(x)/x
  plt.plot(x, y)
  plt.show()
  ```
  - `nan` (not-a-number) values don't affect us at all! We're essentially free
    from worry about them (but you should be careful anyway)
  - We know that `0` is in the array too: `x[4999] == 0` or `assert 0 in x`
 -->
 
---

## Labels

```python
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title(r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
```
You can use LaTeX!

---

## Histograms

```python
plt.hist(a)
```

Look up the options and this [example](http://matplotlib.org/1.2.1/examples/pylab_examples/histogram_demo.html).

---

## Sunspots

Total observed number of sunspots for each month starting in January, 1749 

- Read in `sunspots.tsv`, and plot it
- Change the plot to *not* be a connected line graph
- On the same plot, include a moving average (window = 5)


---

# Git review


---

# Practice

- Handout
- Read in `sunspots.tsv` and make a histogram of the counts/month
- Read in `sunspots.tsv`, and make a scatter plot of the data
- Add a moving average to you
- Read Newman Ch 5