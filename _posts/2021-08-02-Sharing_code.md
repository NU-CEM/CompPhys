---
toc: true
layout: post
categories: [documentation, testing]
title: Documentation and testing
sticky_rank: 9
hide: true
---

- Write short functions where possible as these are easier to test
- See https://coderefinery.github.io/testing/motivation/
- Documentation: README, API? https://pdoc3.github.io/pdoc/
- README: markdown incl. dropdown boxes
- README: pdoc: https://github.com/pdoc3/pdoc/issues/55
- cookiecutter?

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

Rather than running unit tests one-by-one we can use [pytest](http://pytest.org/) to automatically find and run all the tests within a project.

> pytest collects and runs all test functions starting with test_.

In the following steps we will make a simple Python function and use pytest to test it.


### TASKS

Extension:
