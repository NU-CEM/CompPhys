---
toc: false
layout: post
title: Analysing data - quick test
hide: true
---

## Encapsulation

Fill in the blanks to create a function that takes a single filename, containing comma separated values, as an argument,
loads the data in the file named by the argument,
and returns the minimum value in that data.

~~~python
import numpy

def min_in_data(____):
 data = ____
 return ____
~~~


{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>

~~~python
import numpy

def min_in_data(filename):
  data = numpy.loadtxt(fname=filename, delimiter=',')
  return data.min()
~~~

</details>

{::options parse_block_html="false" /}

## Stacking Arrays

Arrays can be concatenated and stacked on top of one another,
using NumPy's `vstack` and `hstack` functions for vertical and horizontal stacking, respectively.

~~~python
import numpy

A = numpy.array([[1,2,3], [4,5,6], [7, 8, 9]])
print('A = ')
print(A)

B = numpy.hstack([A, A])
print('B = ')
print(B)

C = numpy.vstack([A, A])
print('C = ')
print(C)
~~~


~~~output
A =
[[1 2 3]
[4 5 6]
[7 8 9]]
B =
[[1 2 3 1 2 3]
[4 5 6 4 5 6]
[7 8 9 7 8 9]]
C =
[[1 2 3]
[4 5 6]
[7 8 9]
[1 2 3]
[4 5 6]
[7 8 9]]
~~~

Write some additional code that slices the first and last columns of `A`,
and stacks them into a 3x2 array.
Make sure to `print` the results to verify your solution.


{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>

A 'gotcha' with array indexing is that singleton dimensions
are dropped by default. That means `A[:, 0]` is a one dimensional
array, which won't stack as desired. To preserve singleton dimensions,
the index itself can be a slice or array. For example, `A[:, :1]` returns
a two dimensional array with one singleton dimension (i.e. a column
vector).

~~~python
D = numpy.hstack((A[:, :1], A[:, -1:]))
print('D = ')
print(D)
~~~

~~~output
D =
[[1 3]
[4 6]
[7 9]]
~~~


An alternative way to achieve the same result is to use Numpy's
delete function to remove the second column of A.

~~~python
D = numpy.delete(A, 1, 1)
print('D = ')
print(D)
~~~


~~~output
D =
[[1 3]
[4 6]
[7 9]]
~~~

</details>

{::options parse_block_html="false" /}

---

See [the notebook](https://nu-cem.github.io/CompPhys/2021/08/02/Analysing-Data.html).

Back to [Data analysis and visualisation](https://nu-cem.github.io/CompPhys/2021/08/02/Data_analysis.html).

---
