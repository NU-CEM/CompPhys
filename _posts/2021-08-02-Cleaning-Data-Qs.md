---
toc: false
layout: post
title: Cleaning data - quick test
hide: true
---

## Pandas or Numpy

Pandas and [NumPy](https://numpy.org/) are both essential libraries for scientific computation due to their intuitive syntax and high-performance matrix computation capabilities. In which contexts might Pandas be a more useful library than Numpy (and vice-verca)?


{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>

- The Pandas module works well with tabular data. Pandas provides 2d table object called DataFrame.
- The NumPy module works well with numerical data. NumPy provides a multi-dimensional array, well suited to matrix operations.
- If memory is a limiting factor, NumPy typically consumes less memory than Pandas.

</details>

{::options parse_block_html="false" /}

## Crack the code

Crack the code using the dataframe `df` 

<img src="../images/alphabet.png"  class="plain" width="300"/>

```
df.loc[3,0:1] df.loc[0,4] df.loc[3,4] df.loc[0,4] df.loc[0,3]
df.loc[3,3] df.loc[4,2:3]
```

{::options parse_block_html="true" /}
<details>
  <summary markdown="span">Show answer</summary>

Mmm, tasty tasty "stewed veg".

</details>

{::options parse_block_html="false" /}

---

See [the notebook](https://nu-cem.github.io/CompPhys/2021/08/02/Cleaning-Data.html).

Back to [Data analysis and visualisation](https://nu-cem.github.io/CompPhys/2021/08/02/Data_analysis.html).

---
