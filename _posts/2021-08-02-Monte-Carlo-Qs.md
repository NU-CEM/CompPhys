---
toc: false
layout: post
title: Monte Carlo methods for integration - quick test
hide: true
---

## Integrating a semicircle re-visited

Use Monte Carlo integration (with 100 random points) to calculate the value of the integral:

$ I = \int_{-1}^1\sqrt{1-x^2}\mathrm{d}x $

How does this compare to exact answer? (Hint: the integrand is a semicircle of radius 1)

How can you improve the accuracy of your estimate?

Increase the number of points until you get an accuracy comparable (same order of magnitude) as the Riemann sum method with 100 points (which was implemented in the [Numerical integration - quick test](https://nu-cem.github.io/CompPhys/2021/08/02/Numerical-Integration-Qs.html)).

Use the [%%timeit notebook magic](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-timeit) to compare the calculation times for the Riemann sum method and Monte Carlo method.

Which is more efficient? 

{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>
    
We want to calculate the area of a semicircle with radius 1. We can adapt the approach used in the Monte Carlo tutorial but, in this case, we use the fact that $P_i = \frac{A_c}{A_r}$ where $A_r$ is a rectangle of length 2 (as the semicircle goes from $-1$ to $1$) and height 1.
  
~~~python
import random
import math
    
def estimate_semicircle_area(num_points):
    
    points = []
    hits = 0
    for i in range(num_points):
        # random.uniform(a,b) returns a random number drawn from a uniform distribution from a to b
        x, y = random.uniform(-1,1), random.uniform(0,1)
        # we test if the point is within the circle (using the equation for a circle, X^2+y^2=r^2)
        if x*x + y*y < 1.0:
            hits += 1
    
    probability = hits / num_points
    rectangle_area = 2
    return probability*rectangle_area
    
estimate_semicircle_area(100)
~~~
    
~~~output
1.58
~~~

Note that your estimate will be different as you be using a different set of random numbers.                        
The exact answer is $\frac{\pi}{2}$. The error on our calculation is
    
~~~python
math.pi/2 - estimate_semicircle_area(100)
~~~
    
~~~output
-0.04920367320510355
~~~
    
To improve the accuracy we can use a larger number of random points:
    
~~~python
math.pi/2 - estimate_semicircle_area(1000)
~~~

~~~output
0.04679632679489654
~~~   
          
~~~python                          
math.pi/2 - estimate_semicircle_area(10000)
~~~  
                          
~~~output
-0.0048036732051033315
~~~ 
                           
Increasing the number of points to 10,000 gives an error comparable to the Riemann sum method with 100 integration slices (where the error is 0.002). Let's use the %%timeit magic to time how long each takes to run
            
~~~python                          
%%timeit
estimate_semicircle_area(10000)
~~~  
                          
~~~output
6.23 ms ± 370 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
~~~ 
            
~~~python                          
%%timeit
rectangular_slice_integral(semicircle, -1, 1, 100)
~~~  
                          
~~~output
31 µs ± 1.09 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
~~~ 
            
As each method gives roughly the same accuracy, but the `estimate_semicircle_area` is 100x smaller, we can deduce that the Monte Carlo method implemented in `estimate_semicircle_area` is considerably less efficient than the Riemann summation method implemented in `rectangular_slice_integral`. However the Monte Carlo method is useful for badly behaving systems, as we will see in the lesson exercises.
   
</details>