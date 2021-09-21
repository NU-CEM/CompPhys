---
toc: false
layout: post
title: Programming good practice
sticky_rank: 1
hide: true
---

**Document your code**

There are multiple ways you can document your code. In this course we will use three different methods:

1. Docstrings

```
 def calc_bulk_density(mass,volume):
     "Return dry bulk density = powder mass / powder volume."
     return mass / volume
```
Docstrings are the first statement in a module, function, class or method.

2. In-line comments

```
# bulk density is the powder mass / powder volume
density = mass / volume 
```

3. Markdown in a Jupyter Notebook

**Focus on readability**

1. consistency is key
2. Use consisten whitespace:  
	 `spam(ham[1], {eggs: 2})`   
	 `spam( ham[ 1 ], { eggs: 2} )`
3. Use clear, meaningful variable names (don't just use `x`, `p` and expect the reader to know what they mean!)

The [Pep 8 Style Guide for Python code](https://www.python.org/dev/peps/pep-0008/) has further guidance.

**Think about reproducibility**

[Writing reproducible code is difficult](https://www.nature.com/articles/d41586-020-02462-7). In fact, there are many interesting initiatives designed to improve reproducibility in the computational scientists, such as [Reprohacks](https://reprohacks.eu.pythonanywhere.com/about).

One straight-forward thing you can do is print the version number for each package you import using ```print(packagename.__version__)```
