---
toc: false
layout: post
title: Introduction to PDEs - quick test
hide: true
---

## Boundary value problem or initial value problem

Decide whether the following systems are a boundary value problem or initial value problem, and whether they are diffusion-like, wave-like or poisson-like:

a) Brownian motion of small particles in a liquid (the random-walk)

\begin{equation}
\frac{dP}{dt} = \frac{l^2}{2Np^2}\del^2P
\end{equation}

b) the Klein-Gordon equation for describing the energy-momentum relation of relativistic particles:

\begin{equation}
\left(\frac{1}{c^2}\frac{\partial^2}{\partial t^2} - \del^2 + \frac{m^2c^2}{\hbar^2}\right)\phi(t,x)=0
\end{equation}

{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>
  
 a) this is an initial value problem described by the diffusion equation
 b) this is an initial value problem described by the wave equation
 
</details>

{::options parse_block_html="false" /}

---

See [the notebook](https://nu-cem.github.io/CompPhys/2021/08/02/PDE-Intro.html).

Back to [Modelling with Partial Differential Equations](https://nu-cem.github.io/CompPhys/2021/08/02/PDEs.html).

---
