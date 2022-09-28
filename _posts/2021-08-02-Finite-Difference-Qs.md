---
toc: false
layout: post
title: Laplace's equation - quick test
hide: true
---

## Boundary conditions

In [the tutorial](https://nu-cem.github.io/CompPhys/2021/08/02/Finite-Difference) we implement a finite difference method to solve Laplace's equation. We use fixed boundary conditions, which are an example of [Dirichlet-type boundary conditions](https://math.libretexts.org/Bookshelves/Differential_Equations/Book%3A_Partial_Differential_Equations_(Walet)/03%3A_Boundary_and_Initial_Conditions/3.02%3A_Explicit_Boundary_Conditions). 

~~~python
def finite_difference(phi):

    for i in range(grid_height): # for each grid point
        for j in range(grid_width):
            if i==0 or i==grid_height-1 or j==0 or j==grid_width-1:
                phi_prime[i,j] = phi[i,j] # if at boundary, keep fixed
            else: # otherwise apply finite difference
                phi_prime[i,j] = (phi[i+1,j]+phi[i-1,j]+phi[i,j+1]+phi[i,j-1]) / 4
    
    return phi_prime
~~~

Another form of boundary condition is a Periodic Boundary Condition. PBCs are often chosen for approximating a large (infinite) system by using a small part called a unit cell, and are most famously used for modelling periodic crystals in solid state physics. Mathematically, PBCs can be expressed for $f(x,y)$ on a two dimensional $N \times N$ grid as:

\begin{equation}
f[N+1,y] = f[0,y],
\end{equation}

\begin{equation}
f[x,N+1] = f[x,0],
\end{equation}

Write a function which calculates `phi_prime` using a finite difference method with periodic boundary conditions.

{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>
    
~~~python
def finite_difference(phi):

    for i in range(N): # for each grid point
        for j in range(N):
    
            i1 = i+1
            j1 = j+1
            i2 = i-1
            j2 = j-1
            
            if i == N-1:
                i1 = 0
            if i == 0:
                i2 == N-1
            if j == N-1:
                j1 = 0
            if j == 0:
                j2 == N-1

            phi_prime[i,j] = (phi[i1,j]+phi[i2,j]+phi[i,j1]+phi[i,j2]) / 4
    
    return phi_prime
~~~
    
</details>

{::options parse_block_html="false" /}    

---

See [the notebook](https://nu-cem.github.io/CompPhys/2021/08/02/Finite-Difference.html).

Back to [Modelling with Partial Differential Equations](https://nu-cem.github.io/CompPhys/2021/08/02/PDEs.html).

---
