---
toc: false
layout: post
title: Modelling ODEs - extension
hide: true
---

## The fourth order Runge-Kutta method

We can extend the approach outlined in [the Runge-Kutta tutorial] to higher orders. The most common method for the numerical solution of ODEs is the fourth-order Runge-Kutta method (RK4).
This is accurate to terms of order $h^4$ (equivalently, it carries an error or order $h^5$). It's derivation is quite tedious, but the approach is the same as that for the second-order method:
 we Taylor expand around various points and take linear combinations that lead to the cancellation of terms in $h^3$, $h^4$ and so on.
 
 The five resulting equations are:
 
\begin{equation}
k_1 = hf(x,t)
\end{equation}
 
\begin{equation}
k_2 = hf(x+\frac{1}{2}k_1,t+\frac{1}{2}h)
\end{equation}
 
\begin{equation}
k_3 = hf(x+\frac{1}{2}k_2,t+\frac{1}{2}h)
\end{equation}
 
\begin{equation}
k_4 = hf(x+k_3,t+h)
\end{equation}
 
\begin{equation}
x(t+h) = x(t) + \frac{1}{6}(k_1+2k_2+2k_3+k_4)
\end{equation}

Use RK4 to solve the differential equation

\begin{equation}
\frac{\mathrm{d}x}{\mathrm{d}t} = -x^3 + \mathrm{sin} t
\end{equation}

with the initial condition $x=0$ at $t=0$.

Plot $x(t)$ for a number of steps $N$ equal to 10, 20, 50 and 1000. How does convergence compare to that when using RK2 (which was a question in [the exercises](https://nu-cem.github.io/CompPhys/2021/08/02/ODE_exercises))?

## Dynamical systems

The motion of two bodies of mass $m_1$ and $m_2$ attracted by gravity is the Kepler problem. 
In this case the moving bodies experience a force varying as the inverse square of the distance between them; for body one the distance to body two is 
 
 \begin{equation} 
 \mathbf{r}_{12} =  \mathbf{r}_1-\mathbf{r}_2,
 \end{equation}
 
 whilst for body two the distance to body one is 
 
 \begin{equation}
 \mathbf{r}_{21} =  \mathbf{r}_2-\mathbf{r}_1.
 \end{equation}
 
 So that the corresponding forces are:

\begin{equation}
\mathbf{F}_1 = -\frac{Gm_1m_2}{r_{12}}\hat{\mathbf{r_{12}}}
\end{equation}

\begin{equation}
\mathbf{F}_2 = -\frac{Gm_1m_2}{r_{21}}\hat{\mathbf{r_{21}}}
\end{equation}

Numerically compute and plot the orbits by integrating the equations of motion:

\begin{equation}
m_1\mathbf{a}_1 = \mathbf{F}_1,
\end{equation}

\begin{equation}
m_2\mathbf{a}_2 = \mathbf{F}_2.
\end{equation}

Use the Euler method for the integration:

\begin{equation}
\mathrm{v}_1(t+\Delta t)= \mathrm{v}_1(t)+\Delta t \frac{\mathrm{F_1}}{m_1}
\end{equation}

\begin{equation}
\mathrm{v}_2(t+\Delta t)= \mathrm{v}_2(t)+\Delta t \frac{\mathrm{F_2}}{m_2}
\end{equation}

\begin{equation}
\mathrm{r}_1(t+\Delta t)= \mathrm{r}_1(t)+\Delta t \mathrm{v}_1(t)
\end{equation}

\begin{equation}
\mathrm{r}_2(t+\Delta t)= \mathrm{r}_2(t)+\Delta t \mathrm{v}_2(t)
\end{equation}

Assume that the $z$ axis is perpendicular to the plane of motion so that the motion is in two dimensions. Note that the force is not constant - it depends on $r$, which couples together the equations for $\mathbf{v}$ and $\mathbf{r}$

For the parameters assume $G=1$, $m_1=1$ and $m_2=1$. For the initial conditions, assume that $r_1 = [1,0]$, $r_2 = [-1,0]$, $v_1 = [0,0.5]$ and $v_2 = [0,-0.5]$. Integrate up to the time $t_\mathrm{max} = 20$ with a time step size of $\delta t = 0.05$.

Once you have working code, change the initial velocities and comment on what you observe.

---

Back to [Modelling with Ordinary Differential Equations](https://nu-cem.github.io/CompPhys/2021/08/02/ODEs.html).

---
