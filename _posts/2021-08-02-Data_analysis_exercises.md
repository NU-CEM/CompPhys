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

a) Read in the photoelectric measurement data from the file Planck.txt. The first column contains frequencies $f$ is hertz and the second column contains voltages $V$. Use this data to plot $V$ vs $f$. Think about the plot type - does a scatter plot of line plot make most sense?

The least-squares method is very commonly used for fitting a polynomial to a set of data. As it is so prevalent in physics and engineering, you are encouraged to watch [this video](https://www.youtube.com/watch?v=YwZYSTQs-Hk) which give an intuitive and mathematical description of the method. 

b) Fit a straight line (polynomial of degree one) to the data using the least-squares method implemented in [`numpy.polyfit`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html). Overlay this line on your data points. 

c) Using the gradient of the fitted line calculate a value for Planck's constant. Compare this to values you can find online.

---

Back to [Data analysis and visualisation](https://nu-cem.github.io/CompPhys/2021/08/02/Data_analysis.html).

---
