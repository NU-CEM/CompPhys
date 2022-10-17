---
toc: false
layout: post
title: Finite Difference Methods - quick test
hide: true
---

## Implementing the Laplacian

Use a five-point stencil to calculate

$\nabla^2\phi = \frac{\partial^2\phi}{\partial x^2} + \frac{\partial^2\phi}{\partial y^2} + \frac{\partial^2\phi}{\partial z^2}$

for $\phi = 6\cos(x)+7\sin(y)$ at $x=\pi/4, y=\pi$. Use a step-size of your choice, making sure that the answer is converged to 5 significant figures.
