---
toc: false
layout: post
title: Programming good practice
sticky_rank: 1
hide: true
---

### Document your code

There are multiple ways you can document your code. Below are three examples:

1. Docstrings

Docstrings are the first statement in a module, function, class or method so programmers can understand what it does without having to read the details of the implementation.


Docstrings are string literals so must be contained within single quote marks (for single line docstrings) or triple quotes (for multiline docstrings). See the example below for a function-level docstring. 

```
 def calc_bulk_density(mass,volume):
     "Return dry bulk density = powder mass / powder volume."
     return mass / volume
```

Docstrings are preferred over in-line comments (see below) as the docstrings can be easily accessed using the Python `help()` function. It is also possible to generate online documentation automatically from docstrings.

2. In-line comments

```
# bulk density is the powder mass / powder volume
density = mass / volume 
```

3. Markdown in a Jupyter Notebook

For more extensive discussion you can combine code and text in a single document. 
See [this tutorial](https://lucydot.github.io/python_novice/01-run-quit/index.html) for more information about using Markdown in a Jupyter Notebook.

### Focus on readability

1. Consistency is key. Code formatting (for example, brackets) and use of whitespace should be consistent.
2. Use consistent whitespace:  

```
spam(ham[1], {eggs: 2})   
spam( ham[ 1 ], { eggs: 2} )
```

3. Use clear, meaningful variable names (don't just use `x`, `p` and expect the reader to know what they mean!)

The [Pep 8 Style Guide for Python code](https://www.python.org/dev/peps/pep-0008/) has further guidance.

### Avoid duplication

Duplication of code should be avoided where possible. 

1. If you will re-use a block of code multiple times consider encapsulating it in a function. See [this tutorial](https://lucydot.github.io/python_novice/08-writing-functions/index.html) for information about writing functions.

2. Use appropriate functions and data-types, including those from external libraries. For example, if you need to perform mathematical operations on an array of values, [use Numpy arrays](https://lucydot.github.io/python_novice/12-numpy-intro/index.html) instead of Python lists.

3. Use control structures appropriately. Only use `if`, `while` or `for` loops when necessary.

### Think about reproducibility

[Writing reproducible code is difficult](https://www.nature.com/articles/d41586-020-02462-7). In fact, there are many interesting initiatives designed to improve reproducibility in the computational scientists, such as [Reprohacks](https://www.reprohack.org/).

One straight-forward thing you can do is print the version number for each package you import using ```print(packagename.__version__)```
