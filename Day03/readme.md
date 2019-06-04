# Looping, Iterables, and File Processing

Chris Seymour
June 04, 2019

---

## Class Details

* Office Hours: Tuesdays at 3pm, ~~NSH 101~~ Nieuwland Science Hall 284 K
* Today's material is at 
    - `https://github.com/2019-reu-cmp/assignments`

---

# Goals

1. ~~Be able to use `git`'s `pull`, `add`, `commit`, and `push` commands~~
2. Be able to use `while` and `for` loops
3. Iterables
4. Be able to import and manipulate text or data from a file

---

# Git

* `pull` from Classroom
* copy `change_this_file.txt`, `sunspots.txt` and `northwind.txt` to _assignments-yourname/Day03_ folder
* change `change_this_file.txt`
* `add` and `commit` changes
* `push` to your own remote repository

---

# From last time...

* `if`, `elif`, `else` case structures
```python
def CheckNumber(n):
    '''check how the number compares to 5'''
    if x > 5:
        print('greater than 5!')
    elif x < 5:
        print('less than 5!')
    else:
        print("it's 5!")
```
---

# From last time...
* What are lists, tuples, sets, and dictionaries?
    * How to use sets. `s = {1,2,3} or s2 = set( (1,2,3) )`
        * `s.add(4)` and `s.remove(3)`
        * `s.difference(s2)` or `s-s2` ("in s but not in s2")
    * How to access a dictionary by key. 
    
        * `d = {'a', 1}` -> access it with: `d['a']` (i.e. value associated with key 'a')

* How would you check if a variable is of a certain type?
    - e.g. int, float, string, list, tuple, dict
* What it means to be Imutable.
[https://docs.python.org/3/tutorial/datastructures.html]
---

# Loops

---

## `while`

Basic structure:

```python
while condition is True:
    do_something()
    update_condition()
```

- condition can be anything that returns a `bool` (*boolean*, usually math-related)
- without update, infinite loop 

---

## `for`

Basic structure:

```python
for item in container:
    do_something_with(item)
```

- container is an *iterable* (list, tuple, string, or *generator*)
- if you just want numbers, use `range(n)`

---



## Estimating pi

Srinivasa Ramanujan discovered an infinite series for pi:

<!-- ![](./Images/pi.png) -->
![](pi.png)


---

# File Input/Output (I/O)

## Filenames -- UNIX

* `.` is current directory or folder
* `..` is the directory above
* `/` to separate directories


---

## Basic file reading

```python
f = open(filename, 'r')
f.read()
f.close()
```

---

## Better file reading

```python
with open(filename, 'r') as f:
    wholefile = f.read()
    #or, you can initialize a list to store your data
    data = []
    for line in f:
        data.append(line)
```
 
 ---
There is also a very useful `.readline()` method that reads one line at a time instead of the whole file at once.

`.readlines()` will break the file into an list of strings split at the `\n` characters.

---

## String detour
* `print( repr( object ) )` will show you hidden characters (good for diagnosing problems)
* `s.strip()` remove any trailing whitespace and `\n` or `\r` characters from a string
* `s.split()` split string into a list (typically space or comma delimited)
* `int(s)` convert a string to an int
* `float(s)` convert a string to a float
* `\n` newline

---

# Practice Time!

- Practice with the handout
- Import `northwind.txt` then separate by word
    + Try to count how many times each word appears
- Calculate the average number of sunspots per day form `sunspots.txt` 
    + Can you count the days who's number of sunspots fell with an arbitrary range?
    + i.e. Implement a `count(low, high)` function that returns the number of days with sunspots above low and below high.

*Readings* - nothing new, just catch up if you need to.