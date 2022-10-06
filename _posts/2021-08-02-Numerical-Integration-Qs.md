---
toc: false
layout: post
title: Numerical integration - quick test
hide: true
---

## Integrating a semicircle

Use Riemann sums (with 10 rectangular slices) to calculate the value of the integral:

$ I = \int_{-1}^1\sqrt{1-x^2}\mathrm{d}x $

How does this compare to exact answer? (Hint: the integrand is a semicircle of radius 1)

How can you improve the accuracy of your estimate?

{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>
    
We can use the same approach as in the tutorial, but with a different function for calculating the integrand. 
  
~~~python
import math

def semicircle(x):
    
    return math.sqrt(1-x**2)

def rectangular_slice_integral(f_x, a, b, N):
    
    integral = 0
    h = (b-a) / N   # h is the width of each slice
    for i in range(N):
        x = a + h*i # the x value for the slice
        integral += f_x(x)*h
    return integral
    
rectangular_slice_integral(semicircle, -1, 1, 100)
~~~
    
~~~output
1.5691342555492505
~~~
    
The exact answer is $\frac{\pi}{2}$. The error on our calculation is
    
~~~python
math.pi/2 - rectangular_slice_integral(semicircle, -1, 1, 100)
~~~
    
~~~output
0.0016620712456461018
~~~
    
To improve the accuracy we can use a larger number of slices:
    
~~~python
math.pi/2 - rectangular_slice_integral(semicircle, -1, 1, 1000)
~~~

~~~output
5.2588293825595045e-05
~~~       
        
   
</details>