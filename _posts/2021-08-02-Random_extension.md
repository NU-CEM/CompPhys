---
toc: false
layout: post
title: Numerical integration - extension
hide: true
---

## Volume of a sphere

We have seen that performing an integral over one variable requires us to take samples across a one-dimensional grid. Similarly, integration over two variables requires us to take samples on a two-dimensional grid, and so on. The number of grid points required scales exponentially with the number of variables, so that integrals over three or more dimensions can quickly become unmanageable. In this case, Monte Carlo integration can be very useful.

The volume of a sphere with unit radius in three dimensions is given by:

$V = \int\int\int_{-1}^1f(x,y,z)\mathrm{d}x\mathrm{d}y\mathrm{d}z$

where $f(x,y,z)=1$ everywhere inside the sphere and zero everywhere outside.

a) Use Monte Carlo integration to estimate the volume of this sphere using 100 random points. 

b) Increase the number of random points until you reach an estimate that is exact to three significant figures.

c) By considering how many points would need to be sampled, estimate the length of time it would take to reach the same level of accuracy using a Riemann slice type method.


## The Stefan-Boltzmann constant re-visited

In the [lesson exercise](https://nu-cem.github.io/CompPhys/2021/08/02/Random_exercises) we use rectangular slices to estimate the Stefan-Boltzmann constant to three significant figures. The trapezoidal rule is a neat extension to rectangular slices, where the value at the start and end of each segment is considered. It can be expressed as

$\int^b_af(x)\mathrm{d}x = h\left[\frac{1}{2}f(a)+\frac{1}{2}f(b)+\sum_{k=1}^{N-1}f(a+kh)\right]$

a) Use the trapezoidal rule to re-calculate the Stefan-Boltzmann constant to three significant figures

b) Demonstrate that the error scales quadratically with $h^2$, and that the trapezoidal rule is more computationally efficient than using rectangular slices

c) The absolute error $\epsilon_n$ on the n^{th} estimate of an integral is given by $\epsilon_n = |\frac{1}{3}(I_n-I_{n-1})|$. Using this expression, write a programme that calculates the Stefan-Boltzmann with a maximum error of 1E-5.



