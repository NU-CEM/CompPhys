---
toc: false
layout: post
title: Classifying differential equations - quick test
hide: true
---

## Describing equations
For the following differentials identify if the equation is:
- an ODE or PDE
- first order or higher
- linear or non-linear
- heterogeneous or homogeneous
- separable or non-separable

a) The oscillation of a non-linear driven pendulum,

\begin{equation}
\frac{\mathrm{d}^2\theta}{\mathrm{t}^2} = -\frac{g}{l}\mathrm{sin}\theta + C\mathrm{cos}\theta\mathrm{sin}\sigma t.
\end{equation}

b) The one dimensional diffusion equation,

\begin{equation}
\frac{\partial T}{\partial t} = D\frac{\partial ^2 T}{\partial x^2}.
\end{equation}

c) The motion of two bodies with gravity and a viscous friction term,

\begin{equation}
m_1 \frac{\mathrm{d}^2 \mathbf{r}}{\mathrm{d} t^2} = -\frac{G m_1 m_2}{r^2} \hat{\mathbf{r}} - cv^2\hat{\mathbf{v}},
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
