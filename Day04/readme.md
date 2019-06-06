# Special Topics in Standard Python

June 6, 2019

Chris Seymour
`seymour.16@nd.edu`

----

# Todays goals

1. Review: Be able to import and manipulate text or data from a file, arbitrary prescision
2. Know what `format` is and how to use it
3. Be able to describe how and when to use `range`, `enumerate`, and `zip`
4. Be able to use at least one special container form the `collections` class
5. Know how and when to use `try`, and `except`, and `assert`

---

# Git

* `pull` from Classroom
* add to your assignments directory
* `commit` changes
* `push` to your own remote repository

---

# Last Time

* `northwind.txt`
    * Able to count the occurrence of each word?
    * see `Day03/countwords.py` 
* `sunspots.txt`
    * What was hard?


---

## Arbitrary Prescision
* 1/pi estimation `pi.py`
    * mpmath
```python
from mpmath import mp
mp.dps = 50 #set prescision to 50 digits (decimal)
pi = mp.mpf( mp.pi )
pi_2 = mp.fdiv(pi, 2) 

mp.fsub(2, 2E-5) #bad
mp.fsub(2, '2E-5') #good 

```
    * Decimal
```python
import decimal as de
de.getcontext().prec = 50 #set prescision to 50 digits (decimal)
pi = de.Decimal('3.14159...') #must define pi
```

see `Day03/arbitrary_prescision.py` for example

[http://mpmath.org/doc/current/]
---

## File I/O

* For *prose* -- `f.read()` is sufficient

* For *tabular data* -- `f.readline()` or `f.readlines()` can be helpful

```python
with open('data.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        split_line = line.split()
        #...process the line
```

---

## `.split()`

* don't forget about  `.split()`
```python
In [1]: run_numbers = '123 134 167 176 182'.split()

In [2]: run_numbers
Out[2]: ['123', '134', '167', '176', '182']
```
they are still strings...

---

# Better printing

using `format`

```python
s1 = 'num: {}'.format(value)
s2 = 'num: {:.4f}'.format(value)
```

<!-- 
    2. Know `format`
 -->
 --- 

## Better printing 

using `format` f-strings

```python
s1 = f'num: {value}'
s2 = f'num: {value:.4f}'
```

<!-- 
    2. Know `f-string`
 -->

---

# More Lists and Looping

---

## Lists for math

- If a list contains *only* numbers, we can treat it as a vector:

`v = [0., 0., -9.81]`

- If a nested list contains *only* numbers, we can treat it as a matrix:

`m = [[0, 1], [1, 1]]`

<!-- 
3. range, enumerate, zip
 -->

---

## Lists expanded

Create a string from a list: `''.join(l)`

- everything in `l` **must be a string**

<!-- 
3. range, enumerate, zip
 -->

---

## List Comprehension

`.append()` is slow, so use this trick: 

- `l = [i**2 for i in range(10)]`

- This is extremely useful for a lot of different situations, like file
    processing:

```python
with open(filename, 'r') as f:
    data = [line.split() for line in f]
```

---

## Special for-looping functions

We already know about `range`
```python
xs = [x for x in range(10)]
```

`enumerate` gets the index and value
```python
ix_pairs = [(i,x) for i,x in enumerate(xs)]
```
---

### zip

`zip` "walks" through two lists at the same time
``` python
A = (0, 1, 2, 3)
B = (5, 10, 15, 20)
for a,b in zip(A,B):
    print(a, b, a+b) 

ab_dict = dict( zip(A, B) ) #dict with A as the key and B as the values (no longer ordered)

ab_pairs = [(a,b) for a,b in zip(A, B)] #ab_pairs is a list of four length 2 tuples

A2. B2 = zip(*ab_pairs) #go back to two, length 4 lists

```

<!-- 
3. range, enumerate, zip

Show in REPL
 -->

---

# Special collections

Aside from lists, tuples, sets, and dictionaries, there are a few special-case
collections we can use

```python
import collections

counter = collections.Counter()
colors = ['red', 'blue', 'red',
          'green', 'blue', 'blue']
for word in colors:
    counter[word] += 1
```
<!-->
```python
Isotope = collections.namedtuple(
    'Isotope', ['symbol', 'A', 'Z'])
he4 = Isotope('He4', 4, 2)
```
-->

<!-- 
4. collections!

Show in REPL
 -->

---

## Errors and Exception Handling

We place operations within `try`-blocks to safeguard ourselves from unwanted
operations 
 - (bad division, importing the wrong thing, requiring user input, etc.)

```python
try:
    x = 5 / 0
except Exception as e:
    print('Error:', e)
    x = 0
```

* `Exception`  the most generic 
    - Will often use `TypeError` or `ZeroDivisionError` or `ValueError`
* `e` now contains the Exception message, but not the Exception name.

see `/Day04/try-except.py` for examples

[https://docs.python.org/3/tutorial/errors.html]
<!-- 
5. Exception handling.
 -->

---

# `assert` statement

`assert <condition>`

equivilent to

```python
if not condition:
    raise AssertionError()
```
- stops program execution if condition is false

```python
eg = 1.5 
assert type(eg) == int, "eg is not an int!"
```

<!-- 
5. Exception handling.
useful for detecting errors early, instead of later as a side effect
 -->

---

# Practice Time!

- Practice with the handout

- Import `nothwind.txt` then separate by word
    + Try to count how many times each word appears 
    + Count how many times each letter appears.
- Calculate the average sunspot form `sunspots.txt` 
    + Can you count the days who's number of sunspots fell with an arbitrary range?
    + i.e. Implement a `count(low, high)` function that returns the number of days with sunspots above low and below high.

Read Ch 3 of Mark Newman's _Computational Physics_

**Office Hours:** Tuesdays at 3pm, NSH 384 K
