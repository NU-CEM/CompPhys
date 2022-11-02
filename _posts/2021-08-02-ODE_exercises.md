---
toc: false
layout: post
title: Modelling ODEs - exercises
hide: true
---

## Euler's method

Use Euler's method to solve the differential equation

\begin{equation}
\frac{\mathrm{d}x}{\mathrm{d}t} = -x^3 + \mathrm{sin} t
\end{equation}

with the initial condition $x=0$ at $t=0$.

Plot $x(t)$ up to $t=100$, using 1000 steps.

## Euler's method II

Use Euler's method to solve the differential equation

\begin{equation}
\frac{\mathrm{d}y}{\mathrm{d}x} = \mathrm{cos}(x)\mathrm{sin}(y)
\end{equation}

with the initial condition $x=3$ at $t=0$.

Plot $x(t)$ up to $t=100$, using 1000 steps.

## Second order Runge-Kutta method

Use a second order Runge-Kutta method to solve the differential equation

\begin{equation}
\frac{\mathrm{d}x}{\mathrm{d}t} = -x^3 + \mathrm{sin} t
\end{equation}

with the initial condition $x=0$ at $t=0$.

Plot $x(t)$ up to $t=100$, using 1000 steps. Investigate convergence with respect to the number of steps, and compare this to the performance of Euler's method.

## Modelling a non-linear pendulum

In [The strange attractor tutorial](https://nu-cem.github.io/CompPhys/2021/08/02/Strange-Attractor) we use Euler's method to solve simultaneous first order ODEs. 
At the end of the tutorial you are also shown how to re-cast the second order ODE for a non-linear pendulum as two simultaneous first order ODEs. Using expressions 11 and 12
on the tutorial page, and following the same method outlined as that outlined for the Strange Attractor, write a piece of code for modelling $\theta$ as a function of time.

> Tip: Combine the two variable $\theta$ and $\omega$ into a single vector $\mathbf{r} = (\theta,\omega)$. The method will give us a value for $\theta$ and $\omega$, but we can ignore the $\omega$ values generated if they are not needed.

---

Back to [Modelling with Ordinary Differential Equations](https://nu-cem.github.io/CompPhys/2021/08/02/ODEs.html).

---
