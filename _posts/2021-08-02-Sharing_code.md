---
toc: fals
layout: post
categories: [documentation, testing]
title: Documentation and testing
sticky_rank: 9
hide: true
---




In the course so far you have learnt the building blocks of Python. With this you can write a surprising amount of useful code! However our efforts are rewarded many times over if we can share the code we have written. Sharing your code:
- clearly demonstrates your programming skills to future employers and/or supervisors
- enables other researchers to use your code, progressing science forwards
- establishes you an active participant in a particular domain or community of practice (people *know who you are*)

However it is unfortunately not enough to stick our Python scripts / modules online and hope that other people will use them. We need to use tests to demonstrate that our software is reliable, and we need to write documentation so that others understand how best to use the code. These two topics - testing and documentation - are the focus of this lesson.

Please note that the following text has been closeley adapted, with permission, from the [Code Refinery software testing lesson](https://coderefinery.github.io/testing/motivation/).

### Untested software can be compared to uncalibrated detectors

> “Before relying on a new experimental device, an experimental scientist always establishes its accuracy. A new detector is calibrated when the scientist observes > its responses to known input signals. The results of this calibration are compared against the expected response.”   

[From [Testing and Continuous Integration with Python](https://carpentries-incubator.github.io/python-testing/), created by K. Huff]

Simulations and analysis using software should be held to the same standards as experimental measurement devices!

Further motivation for testing:
- [A Scientist’s Nightmare: Software Problem Leads to Five Retractions](https://science.sciencemag.org/content/314/5807/1856.summary)
- [Researchers find bug in Python script may have affected hundreds of studies](https://arstechnica.com/information-technology/2019/10/chemists-discover-cross-platform-python-scripts-not-so-cross-platform/)

### Testing helps to detect errors before they cause problems

In software tests, expected results are compared with observed results in order to establish accuracy:
- As projects grow, it becomes easier to break things without noticing immediately
- Software defects can be caused by both human errors and non-controllable events (i.e. environmental conditions)
- Testing is essential for research software because we care about reproducibility of scientific results

Testing also encourages others to use your code:
- It provides a way for users to see if the code is installed correctly
- It allows users to better judge the quality of the code

Finally, testing encourages other developers to contribute to your code as it is easier for external developers to contribute to the project without breaking your code (or at least it is clear when they have broken the code!)

However bear in mind that tested code does not mean the code is *perfect*; “Program testing can be used to show the presence of bugs, but never to show their absence!” (Edsger W. Dijkstra)

**Discussion question:** Can you think of examples where it is *not* necessary to share your code?

{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>

Some examples where you may choose not to test your code:
- A Jupyter notebook which produces a plot and you know by looking at the plot whether it worked
- A short, 'obviously correct' Python script which you never intend to reuse
    
</details>

{::options parse_block_html="false" /}    

### Use assertions for things you believe will/should never happen.

~~~python
def kelvin_to_celsius(temp_k):
    """
    Converts temperature in Kelvin
    to Celsius.
    """
    assert temp_k >= 0.0, "ERROR: negative T_K"
    temp_c = temp_k - 273.15
    return temp_c
~~~

### Units testing is for small components (units) of a code

~~~python
def fahrenheit_to_celsius(temp_f):
    """Converts temperature in Fahrenheit
    to Celsius.
    """
    temp_c = (temp_f - 32.0) * (5.0/9.0)
    return temp_c

# This is the test function: `assert` raises an error if something
# is wrong.
def test_fahrenheit_to_celsius():
    temp_c = fahrenheit_to_celsius(temp_f=100.0)
    expected_result = 37.777777
    assert abs(temp_c - expected_result) < 1.0e-6
~~~

- Unit tests are functions
- Unit testing is used to test one unit: for example, a single function

**Question:** In the example above we want to check if the calculated `temp_c` is equal to the `expected_result`. Why do we use the assert statement `abs(temp_c - expected_result) < 1.0e-6` instead of the simpler assert statement `temp_c == expected_result`?

{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>

Due to the inherent limitations to computational accuracy, we should not test for the exact equality between two floats. Instead we check that they are the same to within a numerical tolerance (in this case 1.0e-6). For more details please see the lesson [Evaluating numerical errors and accuracy](https://nu-cem.github.io/CompPhys/2021/08/02/Evaluating-Accuracy).
    
</details>

{::options parse_block_html="false" /}    

Another commonly used type of testing is called **end-to-end**. End-to-end tests check if the software is working as a whole, from beginning to end. For example, you input example data at the start of a simulation and then check that the end results of the simulation are correct.

### Pytest can be used to implement a Python test suite

Rather than running unit tests one-by-one we can use [pytest](http://pytest.org/) to automatically find and run all the tests within a project; pytest collects and runs all test functions starting with test_.

In the following steps we will make a simple Python function and use pytest to test it.

1. Create a new directory and change into it:

~~~bash
mkdir pytest-example
cd pytest-example
~~~

2. Then create a file called example.py and copy-paste the following code into it:

~~~python
def add(a, b):
    return a + b


def test_add():
    assert add(2, 3) == 5
    assert add('space', 'ship') == 'spaceship'
~~~

This code contains one genuine function and a test function. pytest finds any functions beginning with test_ and treats them as tests.

3. Let us try to test it with pytest:

~~~bash
pytest -v example.py
~~~

~~~output
============================================================ test session starts =================================
platform linux -- Python 3.7.2, pytest-4.3.1, py-1.8.0, pluggy-0.9.0 -- /home/user/pytest-example/venv/bin/python3
cachedir: .pytest_cache
rootdir: /home/user/pytest-example, inifile:
collected 1 item

example.py::test_add PASSED

========================================================= 1 passed in 0.01 seconds ===============================
~~~

Yay! The test passed!

4. Let us break the test! Introduce a code change which breaks the code and check whether pytest detects the change:

~~~bash
pytest -v example.py
~~~

~~~output
============================================================ test session starts =================================
platform linux -- Python 3.7.2, pytest-4.3.1, py-1.8.0, pluggy-0.9.0 -- /home/user/pytest-example/venv/bin/python3
cachedir: .pytest_cache
rootdir: /home/user/pytest-example, inifile:
collected 1 item

example.py::test_add FAILED

================================================================= FAILURES =======================================
_________________________________________________________________ test_add _______________________________________

    def test_add():
>       assert add(2, 3) == 5
E       assert -1 == 5
E         --1
E         +5

example.py:6: AssertionError
========================================================= 1 failed in 0.05 seconds ==============
~~~

Notice how pytest is smart and includes context: lines that failed, values of the relevant variables.

**Question:** In the example above we have compared integers. In this optional exercise we want to learn how to compare floating point numbers since they are more tricky.

The following test will fail and this might be surprising. Try it out:

~~~python
def add(a, b):
    return a + b


def test_add():
    assert add(0.1, 0.2) == 0.3
~~~

Your goal: find a more robust way to test this addition.

{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>
  
One solution is to use `pytest.approx`:

~~~python
from pytest import approx

def add(a, b):
    return a + b

def test_add():
    assert add(0.1, 0.2) == approx(0.3)
~~~
  
But maybe you didn’t know about pytest.approx: and did this instead:

~~~python
def test_add():
    result = add(0.1, 0.2)
    assert abs(result - 0.3) < 1.0e-7
~~~
                                     
This is OK but the 1.0e-7 can be a bit arbitrary.

</details>

{::options parse_block_html="false" /}  
  
### README.md

> There is nothing in the programming field more despicable than an undocumented program. 
  — Ed Yourdon, Software Engineering pioneer
  
### Docstrings


### TASKS
  
1. Write and run a unit test for the `Lorenz()` function in the `Lorenz.py` script you developed in [a previous lesson](https://nu-cem.github.io/CompPhys/2021/08/02/Scripting.html)
  
2. Write a docstring for the `Lorenz()` function in the `Lorenz.py` script. Follow the [Google docstring format](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#383-functions-and-methods) as in the example above.
  
3. Push your changes (if done locally) to the remote Github repository you created in the [previous lesson](https://nu-cem.github.io/CompPhys/2021/08/02/Version_control.html).

### EXTENSION TASKS: Automate everything!** 
  
4.  Automated testing using a tool such as [Travis Continuous Integration](https://travis-ci.org/) allows us to automatically run tests when there is a commit to a Github repository. Following the tutorial from [The Code Refinery](https://coderefinery.github.io/testing/continuous-integration/), implement continuous integration for a Github repository holding `Lorenz.py` (this could be the Github repository you created in the [previous lesson](https://nu-cem.github.io/CompPhys/2021/08/02/Version_control.html)). Note that you will have to adapt the workflow file so that pip installs the python packages imported in your script (for Lorenz.py the packages are numpy and matplotlib).

5. API (Application Programming Interface) documentation can be automatically generated using a tool such as [pdoc3](https://pdoc3.github.io/pdoc/). These tools read in all of the docstrings within a Python package and generate a webpage accordingly. For example, see the API documentation for the [effmass project](https://effmass.readthedocs.io/en/latest/inputs.html). Automatic API documentation is a real gamechanger; as long as we write docstrings alongside our code, we can quickly generate new documentation. If our code and docstrings change, the documentation will also stay up to date (as long as you remember to re-generate the webpage, or ask Github to do this for you with Github actions). Following the documentation on [pdoc3](https://pdoc3.github.io/pdoc/) generate a html page with the API documentation for Lorenz.py. In the next lesson you will learn how to host this page using Github Pages.
