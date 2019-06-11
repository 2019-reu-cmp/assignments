# Practice Python with Numerical Methods

Chris Seymour

`seymour.16@nd.edu`

June 11, 2019

---

# Goals

* Be able to write four numerical methods that can *do something*

---

# Review 

`sunspots.py` moving average example

---

## "Main" Topics in Computational Methods

1. Integration
1. Linear Algebra
1. Root Finding
1. Differential Equations

Explore these on your own too, since we won't be able to cover everything...

---


# Integration

Want to know area under curve, but don't know functional form of `f(x)`.

---

## Trapezoid method

1. Divide your interval into some number of sub-intervals

1. Each sub interval is a trapezoid, connecting the two points on the graph

```python
trap = dx * (f(x + dx) + f(x)) / 2
```

---

## Simpson's 3/8 rule

```python
h = (b - a) / 3
factor = (f(a) +
          3*f((2*a + b) / 3) +
          3*f((a + 2*b) / 3) +
          f(b))
integral = (3 * h / 8) * factor
```

---

## Extended Simpson's 3/8 rule (for n intervals)

```python
h = (b - a) / n
xi = a + i*h
integral = 3*h/8 * (
                f(x0) + 3*f(x1) + 
               3*f(x2) + 2*f(x3) + 3*f(x4) +
                ... + f(xn) )
```
This only works if `n` is a multiple of 3

---

# Root Finding

We already looked at a Bisection Method example,
	`assignments/Day02/bisection.py`.

---

## Alternatives to bisection

- Newton's method (from a Taylor expansion)
	- Need the function and it's first derivative)
	- Depends on the starting point you choose.
	- Iterative process
```python
x1 = x0 - f(x0)/f'(x0)
```

- Secant method (if we don't)
	- Only need the function (not the derivative).
	- Needs two starting points.
	- Iterative process
```python
x2 = x1 - f(x1) * (x1 - x0)/( f(x1) - f(x0) )
```

---

# Ordinary Differential Equations

`dy/dx = f(y,t)`

want to find solution for `y(t)`

---

## Euler's Method

`h` is some time step *delta t*

```python
y(t + h) = y(t) + dy/dt*h + O[h^2] 
```

where `dy/dt` is some function `f(y,t)`

i.e. `y(t + h) = y(t) + f(y,t)*h + O[h^2]`

---
## Example: Free Fall

`dy/dt = f(y,t) = v(t) = v0 - g*t`

```python
g = 9.81 #gravitational constant

h = 0.01 #step size
y,t = 0,0 #initial values

while t<1:
	#loop over values
	v = v0 - g*t
	y += v + t
	t += h
```

	- Values can be stored in arrays during loop to track progress
	- can be extended to coupled ODEs

---

# Practice

* Handout
* One more week of classes
* Office hours Tuesday 3pm in NSH 384 K
