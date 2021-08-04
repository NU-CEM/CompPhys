---
toc: false
layout: post
title: Lists - quick test
hide: true
---


## Fill in the Blanks

Fill in the blanks so that the program below produces the output shown.

~~~python
values = ____
values.____(1)
values.____(3)
values.____(5)
print('first time:', values)
values = values[____]
print('second time:', values)
~~~
{: .python}

~~~output
first time: [1, 3, 5]
second time: [3, 5]
~~~
{: .output}


{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>
  
~~~python
values = []
values.append(1)
values.append(3)
values.append(5)
print('first time:', values)
values = values[1:]
print('second time:', values)
~~~
   
</details>

{::options parse_block_html="false" /}

## How Large is a Slice?

If 'low' and 'high' are both non-negative integers,
how long is the list `values[low:high]`?


{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>
  
The list `values[low:high]` has `high - low` elements.  For example,
`values[1:4]` has the 3 elements `values[1]`, `values[2]`, and `values[3]`.
Note that the expression will only work if `high` is less than the total
length of the list `values`.
   
</details>

{::options parse_block_html="false" /}

## From Strings to Lists and Back

Given this:

~~~python
print('string to list:', list('tin'))
print('list to string:', ''.join(['g', 'o', 'l', 'd']))
~~~

~~~output
['t', 'i', 'n']
'gold'
~~~


1.  Explain in simple terms what `list('some string')` does.
2.  What does `'-'.join(['x', 'y'])` generate?


{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>
  
1. `list('some string')` "splits" a string into a list of its characters.
2. `x-y`
   
</details>

{::options parse_block_html="false" /}

## Working With the End

What does the following program print?

~~~python
element = 'helium'
print(element[-1])
~~~

1.  How does Python interpret a negative index?
2.  If a list or string has N elements,
     what is the most negative index that can safely be used with it,
     and what location does that index represent?
3.  If `values` is a list, what does `del values[-1]` do?
4.  How can you display all elements but the last one without changing `values`?
     (Hint: you will need to combine slicing and negative indexing.)


{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>
  
The program prints `m`.
1. Python interprets a negative index as starting from the end (as opposed to
    starting from the beginning).  The last element is `-1`.
2. The last index that can safely be used with a list of N elements is element
   `-N`, which represents the first element.
3. `del values[-1]` removes the last element from the list.
4. `values[:-1]`
   
</details>

{::options parse_block_html="false" /}

## Stepping Through a List

What does the following program print?

~~~python
element = 'fluorine'
print(element[::2])
print(element[::-1])
~~~


1.  If we write a slice as `low:high:stride`, what does `stride` do?
2.  What expression would select all of the even-numbered items from a collection?


{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>
  
The program prints
  
~~~output
furn
eniroulf
~~~

1. `stride` is the step size of the slice
2. The slice `1::2` selects all even-numbered items from a collection: it starts
   with element `1` (which is the second element, since indexing starts at `0`),
   goes on until the end (since no `end` is given), and uses a step size of `2`
   (i.e., selects every second element).
   
</details>

{::options parse_block_html="false" /}

## Copying (or Not)

What do these two programs print?
In simple terms, explain the difference between `new = old` and `new = old[:]`.

~~~python
# Program A
old = list('gold')
new = old      # simple assignment
new[0] = 'D'
print('new is', new, 'and old is', old)
~~~

~~~python
# Program B
old = list('gold')
new = old[:]   # assigning a slice
new[0] = 'D'
print('new is', new, 'and old is', old)
~~~


{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>
  
Program A prints
  
~~~output
> > new is ['D', 'o', 'l', 'd'] and old is ['D', 'o', 'l', 'd']
~~~

Program B prints
  
~~~output
> > new is ['D', 'o', 'l', 'd'] and old is ['g', 'o', 'l', 'd']
~~~

`new = old` makes `new` a reference to the list `old`; `new` and `old` point
towards the same object.
 
`new = old[:]` however creates a new list object `new` containing all elements
from the list `old`; `new` and `old` are different objects.
   
</details>

{::options parse_block_html="false" /}

---

See [the notebook](https://nu-cem.github.io/CompPhys/2021/08/02/Lists.html).

Back to [Python basics - part one](https://nu-cem.github.io/CompPhys/2021/08/02/Python_basics_one.html).

---
