---
toc: false
layout: post
title: Modelling PDEs - extension
hide: true
---

### The method of finite differences for second order derivatives

In [one of the tutorials](https://nu-cem.github.io/CompPhys/2021/08/02/Finite-Difference) we give an expression for calculating second order derivatives using the finite difference method:

\begin{equation}
\frac{\mathrm{d} ^2f}{\mathrm{d} x^2} \simeq \frac{f(x+h)-2f(x)+f(x-h)}{h^2}.
\end{equation}

Using the fact that a second derivative is, by definition, a derivative of a derivative, and by applying the central difference method three times, derive this expression.

---

Back to [Modelling with Partial Differential Equations](https://nu-cem.github.io/CompPhys/2021/08/02/PDEs.html).

---
