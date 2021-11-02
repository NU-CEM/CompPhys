---
toc: false
layout: post
title: Classifying differential equations - quick test
hide: true
---

## Describing equations
Describe the following differential equations. Are they - 
- an ODE or PDE?
- first order or higher?
- linear or non-linear?
- heterogeneous or homogeneous?
- separable or non-separable?

a) The oscillation of a non-linear driven pendulum,

\begin{equation}
\frac{\mathrm{d}^2\theta}{\mathrm{d}t^2} = -\frac{g}{l}\sin(\theta) + C\cos(\theta)\sin(\sigma t),
\end{equation}

where $l$ and $\sigma$ are constant parameters and $g$ is the acceleration due to gravity.

b) The one dimensional diffusion equation,

\begin{equation}
\frac{\partial T}{\partial t} = D\frac{\partial ^2 T}{\partial x^2}.
\end{equation}

c) The motion of mass $m_1$ in the gravitational field of mass $m_2$ and with a viscous friction term,

\begin{equation}
m_1 \frac{\mathrm{d}^2 \mathbf{r}}{\mathrm{d} t^2} = -\frac{G m_1 m_2}{r^2} \mathbf{r} - cv^2\mathbf{v},
\end{equation}

where $v$ is the velocity.


{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>

  a) This equation is a second order, linear, heterogeneous, non-separable ODE.
  
  b) This equation is a second order, linear, homogeneous PDE. A linear, homogeneous PDE is separable and can be solved using the [Separation of Variables](https://tutorial.math.lamar.edu/classes/de/SeparationofVariables.aspx).
  
  c) This equation is a second order, non-linear, heterogeneous, non-separable ODE.
  
  </details>

{::options parse_block_html="false" /}
