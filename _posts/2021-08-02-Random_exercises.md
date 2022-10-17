---
toc: false
layout: post
title: Numerical integration - exercises
hide: true
---

## The Stefan-Boltzmann constant

Planck's law tells us that in the angular frequency interval $\omega$ to $\omega+\mathrm{d}\omega$, a black-body of unit area and temperature $T$ radiates electromagnetically an amount of thermal energy per second equal to $I(\omega)\mathrm{d}\omega$, where

$I(\omega) = \frac{\hbar}{4\pi^2\mathrm{c}^2}\frac{\omega}{(\mathrm{e}^{\frac{\hbar\omega}{k_\mathrm{B}T}}-1)}.$

The quantum theory of modern physics was born with Planck's law. Up until this point, an outstanding problem in physics was the ultra-violet catastrophe, a prediction from classical physics that a black body at thermal equilibrium would emit an unbounded quantity of energy as wavelength decreased into the ultraviolet range. This was in stark contrast to what was being measured experimentally. To resolve this, Planck assumed that electromagnetic radiation can only be absorbed or emitted in discrete packets (quanta) and from this derives Planck's law as shown above. Planck's law was in agreement with experimental results and the Stefan-Boltzmann law, which states:

$W = \sigma T^4$

where $\sigma$ is the Stefan-Boltzmann constant.

Einstein later postulated that the discrete quanta are real, physical particles (photons) and used this to explain the photoelectric effect. This research resulted in Einstein receiving the Nobel prize for physics in 1921.

By substituting $x = \frac{\hbar\omega}{k_\mathrm{B}T}$ we can deduce that the total rate of energy radiation by a black body per unit area, over all frequencies, is

$W = \frac{k_\mathrm{B}^4T^4}{4\pi^2\mathrm{c}^2\hbar^3}\int_0^\infty\frac{x^3}{(\mathrm{e}^x-1)}\mathrm{d}x.$

a) We will approximate the exact expression, an integral from 0 to $\infty$, using an integral with finite limits. Plot the integrand as a function of $x$ to justify your choice of limits.

b) Use the rectangular slice method to evaluate the integral in the expression for $W$

c) Use your value for the integral above to compute a value for the Stefan-Boltzmann constant to three significant figures. Check your result against the known value (available in the `scipy.constants` library).

d) Show that the error of your estimate scales linearly with the width $h$ of the rectangular slices used to approximate the integral.
