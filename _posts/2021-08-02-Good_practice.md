---
toc: false
layout: post
title: Programming good practice
sticky_rank: 1
hide: true
---

### Document your code

There are multiple ways you can document your code. Below are three examples:

#### Docstrings

Docstrings are the first statement in a module, function, class or method so programmers can understand what it does without having to read the details of the implementation.


Docstrings are string literals so must be contained within single quote marks (for single line docstrings) or triple quotes (for multiline docstrings). See the example below for a function-level docstring. 

```
 def calc_bulk_density(mass,volume):
     "Return dry bulk density = powder mass / powder volume."
     return mass / volume
```

Docstrings are preferred over in-line comments (see below) as the docstrings can be easily accessed using the Python `help()` function. It is also possible to generate online documentation automatically from docstrings.

#### In-line comments

```
# bulk density is the powder mass / powder volume
density = mass / volume 
```

#### Markdown in a Jupyter Notebook

For more extensive discussion you can combine code and text in a single document. 
See [this tutorial](https://lucydot.github.io/python_novice/01-run-quit/index.html) for more information about using Markdown in a Jupyter Notebook.

### Focus on readability

Your code should be easily readable by others. This is a big topic! The [Pep 8 Style Guide for Python code](https://www.python.org/dev/peps/pep-0008/) has further guidance, although it is a daunting document. The most important thing is that you are consistent within your own code.

#### Consistency is key

Code formatting (for example, brackets) and use of whitespace should be consistent. For example, do not mix-and-match whitespace as in the code below:

```
spam(ham[1], {eggs: 2})   
spam( ham[ 1 ], { eggs: 2} )
```

#### Variable and function names

Use clear, meaningful variable and function names (don't just use `x`, `p` and expect the reader to know what they mean!)

### Avoid duplication 

Duplication of code should be avoided where possible. There are several ways this can be achieved.

#### Use functions
If you will re-use a block of code multiple times consider encapsulating it in a function. See [this tutorial](https://lucydot.github.io/python_novice/08-writing-functions/index.html) for information about writing functions.

#### Use external libraries
Use appropriate functions and data-types, including those from external libraries. For example, if you need to perform mathematical operations on an array of values, [use Numpy arrays](https://lucydot.github.io/python_novice/12-numpy-intro/index.html) instead of Python lists.

#### Use control structures when appropriate
Use control structures appropriately. Only use `if`, `while` or `for` loops when necessary.

### Think about reproducibility

[Writing reproducible code is difficult](https://www.nature.com/articles/d41586-020-02462-7). In fact, there are many interesting initiatives designed to improve reproducibility in the computational scientists, such as [Reprohacks](https://www.reprohack.org/).

One straight-forward thing you can do is print the version number for each package you import using ```print(packagename.__version__)```
