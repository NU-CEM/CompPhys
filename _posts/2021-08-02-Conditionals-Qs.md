---
toc: false
layout: post
title: Conditionals - quick test
hide: true
---

## Tracing Execution

What does this program print?

~~~python
pressure = 71.9
if pressure  50.0:
   pressure = 25.0
elif pressure <= 50.0:
   pressure = 0.0
print(pressure)
~~~


{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>

~~~
25.0
~~~

</details>

{::options parse_block_html="false" /}

## Trimming Values

Fill in the blanks so that this program creates a new list
containing zeroes where the original list's values were negative
and ones where the original list's values were positive.

~~~python
original = [-1.5, 0.2, 0.4, 0.0, -1.3, 0.4]
result = ____
for value in original:
   if ____:
       result.append(0)
   else:
       ____
print(result)
~~~


~~~output
[0, 1, 1, 1, 0, 1]
~~~


{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>

~~~python
original = [-1.5, 0.2, 0.4, 0.0, -1.3, 0.4]
result = []
for value in original:
    if value<0.0:
        result.append(0)
    else:
        result.append(1)
print(result)
~~~

</details>

{::options parse_block_html="false" /}

## Initializing

Modify this program so that it finds the largest and smallest values in the list
no matter what the range of values originally is.

~~~python
values = [...some test data...]
smallest, largest = None, None
for v in values:
   if ____:
       smallest, largest = v, v
   ____:
       smallest = min(____, v)
       largest = max(____, v)
print(smallest, largest)
~~~

What are the advantages and disadvantages of using this method
to find the range of the data?


{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>

~~~python
values = [-2,1,65,78,-54,-24,100]
smallest, largest = None, None
for v in values:
    if smallest==None and largest==None:
        smallest, largest = v, v
    else:
        smallest = min(smallest, v)
        largest = max(largest, v)
print(smallest, largest)
~~~

</details>

{::options parse_block_html="false" /}


---

See [the notebook](https://nu-cem.github.io/CompPhys/2021/08/02/Conditionals.html).

Back to [Python part two](https://nu-cem.github.io/CompPhys/2021/08/02/Python_basics_two.html).

---