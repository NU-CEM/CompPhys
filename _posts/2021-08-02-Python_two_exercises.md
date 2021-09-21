---
toc: false
layout: post
categories: [python]
title: Python part two: exercises
sticky_rank: 3
hide: true
---

# A function to calculate standard errors

In experimental work it is common for a quantity of interest to be calculated from a combination of direct measurements. It is important to remember that all experimentally measured quantities present an uncertainty that will affect the final result.

The uncertainty is determined by the measurement instrument and settings. For example, if we measure a triangle with a caliper (resolution 0.1mm) we will get a more accurate value than if we use a ruler (resolution 1mm). But remember that whichever instrument we use we will introduce some amount of uncertainty. 

The table below outlines how the standard error can be obtained from the uncertainty associated with individual measurements.

| Calculation | Standard error |
|------|-------|
| Z = A+B | $(\Delta Z)^2 = (\Delta A)^2 + (\Delta B)^2$|
| Z = A-B | $(\Delta Z)^2 = (\Delta A)^2 + (\Delta B)^2$|
| Z = AB | $\left(\frac{\Delta Z}{Z}\right)^2 = \left(\frac{\Delta A}{A}\right)^2 + \left(\frac{\Delta B}{B}\right)^2$|
| Z = \frac{A}{B} | $\left(\frac{\Delta Z}{Z}\right)^2 = \left(\frac{\Delta A}{A}\right)^2 + \left(\frac{\Delta B}{B}\right)^2$|

a) Write a function which calculates the perimeter of a triangle and the standard error associated with this perimeter. The function argument will specify the length of each triangle side and the uncertainty associated with each measurement.

b) Using conditionals, write a function which calculates the standard error for any of the operations listed in the table. The function arguments will specify $A$, $B$, $\Delta A$, $\Delta B$ and the operation type.

# The emission lines of hydrogen

*Taken from Mark Newman's book "Computational Physics, p. 73*

There is a simple and famous formula for calculating the wavelengths $\lambda$ of the emission lines of the hydrogen atom.

$ \frac{1}{\lambda} = R\left(\frac{1}{m^2} - \frac{1}{n^2}\right),$

where R is the Tydberg constant ($R = 1.097\times 10^{-2}\mathrm{nm}^{-1}$) and $m$ and $n$ are positive integers and $n>m$.

a) Write a piece of code to calculate the Lyman series ($m=1$), Balmer series ($m=2$) and Paschen series ($m=3$).

