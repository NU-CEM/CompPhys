---
toc: false
layout: post
title: Variable scope - quick test
hide: true
---

## Local and Global Variable Use

Trace the values of all variables in this program as it is executed.
(Use '---' as the value of variables before and after they exist.)

~~~python
limit = 100

def clip(value):
     return min(max(0.0, value), limit)

value = -22.5
print(clip(value))
~~~


## Reading Error Messages

Read the traceback below, and identify the following:

1. How many levels does the traceback have?
2. What is the file name where the error occurred?
3. What is the function name where the error occurred?
4. On which line number in this function did the error occurr?
5. What is the type of error?
6. What is the error message?

~~~output
 ---------------------------------------------------------------------------
 KeyError                                  Traceback (most recent call last)
 <ipython-input-2-e4c4cbafeeb5> in <module>()
       1 import errors_02
 ----> 2 errors_02.print_friday_message()

 /Users/ghopper/thesis/code/errors_02.py in print_friday_message()
      13
      14 def print_friday_message():
 ---> 15     print_message("Friday")

 /Users/ghopper/thesis/code/errors_02.py in print_message(day)
       9         "sunday": "Aw, the weekend is almost over."
      10     }
 ---> 11     print(messages[day])
      12
      13

 KeyError: 'Friday'
 ~~~


{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>


1. Three levels.
2. `errors_02.py`
3. `print_message`
4. Line 11
5. KeyError. These errors occur when we are trying to look up a key that does not exist (usually in a data structure such as a dictionary). We can find more information about the KeyError and other built-in exceptions in the Python docs.
6. `KeyError: 'Friday'`

</details>

{::options parse_block_html="false" /}

---

See [the notebook](https://nu-cem.github.io/CompPhys/2021/08/02/Variable-Scope.html).

Back to [Python part two](https://nu-cem.github.io/CompPhys/2021/08/02/Python_basics_two.html).

---