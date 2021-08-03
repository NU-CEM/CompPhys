---
toc: false
layout: post
title: Running python - quick test
hide: true
---

## Creating Lists in Markdown

Create a nested list in a Markdown cell in a notebook that looks like this:

1.  Get funding.
2.  Do work.
    *   Design experiment.
    *   Collect data.
    *   Analyze.
3.  Write up.
4.  Publish.

{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>

Note that the bullet list is indented 2 spaces so that it is inline with the items of the numbered list.
~~~
1.  Get funding.
2.  Do work.
    *   Design experiment.
    *   Collect data.
    *   Analyze.
3.  Write up.
4.  Publish.
~~~
   
</details>

{::options parse_block_html="false" /}

## Multiple Maths

What is displayed when a Python cell in a notebook
that contains several calculations is executed?
For example, what happens when this cell is executed?

~~~python
7 * 3
2 + 1
~~~


{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>

Python returns the output of the last calculation. The output is:
~~~python
3
~~~
   
</details>

{::options parse_block_html="false" /}

## Equations

Standard Markdown (such as we're using for these notes) won't render equations, but the Notebook will.
Create a new Markdown cell and enter the following:

~~~
$\sum_{i=1}^{N} 2^{-i} \approx 1$
~~~

(It's probably easier to copy and paste.) What does it display? What do you think the underscore, `_`, circumflex, `^`, and dollar sign, `$`, do?

{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>

The notebook shows the equation as it would be rendered from [LaTeX]() equation syntax.

- The dollar sign, `$`, is used to tell markdown that the text in between is a latex equation.
- underscore, `_`, is used for subscripts
- circumflex, `^`, is used for superscripts.
- A pair of curly braces, `{` and `}`, is used to group text together so that the statement `i=1` becomes the the subscript and `N` becomes the superscript.
- Similarly, `-i` is in curly braces to make the whole statement the superscript for `2`.
- `\sum` and `\approx` are latex commands for "sum over" and "approximate" symbols. 
   
</details>

{::options parse_block_html="false" /}

---

See [the notebook](https://nu-cem.github.io/CompPhys/2021/08/02/01-Running_python.html).

Back to [Python basics - part one](https://nu-cem.github.io/CompPhys/2021/08/02/Python_basics_one.html).

---
