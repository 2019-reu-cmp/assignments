<!-- $theme: default -->

# Introduction to Python

Chris Seymour
(modified from Ben Rose)

May 29, 2019

<!-- 
- I've been using python for about 7 years
- My research
-->

---

## Course Goal

Learn by doing

1. Be able to use Python to **do something** with scientific data
2. Teach yourself to learn more
3. Understand the basic Python vocabulary
5. Gain confidence in your programing skills

<!--
- A self-help class
- 
- Will start with a language foundation
	- Python terms will be italics
	- Then add python best practices
	- Then data!
- We'll use live coding interspersed with you doing individual and pair coding
- Worksheets
- Notes/presentations will be available
- More information on website 
-->

---
## Learning Goal: Day 1

1. Install and run Python 3.7
3. Learn where to find more information on about Python
2. Be able to write, save, and run a basic program like "Hello World"
5. Be able to describe the meaning of at least 10 Python specific terms

---

## Course Site

`chrisseymour.pythonanywhere.com/reu-python-2019`

- includes installation files, data, notes, schedule, etc.
- will be continually updated during the course

---

## Who are you?

<!--
- Research interests?
- Tech related interests?
- Programing skills
- Trade phone numbers
-->

---

## Getting Help

- Google/Stackoverflow 
    - `python3 [thing to search]` 
- Python documentation is very helpful: 
    - docs.python.org/3/
- The *interpreter* itself: `help(print)`
- External Resources section on the class website

<!--
- Course Goal 2: "Teach yourself to learn more"
- Class Goal: "Learn where to find more information on about Python"
- You will need this for the worksheet
-->


---

# Road Map

1. Introduction to Python
1. Introduction continued: Git & GitHub
1. Loops and File I/O
1. Special Topics in Standard Python
1. Introduction to NumPy/Matplotlib
1. Numerical Methods
1. Numerical Methods in SciPy
1. Final Project: Doing Science with Python

---

# Let's code!

python.org/downloads/
anaconda.com/distribution/


<!--
- Class Goal: "Install and run Python 3.6"
-->


---

## Math Operations

Basic arithmetic *operators*

```
+  -  *  **  /  //  %

import math
math.cos(math.pi)
```

<!--
5:00 PM
- What are each of these operators?
- Just numbers?
- Class Goal: "Be able to describe the meaning of at least 10 Python specific terms"
-->

---

## Functions

*Functions* - blocks of code

```
print('Hello, world!')
print(5**3)
len('physics')
```

<!--
- Useful blocks of code
- Build in or you can write your own
- Class Goal: "Be able to describe the meaning of at least 10 Python specific terms"
-->

---

## Variables

*Variables* store information for later.
Each variables is of a specific *type*.

```
name = 'Chris'
print(name)
full_name = name + ' Seymour'
print('My full name is', full_name)
type(name)
```

<!--
- operators can change!
- dynamic type
- Class Goal: "Be able to describe the meaning of at least 10 Python specific terms"
-->

---

## Tired of typing?

We can create a *program* (*module* or sometimes *script*) that we can just run, instead of typing everything in over and over again.

```python
#!/usr/bin/env python3
""" file.py -- description

Chris Seymour
2019-05-29
"""
# code goes here
print(5**2)
```

<!--
- module vs script
- Module docstring
- author, date, description, usage, program language?
- Class Goal: "Be able to describe the meaning of at least 10 Python specific terms"
-->

---

## Your own functions

```
def square_it(number):
    """ square any number
    
    Parameters
    ---------
    number : float
    	the number to sqaure


    Returns
    -------
    float
    	the square input number
    """
    return number**2
```

<!--
- def keyword
- :
- docstring
	- Parameters
		- name
		- type
		- description
	- Returns
		- no name!
- return keyword 
- Class Goal: "Be able to describe the meaning of at least 10 Python specific terms"
-->

---

## Worksheet 

* 6 questions
* 2 programs

<!--
5:30
- Class Goal: "Be able to write, save, and run a basic program like 'Hello World'"
- Class Goal: "Be able to describe the meaning of at least 10 Python specific terms"
- Course Goal: "Gain confidence in your programing skills"
-->
