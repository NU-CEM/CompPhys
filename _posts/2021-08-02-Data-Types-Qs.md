---
toc: false
layout: post
title: Data types and type conversion - quick test
hide: true
---



## Slicing 

If you assign `a = 123`,
what happens if you try to get the second digit of `a` via `a[1]`?

{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>
  
Numbers are not stored in the written representation,
so they can't be treated like strings.

~~~python
a = 123
print(a[1])
~~~

~~~output
TypeError: 'int' object is not subscriptable
~~~
  
</details>

{::options parse_block_html="false" /}

## More slicing

What does the following program print?

~~~python
atom_name = 'carbon'
print('atom_name[1:3] is:', atom_name[1:3])
~~~

{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>

~~~output
atom_name[1:3] is: ar
~~~
  
</details>

{::options parse_block_html="false" /}

## Even more slicing

Open a Notebook to help answer the following questions:

1.  What does `thing[low:]` (without a value after the colon) do?
2.  What does `thing[:high]` (without a value before the colon) do?
3.  What does `thing[:]` (just a colon) do?
4.  What does `thing[-2]` do?

{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>
  
1. Slices from `low` to the end (inclusive)
2. Slices from the start to `high` (exclusive)
3. Slices from the start to the end
4. Selects the second last element
  
</details>

{::options parse_block_html="false" /}

## Decimals

What type of value is 3.4?
How can you find out?

{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>

It is a floating-point number (often abbreviated "float").

~~~python
print(type(3.4))
~~~

~~~output
<class 'float'>
~~~
  
</details>

{::options parse_block_html="false" /}


## Choose a Type

  What type of value (integer, floating point number, or character string)
would you use to represent each of the following?  
  
1. Number of days since the start of the year.
2. Time elapsed from the start of the year until now in days.
3. Serial number of a piece of lab equipment.
4. A lab specimen's age
5. Current population of a city.
6. Average population of a city over time.

{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>

The answers to the questions are:
1. Integer, since the number of days would lie between 1 and 365. 
2. Floating point, since fractional days are required
3. Character string if serial number contains letters and numbers, otherwise integer if the serial number consists only of numerals
4. This will vary! How do you define a specimen's age? whole days since collection (integer)? date and time (string)?
5. Choose floating point to represent population as large aggreates (eg millions), or integer to represent population in units of individuals.
6. Floating point number, since an average is likely to have a fractional part.

</details>

{::options parse_block_html="false" /}

## Division Types

In Python 3, the `//` operator performs integer (whole-number) floor division, the `/` operator performs floating-point
division, and the '%' (or *modulo*) operator calculates and returns the remainder from integer division:

~~~python
print('5 // 3:', 5//3)
print('5 / 3:', 5/3)
print('5 % 3:', 5%3)
~~~

~~~output
5 // 3: 1
5 / 3: 1.6666666666666667
5 % 3: 2
~~~
{: .output}

However in Python 2 (and other languages), the `/` operator between two integer types perform a floor (`//`) division. To perform a float division, we have to convert one of the integers to float.

~~~python
print('5 // 3:', 1)
print('5 / 3:', 1 )
print('5 / float(3):', 1.6666667 )
print('float(5) / 3:', 1.6666667 )
print('float(5 / 3):', 1.0 )
print('5 % 3:', 2)
~~~

If `num_subjects` is the number of subjects taking part in a study,
and `num_per_survey` is the number that can take part in a single survey,
write an expression that calculates the number of surveys needed
to reach everyone once.

{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>
  
We want the minimum number of surveys that reaches everyone once, which is
the rounded up value of `num_subjects / num_per_survey`. This is 
equivalent to performing an integer division with `//` and adding 1.
  
~~~python
num_subjects = 600
num_per_survey = 42
num_surveys = num_subjects // num_per_survey + 1

print(num_subjects, 'subjects,', num_per_survey, 'per survey:', num_surveys)
~~~

~~~outpu
600 subjects, 42 per survey: 15
~~~

  
</details>

{::options parse_block_html="false" /}


## Arithmetic with Different Types

Which of the following will print 2.0?
Note: there may be more than one right answer.

~~~pythhon
first = 1.0
second = "1"
third = "1.1"
~~~

1. `first + float(second)`
2. `float(second) + float(third)`
3. `first + int(third)`
4. `first + int(float(third))`
5. `int(first) + int(float(third))`
6. `2.0 * second`

{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>

Answer: 1 and 4

</details>

{::options parse_block_html="false" /}

## Complex Numbers

Python provides complex numbers,
which are written as `1.0+2.0j`.
If `val` is an imaginary number,
its real and imaginary parts can be accessed using *dot notation*
as `val.real` and `val.imag`.

1.  Why do you think Python uses `j` instead of `i` for the imaginary part?
2.  What do you expect `1+2j + 3` to produce?
3.  What do you expect '4j' to be?  What about `4 j` or `4 + j'? > 

  
{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>

1. Standard mathematics treatments typically use `i` to denote an imaginary number. However, from media reports it
was an early convention established from electrical engineering that now presents a technically expensive area to
change. [Stack Overflow provides additional explanation and
discussion](http://stackoverflow.com/questions/24812444/why-are-complex-numbers-in-python-denoted-with-j-instead-of-i)
2. 4+2j
3. 4j, syntax error, depends on the value of j

  
</details>

{::options parse_block_html="false" /}
  
---

See [the notebook](https://nu-cem.github.io/CompPhys/2021/08/02/Data-Types.html).

Back to [Python basics - part one](https://nu-cem.github.io/CompPhys/2021/08/02/Python_basics_one.html).

---
