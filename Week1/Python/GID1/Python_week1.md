# Introduction to Python

#### About Python Language  

Remember that you are intelligent and you can learn, but the computer is simple and very fast, but can not learn by itself. Therefore, in order for you to communicate instructions to the computer it is easier for you to learn a computer Language (e.g. Python) than for the computer to learn English.

Python can be **asy to pick up and friendly to learn**. [Python](https://www.python.org/) is a **general-purpose** interpreted , interactive, object-oriented, and high-level programming language. It was created by Guido van Rossum during 1985- 1990. There are two main python versions: 2.7 and 3. For this course we will use 2.7 since it is the most common or popular used.  

#### Basic Practise

Let's get familiar with python by playing in the terminal in the interactive mode (you type a line at a time and the interpreter responds). You invoke the interpreter and brings up the following prompt:

``` python
$python
Python 2.7.9 (default, Sep 17 2016, 20:26:04)
[GCC 4.9.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Strings, integers, and floating points:
``` python
>>> print "Hello, Python!"
>>> x = 1         # Integer assignment
>>> y = 1005.00   # Floating points
>>> name = "John" # A string
>>> print x
>>> print y
>>> print name  
```
In Python, the [standard order of operations](https://en.wikibooks.org/wiki/Python_Programming/Basic_Math) are evaluated from left to right following order (memorized by many as PEMDAS):


| Name        | Syntax           | Description  |
| ------------- |:-------------:| :-----|
| **P**arentheses     | ( ... ) | Happening before operating on anything else.|
| **E**xponents     | **  |  An exponent is a simply short multiplication or division, it should be evaluated before them. |
| **M**ultiplication and **D**ivision | * / |  Multiplication is rapid addition and must happen first. |
| **A**ddition and **S**ubtraction | + -  |     |

``` python
>>> 3/4 * 5  # First division and then Multiplication
>>> 3.0 / 4 * 5
>>>(3.0 / 4) * 4
```
