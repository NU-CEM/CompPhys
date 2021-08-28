---
toc: false
layout: post
title: Cleaning data - quick test
hide: true
---

## Plot Scaling I

Why do all of our plots stop just short of the upper end of our graph?


{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>

Because matplotlib normally sets x and y axes limits to the min and max of our data
(depending on data range)
{: .solution}

If we want to change this, we can use the `set_ylim(min, max)` method of each 'axes',
for example:

~~~python
axes3.set_ylim(0,6)
~~~

</details>

{::options parse_block_html="false" /}

## Plot Scaling II

Update your plotting code to automatically set a more appropriate scale.
(Hint: you can make use of the `max` and `min` methods to help.)


{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>

~~~python
# One method
axes3.set_ylabel('min')
axes3.plot(numpy.min(data, axis=0))
axes3.set_ylim(0,6)
~~~


~~~python
# A more automated approach
min_data = numpy.min(data, axis=0)
axes3.set_ylabel('min')
axes3.plot(min_data)
axes3.set_ylim(numpy.min(min_data), numpy.max(min_data) * 1.1)
~~~

</details>

{::options parse_block_html="false" /}


## Make Your Own Plot

Create a plot showing the standard deviation (`numpy.std`)
of the absorption data for each day across all patients.


{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>

~~~python
std_plot = matplotlib.pyplot.plot(numpy.std(data, axis=0))
matplotlib.pyplot.show()
~~~

</details>

{::options parse_block_html="false" /}

## Moving Plots Around

Modify the program to display the three plots on top of one another
instead of side by side.


{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>


~~~python
import numpy
import matplotlib.pyplot

data = numpy.loadtxt(fname='UVVis-01-cleaned.csv', delimiter=',')

# change figsize (swap width and height)
fig = matplotlib.pyplot.figure(figsize=(3.0, 10.0))

# change add_subplot (swap first two parameters)
axes1 = fig.add_subplot(3, 1, 1)
axes2 = fig.add_subplot(3, 1, 2)
axes3 = fig.add_subplot(3, 1, 3)

axes1.set_ylabel('average')
axes1.plot(numpy.mean(data, axis=0))

axes2.set_ylabel('max')
axes2.plot(numpy.max(data, axis=0))

axes3.set_ylabel('min')
axes3.plot(numpy.min(data, axis=0))

fig.tight_layout()

matplotlib.pyplot.show()
~~~

</details>

{::options parse_block_html="false" /}


---

See [the notebook](https://nu-cem.github.io/CompPhys/2021/08/02/Visualising-Data.html).

Back to [Data analysis and visualisation](https://nu-cem.github.io/CompPhys/2021/08/02/Data_analysis.html).

---