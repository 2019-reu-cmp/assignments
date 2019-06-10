# `numpy` and `matplotlib`

Chris Seymour

`seymour.16@nd.edu`

June 10, 2019

---

# Goals

1. Learn about `numpys`'s `ndarray` class (i.e.) `np.array`s)
  - mathematical vectors/matrices [numpy](https://www.numpy.org/)
2. Be able to use  `numpy` to store and manipulate data
3. Be able to make a line or scatter plot
4. Be able to make a histogram

---

# Numpy

---

## `import` Convention

```python
import numpy as np
```

---

## Initialize an array

All of these create the same array:

```python
a = np.array( [0, 1, 2] )
b = np.arange(3)
c = np.linspace(0, 2, 3)
```
---

## Creating Empty Arrays

`np.zeros()` or `np.empty()` to create empty lists

```python
d = np.zeros( shape=(4) ) # 1-D vector of four zeros
d_int = np.zeros( shape=(4), dtype=int ) # can specify the data type
e = np.empty( (40)  )
```
 -`np.empty()` is likely to have crazy values initially, so be careful

for a 2-D matrix
```python
np.zeros( shape=(2,4) ) # create a 2 row, 4 column matrix of zeros
```
  - the `shape` argument gives the dimensions of the array `shape=(rows,columns)`
  - rows and colums must be integers
  - `shape` will always be a tuple, so it's good practice to use parenthesis (even on 1-D arrays)



---


## Math with arrays

```python

```
Examples:
 a and b are `numpy.ndarrays` 
 - add one to each element in the array: `a+1`
 - add the arrays element by element: `a + b` (must be the same `shape`)
 - apply a fucntion to each element of the array `np.sqrt(a)`

Basic stats:
 - mean: `a.mean()` 
   - for multidimensional arrays, specify an axis: `a.mean(axis=0)`
 - standard deviation: `a.std()`
 - sum along an axis `a.sum( axis=1 )`

Linear Algebra: 
 - `a.dot(b)` dot product
 - `np.cross(a, b)` cross product

---

## Manipulating arrays

- Transpose with `a.T`
- Slices similar to lists, `a[:,1]`  
    - [slice notation](https://stackoverflow.com/questions/509211/understanding-slice-notation)

checking and changing the number of rows and columns
```python
a.shape # returns the shape (not a function!)
a.reshape( shape ) # change the shape, shape is a tuple in the form: (rows, columns)

```
---

## Reading Numerical Data

- We can use our regular python method of reading files, or use `np.loadtxt()`

```python
a, b = np.loadtxt(filename, unpack=True)
```

---

# Plotting

`import matplotlib.pyplot as plt`

---

## Basics plotting

- At the most basic level, `plt.plot(x, y)` will create a connected line graph
- You can pass additional options to plot to change the graph type
- Everything can be controlled, so look at the documentation
- To display, you need to run `plt.show()`, and program execution waits

```python
import matplotlib.pyplot as plt
plt.plot(x, y)
plt.show()
```

The `matplotlib.pyplot` documentation [http://matplotlib.org/api/pyplot_api.html] is vital.

---

## Plotting Example

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
  - can check value stored at x=0 `print( y[4999] )`
 
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

<!-- 
- If you need random points, you should use `numpy.random.rand(r, c)` or
  `numpy.random.rand(n)` (if you just want a one-dimensional array)
   -->

---

## Histograms
- Histograms are made differently, and take in an array that then generates the
  resulting histogram: 
```python
plt.hist(data, bins=5)
```

Check out this [example](http://matplotlib.org/1.2.1/examples/pylab_examples/histogram_demo.html).

---

## Practice

Total observed number of sunspots for each month starting in January, 1749 

- Read in `sunspots.tsv`, and plot it
- Change the plot to *not* be a connected line graph (i.e. a scatter plot)
- On the same plot, include a moving average (window = 5 months)

Practice with handout05

Read Newman Ch 5 for next time

---