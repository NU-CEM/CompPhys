---
toc: false
layout: post
title: Finite Difference Methods - quick test
hide: true
---

## Implementing the Laplacian

Use a five-point stencil to calculate

$\nabla^2\phi = \frac{\partial^2\phi}{\partial x^2} + \frac{\partial^2\phi}{\partial y^2} + \frac{\partial^2\phi}{\partial z^2}$

for $\phi = 6\cos(x)+7\sin(y)$ at $x=\pi, y=\pi$. Use a step-size of your choice and compare to the exact answer.

{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>

~~~python
import math

def integrand(x,y):
    return 6*math.cos(x) + 7*math.sin(y)

def laplacian(f_xy, x, y, h):
    return (f_xy(x+h,y) + f_xy(x-h,y) + f_xy(x,y+h) + f_xy(x,y-h) - 4*(f_xy(x,y))) / (h**2)    
  
laplacian(integrand, math.pi, math.pi, 1E-2)
~~~

~~~output
5.999950000159515
~~~
  
This is close to the exact answer of 6.
  
</details>

{::options parse_block_html="false" /}
