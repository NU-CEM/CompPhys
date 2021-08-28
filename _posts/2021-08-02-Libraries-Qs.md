---
toc: false
layout: post
title: Libraries - quick test
hide: true
---

## Exploring the Math Module

1. What function from the `math` module can you use to calculate a square root
    *without* using `sqrt`?
2. Since the library contains this function, why does `sqrt` exist?


{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>

1. Using `help(math)` we see that we've got `pow(x,y)` in addition to `sqrt(x)`,
so we could use `pow(x, 0.5)` to find a square root.  
2. The `sqrt(x)` function is arguably more readable than `pow(x, 0.5)` when
implementing equations. Readability is a cornerstone of good programming, so it
makes sense to provide a special function for this specific common case.

Also, the design of Python's `math` library has its origin in the C standard,
which includes both `sqrt(x)` and `pow(x,y)`, so a little bit of the history
of programming is showing in Python's function names.  

</details>

{::options parse_block_html="false" /}

## Locating the Right Module

You want to select a random character from a string:

~~~python
bases = 'ACTTGCTTGAC'
~~~


1. Which [standard library][stdlib] module could help you?
2. Which function would you select from that module? Are there alternatives?
3. Try to write a program that uses the function.


{::options parse_block_html="true" /}
<details>
<summary markdown="span">Show answer</summary>

The [random module](randommod) seems like it could help you.

The string has 11 characters, each having a positional index from 0 to 10.
You could use `random.randrange` function (or the alias `random.randint`
if you find that easier to remember) to get a random integer between 0 and
10, and then pick out the character at that position:

~~~python
from random import randrange

random_index = randrange(len(bases))
print(bases[random_index])
~~~


or more compactly:

~~~python
from random import randrange

print(bases[randrange(len(bases))])
~~~


Perhaps you found the `random.sample` function? It allows for slightly
less typing:

~~~python
from random import sample

print(sample(bases, 1)[0])
~~~


Note that this function returns a list of values. We will learn about
lists in episode 11.

There's also other functions you could use, but with more convoluted
code as a result.

</details>

{::options parse_block_html="false" /}


## Jigsaw Puzzle (Parson's Problem) Programming Example

Rearrange the following statements so that a random
DNA base is printed and its index in the string.  Not all statements may be needed.  Feel free to use/add
intermediate variables.

~~~python
bases="ACTTGCTTGAC"
import math
import random
___ = random.randrange(n_bases)
___ = len(bases)
print("random base ", bases[___], "base index", ___)
~~~


{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>

~~~python
import math 
import random
bases = "ACTTGCTTGAC" 
n_bases = len(bases)
idx = random.randrange(n_bases)
print("random base", bases[idx], "base index", idx)
~~~

</details>

{::options parse_block_html="false" /}

## When Is Help Available?

When a colleague of yours types `help(math)`,
Python reports an error:

~~~output
NameError: name 'math' is not defined
~~~

What has your colleague forgotten to do?

{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>

Importing the math module (`import math`)

</details>

{::options parse_block_html="false" /}

## Importing With Aliases

1. Fill in the blanks so that the program below prints `90.0`.
2. Rewrite the program so that it uses `import` *without* `as`.
3. Which form do you find easier to read?

~~~python
import math as m
angle = ____.degrees(____.pi / 2)
print(____)
~~~


{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>

~~~python
import math as m
angle = m.degrees(m.pi / 2)
print(angle)
~~~

can bewritten as

~~~python
import math
angle = math.degrees(math.pi / 2)
print(angle)
~~~

Since you just wrote the code and are familiar with it, you might actually
find the first version easier to read. But when trying to read a huge piece
of code written by someone else, or when getting back to your own huge piece
of code after several months, non-abbreviated names are often easier, except
where there are clear abbreviation conventions.

</details>

{::options parse_block_html="false" /}
 

## There Are Many Ways To Import Libraries!

Match the following print statements with the appropriate library calls.

Print commands:

1. `print("sin(pi/2) =",sin(pi/2))`
2. `print("sin(pi/2) =",m.sin(m.pi/2))`
3. `print("sin(pi/2) =",math.sin(math.pi/2))`

Library calls:

1. `from math import sin,pi`
2. `import math`
3. `import math as m`
4. `from math import *`


{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>

1. Library calls 1 and 4. In order to directly refer to `sin` and `pi` without
the library name as prefix, you need to use the `from ... import ...`
statement. Whereas library call 1 specifically imports the two functions
`sin` and `pi`, library call 4 imports all functions in the `math` module.
2. Library call 3. Here `sin` and `pi` are referred to with a shortened library
name `m` instead of `math`. Library call 3 does exactly that using the
`import ... as ...` syntax - it creates an alias for `math` in the form of
the shortened name `m`.
3. Library call 2. Here `sin` and `pi` are referred to with the regular library
name `math`, so the regular `import ...` call suffices.

</details>

{::options parse_block_html="false" /}


## Importing Specific Items

1. Fill in the blanks so that the program below prints `90.0`.  
2. Do you find this version easier to read than preceding ones?  
3. Why *wouldn't* programmers always use this form of `import`?  

~~~python
____ math import ____, ____
angle = degrees(pi / 2)
print(angle)
~~~

{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>
 
~~~python
from math import degrees, pi
angle = degrees(pi / 2)
print(angle)
~~~
 
Most likely you find this version easier to read since it's less dense.
The main reason not to use this form of import is to avoid name clashes.
For instance, you wouldn't import `degrees` this way if you also wanted to
use the name `degrees` for a variable or function of your own. Or if you
were to also import a function named `degrees` from another library.

</details>

{::options parse_block_html="false" /}

## Reading Error Messages

1. Read the code below and try to identify what the errors are without running it.  
2. Run the code, and read the error message. What type of error is it?  

 ~~~python
 from math import log
 log(0)
 ~~~


{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>
 
1. The logarithm of `x` is only defined for `x  0`, so 0 is outside the
     domain of the function.
2. You get an error of type "ValueError", indicating that the function
     received an inappropriate argument value. The additional message
     "math domain error" makes it clearer what the problem is.

</details>

{::options parse_block_html="false" /}

[pypi]: https://pypi.python.org/pypi/
[stdlib]: https://docs.python.org/3/library/
[randommod]: https://docs.python.org/3/library/random.html








---

See [the notebook](https://nu-cem.github.io/CompPhys/2021/08/02/Libraries.html).

Back to [Python part two](https://nu-cem.github.io/CompPhys/2021/08/02/Python_basics_two.html).

---