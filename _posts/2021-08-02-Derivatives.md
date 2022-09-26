---
toc: false
layout: post
title: Calculating derivatives
categories: [data, python]
sticky_rank: 4
hide: true
---

> The origin of the notion of derivatives is in the vague feeling of the mobility of things, and of the greater or less speed with which phenomena take place. - Émile Picard

In physics we are often looking at how things change over time or space so, like integrals, the evaluation of derivatives is one of the most important applications of computers in physics - especially when solving partial differential equations (a topic we will cover later in the course). However, unlike integrals, the derivatives of **known** functions can always be calculated analytically, so
there’s generally less need to calculate them numerically. 

In this lesson we will learn how to calculate derivatives using finite difference methods, and take a brief look at the related operation of interpolation. There are some significant practical problems with numerical derivatives; at the end of this lesson we will also learn how to evaluate the accuracy and speed that can be achieved when using these various methods.

### Before you begin

- Check that Python and Jupyter Notebook are installed
- Launch a Jupyter notebook 

Please see the [Setup](https://nu-cem.github.io/CompPhys/2021/08/02/Setup) page for more details.

### Lesson outline

| Topic | Objective | Quick test |
|-------|-----------|-----------|
|[Finite difference methods](https://nu-cem.github.io/CompPhys/2021/08/02/Finite-Difference-Method)|How do I use a finite difference method to calculate derivatives?  | [:mag:](https://nu-cem.github.io/CompPhys/2021/08/02/Finite-Difference-Method-Qs.html) |
|[Evaluating numerical errors, accuracy and speed](https://nu-cem.github.io/CompPhys/2021/08/02/Computational-Efficiency)| How accurate are finite difference methods? </n> How can I measure the speed of my Python code? | [:paperclip:](https://nu-cem.github.io/CompPhys/2021/08/02/Computational-Efficiency-Qs.html)|

### Resources

- [Lesson exercises](https://nu-cem.github.io/CompPhys/2021/08/02/Derivatives_exercises)
- [Extension exercise](https://nu-cem.github.io/CompPhys/2021/08/02/Derivatives_extension)
- [Presentation](https://nu-cem.github.io/CompPhys/slides/Derivatives_slides)
