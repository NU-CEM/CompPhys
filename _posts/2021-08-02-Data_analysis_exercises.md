---
toc: false
layout: post
title: Data analysis and visualisation - exercises
hide: true
---

# Error bars 

In [Python part two] you wrote a function to calculate the perimeter of a triangle and the associated standard error.

a) Use this function to plot the perimeter of an equilateral triangle as a function of side length. Use the following side lengths: 3.1cm, 6.7cm, 9.2cm, 12.4cm and assume you use. Think carefully about the type of plot: should it be a scatter plot or line plot?

b) Re-plot this data with attached error bars using the [`matplotlib.pyplot.errorbar` function](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.errorbar.html)

# Calculating Planck's constant

*Adapted from Mark Newman's book "Computational Physics, p. 124*

When light is shone on the surface of a metal, the photons in the light can excite (transfer energy to) electrons in the metal and, sometimes, eject them from the surface into the free space above. The energy of the ejected electron can be calculated by measuring the minimum voltage $V$ that stops the electron moving.

We know that the energy of an ejected electron is equal to the energy of the photon that excited it minus the workfunction $\phi$ (which is the energy needed to remove it from the surface) and that the energy of a single photon is $hf$ where $h$ is Planck's constant and $f$ is the frequency of light. Mathematically this can be expressed as:

$$eV = hf - \phi$$,

where $e$ is the charge of the electron.

a) Read in the photoelectric measurement data from the file [Planck.txt](https://nu-cem.github.io/CompPhys/data/Planck.txt). The first column contains frequencies $f$ is hertz and the second column contains voltages $V$. Use this data to plot $V$ vs $f$. Think about the plot type - does a scatter plot of line plot make most sense?

The least-squares method is very commonly used for fitting a polynomial to a set of data. As it is so prevalent in physics and engineering, you are encouraged to watch [this video](https://www.youtube.com/watch?v=YwZYSTQs-Hk) which give an intuitive and mathematical description of the method. 

b) Fit a straight line (polynomial of degree one) to the data using the least-squares method implemented in [`numpy.polyfit`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html). Overlay this line on your data points. 

c) Using the gradient of the fitted line calculate a value for Planck's constant. Compare this to values you can find online.

# Line fitting

In the code below we calculate the velocity of a ball between times 0 and 10 and store it as a numpy array

~~~python
import numpy

g = 9.81
velocity_list = numpy.zeros(50)
v_0 = 0
 
for index,time in enumerate(numpy.linspace(0,10,50)):
  velocity_list[index] = v_0 + g*time
~~~

We can fit a polynomial to this data using the `numpy.polyfit` function. In this case, we know from looking at the equation that is is a first order polynomial (straight line).

~~~python
fit = numpy.polyfit(numpy.linspace(0,10,50), velocity_list, 1)
print(fit)
~~~

What is the gradient and intercept of the straight line fit? Does this make physical sense? 
Make a scatter plot of velocity vs time. Label the x-axis and y-axis (with units) and give the plot a title.

{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>

The gradient is equal to the acceleration of the ball which is given by the gravitational constant $g$. The intercept is the starting velocity of the ball, which in this example is zero.
  
~~~python
import matplotlib.pyplot as plt

plt.scatter(numpy.linspace(0,10,50),velocity_list)
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Velocity of an object accelerated by gravity")
~~~
  
</details>

{::options parse_block_html="false" /}


Use the polyval function to generate and plot velocities over the timeframe 30 to 100 seconds.
 
{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>
  
~~~python
import matplotlib.pyplot as plt

time_range = numpy.linspace(30,100,70)
plt.plot(time_range,np.polyval(fit,time_range))
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Velocity of an object accelerated by gravity")
~~~

</details>

{::options parse_block_html="false" /}

# Error bars and exponential growth

This question is partly modelled on the a [blog post](https://towardsdatascience.com/modeling-exponential-growth-49a2b6f22e1f). There is also a nice
[3Blue1Brown video on exponential growth in the context of Covid](https://www.youtube.com/watch?v=Kas0tIxDvrg).

We have the following (hypothetical) data for the growth in Covid cases at a university over a two-week period

~~~python
import numpy as np
day = np.arange(0,14)
case_numbers = np.array([2,3,4,8,15,32,65,128,253,512,1025,2049,4090,8191,16387])
~~~

Assuming that the growth is exponential, fit a straight line to the log of the case number data and predict the exponential growth factor. 
 
{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>

From scanning the blog post we can see that the growth factor is the base of the exponential.
Assuming the growth is exponential, to generate a straight-(ish) line we first need to take a logarithm of the case values data.
We can then fit a straight line to this to calculate the logarithm of the growth factor. 

~~~python
log_growth_factor, log_starting_case_number = np.polyfit(day,np.log(case_numbers),1)
growth_factor = np.exp(log_growth_factor)
~~~
  

</details>

{::options parse_block_html="false" /}

From inspecting the data, does the calculated growth factor make sense? 

{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>

The data roughly doubles each day. The calculated growth factor is 1.94, which is reassuringly close to 2. 


</details>

{::options parse_block_html="false" /}

---

Back to [Data analysis and visualisation](https://nu-cem.github.io/CompPhys/2021/08/02/Data_analysis.html).

---
