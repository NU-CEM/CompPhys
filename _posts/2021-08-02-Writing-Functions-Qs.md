---
toc: false
layout: post
title: Writing functions - quick test
hide: true
---

> ## Identifying Syntax Errors
>
> 1. Read the code below and try to identify what the errors are
>    *without* running it.
> 2. Run the code and read the error message.
>    Is it a `SyntaxError` or an `IndentationError`?
> 3. Fix the error.
> 4. Repeat steps 2 and 3 until you have fixed all the errors.
>
> ~~~
> def another_function
>   print("Syntax errors are annoying.")
>    print("But at least python tells us about them!")
>   print("So they are usually not too hard to fix.")
> ~~~
> {: .python}
>
> > ## Solution
> >
> > ~~~
> > def another_function():
> >   print("Syntax errors are annoying.")
> >   print("But at least Python tells us about them!")
> >   print("So they are usually not too hard to fix.")
> > ~~~
> > {: .python}
> {: .solution}
{: .challenge}

> ## Definition and Use
>
> What does the following program print?
>
> ~~~
> def report(pressure):
>     print('pressure is', pressure)
>
> print('calling', report, 22.5)
> ~~~
> {: .python}
> > ## Solution
> >
> > ~~~
> > calling <function report at 0x7fd128ff1bf8> 22.5
> > ~~~ 
> > {: .output}
> >
> > A function call always needs parenthesis, otherwise you get memory address of the function object. So, if we wanted to call the function named report, and give it the value 22.5 to report on, we could have our function call as follows
> > ~~~
> > print("calling")
> > report(22.5)
> > ~~~
> {: .solution}
{: .challenge}


> ## Order of Operations
>
> The example above:
>
> ~~~
> result = print_date(1871, 3, 19)
> print('result of call is:', result)
> ~~~
> {: .python}
>
> printed:
> ~~~
> 1871/3/19
> result of call is: None
> ~~~
> {: .output}
>
> Explain why the two lines of output appeared in the order they did.
>
> What's wrong in this example?
> ~~~
> result = print_date(1871,3,19)
>
> def print_date(year, month, day):
>    joined = str(year) + '/' + str(month) + '/' + str(day)
>    print(joined)
> ~~~
> {: .python}
> 
> > ## Solution
> > 
> > 1. The first line of output (`1871/3/19`) is from the print function inside `print_date()`, while the second line
> > is from the print function below the function call. All of the code inside `print_date()` is executed first, and
> > the program then "leaves" the function and executes the rest of the code.   
> > 2. The problem with the example is that the function is defined *after* the call to the function is made. Python
> > therefore doesn't understand the function call.
> {: .solution}
{: .challenge}

> ## Find the First
>
> Fill in the blanks to create a function that takes a list of numbers as an argument
> and returns the first negative value in the list.
> What does your function do if the list is empty?
>
> ~~~
> def first_negative(values):
>     for v in ____:
>         if ____:
>             return ____
> ~~~
> {: .python}
> > ## Solution
> >
> > ~~~
> > def first_negative(values):
> >     for v in values:
> >         if v<0:
> >             return v
> > ~~~
> > {: .python}
> > If an empty list is passed to this function, it returns `None`:
> > ~~~
> > my_list = []
> > print(first_negative(my_list)
> > ~~~
> > {: .python}
> > ~~~
> > None
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}

> ## Calling by Name
>
> Earlier we saw this function:
>
> ~~~
> def print_date(year, month, day):
>     joined = str(year) + '/' + str(month) + '/' + str(day)
>     print(joined)
> ~~~
> We saw that we can call the function using *named arguments*, like this:
> ~~~
> print_date(day=1, month=2, year=2003)
> ~~~
> {: .python}
>
> 1.  What does `print_date(day=1, month=2, year=2003)` print?
> 2.  When and why is it useful to call functions this way?
>
> > ## Solution
> > 
> > 1. `2003/2/1`
> > 2. Using named arguments can make code more readable since one can see from the function call what name the different arguments 
> > have inside the function. It can also reduce the chances of passing arguments in the wrong order, since by using named arguments 
> > the order doesn't matter.
> {: .solution}
{: .challenge}

