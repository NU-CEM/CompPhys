---
toc: false
layout: post
title: For loops - quick test
hide: true
---


## Classifying Errors

Is an indentation error a syntax error or a runtime error?


{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>

An IndentationError is a syntax error. Programs with syntax errors cannot be started.
A program with a runtime error will start but an error will be thrown under certain conditions.

</details>

{::options parse_block_html="false" /}

## Tracing Execution

Create a table showing the numbers of the lines that are executed when this program runs,
and the values of the variables after each line is executed.

~~~python
total = 0
for char in "tin":
   total = total + 1
~~~

{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>


| Line no | Variables            |
|---------|----------------------|
| 1       | total = 0            |
| 2       | total = 0 char = 't' |
| 3       | total = 1 char = 't' |
| 2       | total = 1 char = 'i' |
| 3       | total = 2 char = 'i' |
| 2       | total = 2 char = 'n' |
| 3       | total = 3 char = 'n' |

</details>

{::options parse_block_html="false" /}

## Reversing a String

Fill in the blanks in the program below so that it prints "nit"
(the reverse of the original character string "tin").

~~~python
original = "tin"
result = ____
for char in original:
   result = ____
print(result)
~~~


{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>

~~~
original = "tin"
result = ""
for char in original:
    result = char + result
print(result)
~~~

</details>

{::options parse_block_html="false" /}

## Practice Accumulating

Fill in the blanks in each of the programs below
to produce the indicated result.

~~~python
# Total length of the strings in the list: ["red", "green", "blue"] = 12
total = 0
for word in ["red", "green", "blue"]:
   ____ = ____ + len(word)
print(total)
~~~


{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>

~~~
total = 0
for word in ["red", "green", "blue"]:
    total = total + len(word)
print(total)
~~~

</details>

{::options parse_block_html="false" /}

~~~python
# List of word lengths: ["red", "green", "blue"] = [3, 5, 4]
lengths = ____
for word in ["red", "green", "blue"]:
   lengths.____(____)
print(lengths)
~~~


{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>

~~~
lengths = []
for word in ["red", "green", "blue"]:
    lengths.append(len(word))
print(lengths)
~~~

</details>

{::options parse_block_html="false" /}

~~~python
# Concatenate all words: ["red", "green", "blue"] = "redgreenblue"
words = ["red", "green", "blue"]
result = ____
for ____ in ____:
   ____
print(result)
~~~


{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>

~~~
words = ["red", "green", "blue"]
result = ""
for word in words:
    result = result + word
print(result)
~~~

</details>

{::options parse_block_html="false" /}


## Cumulative Sum

Reorder and properly indent the lines of code below
so that they print an array with the cumulative sum of data.
The result should be `[1, 3, 5, 10]`.

~~~python
cumulative += [sum]
for number in data:
cumulative = []
sum += number
sum = 0
print(cumulative)
data = [1,2,2,5]
~~~



{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>

~~~
sum = 0
data = [1,2,2,5]
cumulative = []
for number in data:
    sum += number
    cumulative.append(sum)
print(cumulative)
~~~

</details>

{::options parse_block_html="false" /}

## Identifying Variable Name Errors

1. Read the code below and try to identify what the errors are
  *without* running it.
2. Run the code and read the error message.
  What type of `NameError` do you think this is?
  Is it a string with no quotes, a misspelled variable, or a 
  variable that should have been defined but was not?
3. Fix the error.
4. Repeat steps 2 and 3, until you have fixed all the errors.

~~~python
for number in range(10):
   # use a if the number is a multiple of 3, otherwise use b
   if (Number % 3) == 0:
       message = message + a
   else:
       message = message + "b"
print(message)
~~~



{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>

~~~python
message = ""
for number in range(10):
    # use a if the number is a multiple of 3, otherwise use b
    if (number % 3) == 0:
        message = message + "a"
    else:
        message = message + "b"
print(message)
~~~

</details>

{::options parse_block_html="false" /}

## Identifying Item Errors

1. Read the code below and try to identify what the errors are
  *without* running it.
2. Run the code, and read the error message. What type of error is it?
3. Fix the error.

~~~python
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print('My favorite season is ', seasons[4])
~~~



{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>

~~~
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print('My favorite season is ', seasons[3])
~~~

</details>

{::options parse_block_html="false" /}


---

See [the notebook](https://nu-cem.github.io/CompPhys/2021/08/02/For-Loops.html).

Back to [Python part two](https://nu-cem.github.io/CompPhys/2021/08/02/Python_basics_two.html).

---