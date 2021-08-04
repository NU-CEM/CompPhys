---
toc: false
layout: post
title: Built-in functions, help and errors - quick test
hide: true
---

## What Happens When

1. Explain in simple terms the order of operations in the following program:
    when does the addition happen, when does the subtraction happen,
    when is each function called, etc.
2. What is the final value of `radiance`?

~~~python
radiance = 1.0
radiance = max(2.1, 2.0 + min(radiance, 1.1 * radiance - 0.5))
~~~



{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>
  

1. 1. `1.1 * radiance = 1.1`
   2. `1.1 - 0.5 = 0.6`
   3. `min(randiance, 0.6) = 0.6`
   4. `2.0 + 0.6 = 2.6`
   5. `max(2.1, 2.6) = 2.6`

2. At the end, `radiance = 2.6`

</details>

{::options parse_block_html="false" /}


## Spot the Difference

1. Predict what each of the `print` statements in the program below will print.
2. Does `max(len(rich), poor)` run or produce an error message?
    If it runs, does its result make any sense?

~~~python
easy_string = "abc"
print(max(easy_string))
rich = "gold"
poor = "tin"
print(max(rich, poor))
print(max(len(rich), len(poor)))
~~~


  
{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>
  
1. `c`
2. `tin`
3. `4`
  
2. It throws a TypeError. The command is trying to run `max(4, 'tin')` and you can't compare
a string and an integer

</details>

{::options parse_block_html="false" /}


## Why Not?

Why don't `max` and `min` return `None` when they are given no arguments?


  
{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>
  
`max` and `min` return TypeErrors in this case because the correct number of parameters
was not supplied. If it just returned `None`, the error would be much harder to trace as it
would likely be stored into a variable and used later in the program, which could lead to unintended behaviour.

</details>

{::options parse_block_html="false" /}


---

See [the notebook](https://nu-cem.github.io/CompPhys/2021/08/02/Functions.html).

Back to [Python basics - part one](https://nu-cem.github.io/CompPhys/2021/08/02/Python_basics_one.html).

---
