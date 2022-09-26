---
toc: false
layout: post
title: Recap questions
sticky_rank: 1
hide: true
---

# Altitude of a satellite

*Adapted from Mark Newman's book "Computational Physics, p. 30*

A satellite is launched into a circular orbit around the earth so that it orbits the planet once every $T$ seconds. The altitude $h$ above the Earth's surface that the satellite must have is:

$h = \left(\frac{GMT^2}{4\pi^2}\right)^{\frac{1}{3}} - R$

where $G$ is Newton's gravitational constant, $M$ is the mass of the Earth, and $R$ is the radius.

a) Write a piece of code which calculates the altitude $h$ (in metres) for a given value of $T$ (in seconds).

b) Use this code to calculate the altitude of satellites that orbit the Earth once a day (a "geosynchronous" orbit) and once every 45 minutes. What can you conclude from this final calculation?

# A function to calculate standard errors

In experimental work it is common for a quantity of interest to be calculated from a combination of direct measurements. It is important to remember that all experimentally measured quantities present an uncertainty that will affect the final result.

The uncertainty is determined by the measurement instrument and settings. For example, if we measure a length with a caliper (resolution 0.1mm) we will get a more accurate value than if we use a ruler (resolution 1mm). But remember that whichever instrument we use we will introduce some amount of uncertainty. 

The table below outlines how the standard error can be obtained from the uncertainty associated with individual measurements.

| Calculation | Standard error |
|------|-------|
| Z = A+B | $(\Delta Z)^2 = (\Delta A)^2 + (\Delta B)^2$|
| Z = A-B | $(\Delta Z)^2 = (\Delta A)^2 + (\Delta B)^2$|
| Z = AB | $\left(\frac{\Delta Z}{Z}\right)^2 = \left(\frac{\Delta A}{A}\right)^2 + \left(\frac{\Delta B}{B}\right)^2$|
| Z = \frac{A}{B} | $\left(\frac{\Delta Z}{Z}\right)^2 = \left(\frac{\Delta A}{A}\right)^2 + \left(\frac{\Delta B}{B}\right)^2$|

a) Write a function which calculates the area of a circle and the standard error associated with this area. The function argument will specify the radii of the circle and the uncertainty associated with the measurement.

b) Using conditionals, write a function which calculates the standard error for any of the operations listed in the table. The function arguments will specify $A$, $B$, $\Delta A$, $\Delta B$ and the operation type.

# The emission lines of hydrogen

*Taken from Mark Newman's book "Computational Physics, p. 73*

There is a simple and famous formula for calculating the wavelengths $\lambda$ of the emission lines of the hydrogen atom.

$\frac{1}{\lambda} = R\left(\frac{1}{m^2} - \frac{1}{n^2}\right)$

where R is the Rydberg constant $R = 1.097\times 10^{-2}\mathrm{nm}^{-1}$ and $m$ and $n$ are positive integers and $n>m$.

a) Write a piece of code to calculate the Lyman series ($m=1$), Balmer series ($m=2$) and Paschen series ($m=3$).

# Calculating Planck's constant

*Adapted from Mark Newman's book "Computational Physics, p. 124*

When light is shone on the surface of a metal, the photons in the light can excite (transfer energy to) electrons in the metal and, sometimes, eject them from the surface into the free space above. The energy of the ejected electron can be calculated by measuring the minimum voltage $V$ that stops the electron moving.

We know that the energy of an ejected electron is equal to the energy of the photon that excited it minus the workfunction $\phi$ (which is the energy needed to remove it from the surface) and that the energy of a single photon is $hf$ where $h$ is Planck's constant and $f$ is the frequency of light. Mathematically this can be expressed as:

$eV = hf - \phi$,

where $e$ is the charge of the electron.

a) Read in the photoelectric measurement data from the file [Planck.txt](https://nu-cem.github.io/CompPhys/data/Planck.txt). The first column contains frequencies $f$ is hertz and the second column contains voltages $V$. Use this data to plot $V$ vs $f$. Think about the plot type - does a scatter plot of line plot make most sense?

The least-squares method is very commonly used for fitting a polynomial to a set of data. As it is so prevalent in physics and engineering, you are encouraged to watch [this video](https://www.youtube.com/watch?v=YwZYSTQs-Hk) which give an intuitive and mathematical description of the method. 

b) Fit a straight line (polynomial of degree one) to the data using the least-squares method implemented in [`numpy.polyfit`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html). Overlay this line on your data points. 

c) Using the gradient of the fitted line calculate a value for Planck's constant. Compare this to values you can find online.

# The Madelung constant

*Taken from Mark Newman's book "Computational Physics, p. 74*

The Madelung constant gives the total electric potential felt by an atom in a solid. It depends on the charge and position of other nearby atoms.

Consider the compound sodium chloride. These are arranged on a cubic lattice, with sodium having a positive charge ($+e$) and chlorine having a negative charge ($-e$). If each atom position is given by integers $(i,j,k)$ then the sodium atoms are at positions where $i+j+k$ is even and the chlorine atoms are at positions where $i+j+k$ is odd.

![](https://nu-cem.github.io/CompPhys/images/NaCl.png)

For an atom at $i=j=k=0$, the Madelung constant $M$ can be approximated by using the following formulae:

$V_\mathrm{total} = \sum_{i,j,k} V(i,j,k) = \frac{e}{4\pi\epsilon_0a}M$

$V(i,j,k) = \pm\\frac{e}{4\pi\epsilon_0r}$

where $r$ is the distance from the origin to the atom at position $(i,j,k)$ and $a$ is the atom spacing. The summation runs from $i,j,k=-L$ to $i,j,k=L$ but not including $i,j,k=0$ (otherwise the expression would "blow up").

a) Write an expression (in Markdown/LaTeX) for the distance $r$ in terms of $i$, $j$, $k$ and $a$.

b) Calculate the Madelung constant for sodium chloride using a large a value as L as you can (so the code runs in about a minute or less). How does it compare with published values?
