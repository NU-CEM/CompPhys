---
toc: false
layout: post
title: Modelling PDEs - exercises
hide: true
---

## Modelling the Poisson equation

*Adapted from Mark Newman's book "Computational Physics, p. 412*

In [one of the tutorials](https://nu-cem.github.io/CompPhys/2021/08/02/Finite-Difference) we have used the relaxation method to solve Laplace's equation for electrostatics:

\begin{equation}
\nabla^2\phi = 0
\end{equation}

A more general form of this equation is Poisson's equation:

\begin{equation}
\nabla^2\phi = -\frac{\rho}{\epsilon_0},
\end{equation

which governs the electric potential in the presence of charge density $\rho$.

Assume, as in the tutorial example for Laplace's equation, that there is a 1 meter square. However this time all four walls of the square at fixed at zero volts and that there are two 20cm x 20cm charged areas in the box. One charge has a density +1Cm$^-2$, the other has a density -1Cm$^-2$.

Modify the code for the Laplace's equation example to solve this problem using the relaxation method.

---

Back to [Modelling with Partial Differential Equations](https://nu-cem.github.io/CompPhys/2021/08/02/PDEs.html).

---