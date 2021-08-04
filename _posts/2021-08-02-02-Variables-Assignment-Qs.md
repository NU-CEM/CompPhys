---
toc: false
layout: post
title: Variables and assignment - quick test
hide: true
---

## Swapping Values

Fill the table showing the values of the variables in this program **after** each statement is executed.

| Command | Value of x   | Value of y   | Value of swap |
| ------- | ----------   | ----------   | ------------- |
|x = 1.0    |              |              |               |
|y = 3.0    |             |              |               |
|swap = x   |               |              |               |
|x = y      |                         |              |               |
|y = swap   |                       |              |               |

{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>

| Command | Value of x   | Value of y   | Value of swap |
| ------- | ----------   | ----------   | ------------- |
|x = 1.0  | 1.0          | not defined  | not defined   |
|y = 3.0  | 1.0          | 3.0          | not defined   |
|swap = x | 1.0          | 3.0          | 1.0           |
|x = y    | 3.0          | 3.0          | 1.0           |
|y = swap | 3.0          | 1.0          | 1.0           |

These three lines exchange the values in `x` and `y` using the `swap` variable for temporary storage. 
This is a fairly common programming idiom.   

</details>

{::options parse_block_html="false" /}

## Predicting Values

 What is the final value of `position` in the program below? (Try to predict the value without running the program,
then check your prediction.)

~~~python
initial = 'left'
position = initial
initial = 'right'
~~~

{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>

The final value of position is `'left'`.

The `initial` variable is assigned the value 'left'. In the second line, the `position` variable also receives the string value 'left'. In third line, the `initial` variable is given the value 'right', but the `position` variable retains its string value of 'left'.  
  
</details>

{::options parse_block_html="false" /}

## Choosing a Name

Which is a better variable name, `m`, `min`, or `minutes`?
Why?

Hint: think about which code you would rather inherit from someone who is leaving the lab:
~~~python
ts = m * 60 + s
tot_sec = min * 60 + sec
total_seconds = minutes * 60 + seconds
~~~

{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>
    
`minutes` is better because `min` might mean something like "minimum" (and actually does in Python, but we haven't seen that yet).
  
</details>

{::options parse_block_html="false" /}


---

See [the notebook](https://nu-cem.github.io/CompPhys/2021/08/02/02-Variables-Assignment.html).

Back to [Python part one](https://nu-cem.github.io/CompPhys/2021/08/02/Python_basics_one.html).

---