> ## Encapsulate of If/Print Block
>
> The code below will run on a label-printer for chicken eggs.  A digital scale will report a chicken egg mass (in grams) to the computer and then the computer will print a label.  
>
> Please re-write the code so that the if-block is folded into a function.
>
> ~~~
>  import random
>  for i in range(10):
>
>     # simulating the mass of a chicken egg
>     # the (random) mass will be 70 +/- 20 grams
>     mass=70+20.0*(2.0*random.random()-1.0)
>
>     print(mass)
>    
>     #egg sizing machinery prints a label
>     if(mass>=85):
>        print("jumbo")
>     elif(mass>=70):
>        print("large")
>     elif(mass<70 and mass>=55):
>        print("medium")
>     else:
>        print("small")
> ~~~
> {: .python}
>
>
> The simplified program  follows.  What function definition will make it functional?
>
> ~~~
>  # revised version
>  import random
>  for i in range(10):
>
>     # simulating the mass of a chicken egg
>     # the (random) mass will be 70 +/- 20 grams
>     mass=70+20.0*(2.0*random.random()-1.0)
>
>     print(mass,print_egg_label(mass))    
>
> ~~~
> {: .python}
>
>
> 1. Create a function definition for `print_egg_label()` that will work with the revised program above.  Note, the function's return value will be significant. Sample output might be `71.23 large`.
> 2.  A dirty egg might have a mass of more than 90 grams, and a spoiled or broken egg will probably have a mass that's less than 50 grams.  Modify your `print_egg_label()` function to account for these error conditions. Sample output could be `25 too light, probably spoiled`.
>
> > ## Solution
> >
> > ~~~
> > def print_egg_label(mass):
> >     #egg sizing machinery prints a label
> >     if(mass>=90):
> >         return("warning: egg might be dirty")
> >     elif(mass>=85):
> >         return("jumbo")
> >     elif(mass>=70):
> >         return("large")
> >     elif(mass<70 and mass>=55):
> >         return("medium")
> >     elif(mass<50):
> >         return("too light, probably spoiled")
> >     else:
> >         return("small")
> > ~~~
> > {: .python}
> {: .solution}
{: .challenge}

> ## Simulating a dynamical system
>
> In mathematics, a [dynamical system](https://en.wikipedia.org/wiki/Dynamical_system) is a system in which a function describes the time dependence of a point in a geometrical space.  A canonical example of a dynamical system is a system called the [logistic map](https://en.wikipedia.org/wiki/Logistic_map).
>
>
> 1. Define a function called `logistic_map` that takes two inputs: `x`, representing the state of the system at time _t_, and a parameter `r`. This function should return a value representing the state of the system at time _t+1_.
>
> 2. Using a `for` loop, iterate the `logistic_map` function defined in part 1 starting from an initial condition of 0.5 for `t_final=10`, `100`, and `1000` periods. Store the intermediate results in a list so that after the `for` loop terminates you have accumulated a sequence of values representing the state of the logistic map at time _t=0,1,...,t_final_.
>
> 3. Encapsulate the logic of your `for` loop into a function called `iterate` that takes the initial condition as its first input, the parameter `t_final` as its second input and the parameter `r` as its third input. The function should return the list of values representing the state of the logistic map at time _t=0,1,...,t_final_.
>
>
> > ## Solution
> >
> > 1.
> >
> > ~~~
> > def logistic_map(x, r):
> >     return r * x * (1 - x)
> > ~~~
> > {: .python}
> >
> > 2.
> >
> > ~~~
> > initial_condition = 0.5
> > t_final = 10
> > r = 1.0
> > trajectory = [initial_condition]
> > for t in range(1, t_final):
> >     trajectory[t] = logistic_map(trajectory[t-1], r)
> > ~~~
> > {: .python}
> >
> > 3.
> > ~~~
> > def iterate(initial_condition, t_final, r):
> >     trajectory = [initial_condition]
> >     for t in range(1, t_final):
> >         trajectory[t] = logistic_map(trajectory[t-1], r)
> >     return trajectorys
> > ~~~
> > {: .python}
> {: .solution}
{: .challenge}


{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>


</details>

{::options parse_block_html="false" /}





---

See [the notebook](https://nu-cem.github.io/CompPhys/2021/08/02/Writing-Functions.html).

Back to [Python part two](https://nu-cem.github.io/CompPhys/2021/08/02/Python_basics_two.html).

---