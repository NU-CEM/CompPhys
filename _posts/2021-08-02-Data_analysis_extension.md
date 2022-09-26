---
toc: false
layout: post
title: Data analysis and visualisation - extension activity
hide: true
---

# Wave interference

*Adapted from Mark Newman's book "Computational Physics, p. 108*

When we drop a pebble in a pond waves travel out from the spot where it fell. The height of the waves at some time later could be represented by a sine wave, spreading out in a uniform circle. If the the pebble is dropped at $x_1,y_1$ (the centre of the circle) then the distance $r_1$ between a point $x,y$ and the pebble is:

$
r_1 = \sqrt((x-x_1)^2+(y-y_1)^2)
$

and the sine wave for the height $h$ is

$
h_1(x,y) = h_0\sin(kr_1),
$

where $h_0$ is the amplitdue of the waves and $k$ is the wavevector, related to the wavelength $\lambda$ by $k=\frac{2\pi}{\lambda}$.

**Task**: Write a piece of code to make an image of the wave heights over a 1 metre square region of pond. Suppose the wavelength $\lambda=5\mathrm{cm}$ and the amplitude $h_0=1$. You can choose where the pebble drops within the 1 metre square region. To make the image first create a $500\times500$ array of values representing the height $h_0$. Then use that array to make a density plot using [matplotlib.pyplot.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html).

Now suppose that we drop two pebbles in a pond. We will now have pebble one centred at $x_1,y_1$ (as above) and pebble two at $x_2,y_2$. The distance $r_2$ between a point $x,y$ and pebble two is:

$
r_2 = \sqrt((x-x_2)^2+(y-y_2)^2)
$

and the sine wave for the height $h$ is

$
h_2(x,y) = h_0\sin(kr_2).
$

Assuming the waves add linearly ([superpose](https://en.wikipedia.org/wiki/Superposition_principle)) the total height of the surface at a point $x,y$ is

$
h_{1,2}(x,y) = h_0\sin(kr_1)+h_0\sin(kr_2).
$

**Task**: Write a piece of code to make an image of the wave heights over a 1 metre square region of pond. Assume again that the wavelength $\lambda=5\mathrm{cm}$ and the amplitude $h_0=1$. You can choose where the pebbles drop but they should be $20\mathrm{cm}$ apart. To make the image first create a $500\times500$ array of values representing the height $h_0$. Then use that array to make a density plot using [matplotlib.pyplot.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html).

---

Back to [Data analysis and visualisation](https://nu-cem.github.io/CompPhys/2021/08/02/Data_analysis.html).

---
