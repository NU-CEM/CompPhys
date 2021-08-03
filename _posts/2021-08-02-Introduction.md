---
toc: false
layout: post
title: Introduction and Setup
sticky_rank: 1
hide: true
---

### Introduction

Computing has become central to virtually all research and development in academia and industry, 
and with the advent of Machine Learning and High-Performance Computing this dominance is set to continue.

Computational physics encompasses a wide number of areas including materials modelling, particle physics simulations, protein structure prediction and plasma modelling. In fact, it is possible to find a computational branch for every major field in physics.

The focus of this course is to equip with you with the transferable skills needed for success in a range of computational disciplines, with examples tailored towards the physics domain.

This course is split into three sections - *Getting started*, *Getting results* and *Getting it out there*.
The software packages we will introduce in the first part of the course, *Getting started*, are applicable to all areas of research and industry - from game design to architecture. In the middle section of the course, which is called *Getting results*, we will apply these tools to model the differential equations that are so central to both classical and quantum physics. In the final section of the course, called *Getting it out there*, we will use modern software engineering techniques to document, test and share our code.

{% include alert.html text="An eye for detail is important. If you include an extra full-stop, or forget a space, then your code may not run. Don't let these Error messages worry you - they won't break the computer! - but do double check the steps you have taken and the code you have written for typos or 'silly' mistakes." %}


### Setup
  
To participate in this course you will need access to the following software: Python, Bash, Git and Jupyter.
To install this software on your personal laptop or desktop carefully follow the instructions listed below. 

You will also need a user account at [github.com](https://github.com) - Basic GitHub accounts are free.

{% include info.html text="All of the software needed for this course is pre-installed in the MPEE computers at Northumbria University" %}

{% include alert.html text="You can also run the Python Jupyter Notebook files remotely through the [binder] or [colab] services whenever you see an icon (e.g. like those at the top of [this page]()). But be warned! Any changes you make are not saved and the service can time-out after a period of inactivity (usually ~20 minutes)." %}

#### Python 

[Python][python] is a popular language for scientific computing, and great for
general-purpose programming as well. Installing all of its scientific packages
individually can be a bit difficult, however, so we recommend the all-in-one
installer [Anaconda][anaconda].
Please make sure you install Python
version 3.x (e.g., 3.4 is fine). 

##### Windows - [Video tutorial]

1. Open [https://www.anaconda.com/download]
   with your web browser.

2. Download the Python 3 installer for Windows.

3. Double-click the executable and install Python 3 using _MOST_ of the
   default settings, the only exception is to check **Add Anaconda to my PATH environment variable**.

##### Mac OS X - [Video tutorial]

1. Open [https://www.anaconda.com/download]
   with your web browser.

2. Download the Python 3 installer for OS X.

3. Install Python 3 using all of the defaults for installation.
        
#### Bash and Git

Bash is a commonly-used shell that gives you the power to do simple tasks more quickly.
Git is version-control software that allows to you to develop code more efficiently and share a public version of your code on github.com. 
In fact, this website is built using Bash, Git and github.com (amongst other tools) - the code can be found [here]().
You can download both tools at the same time following the instructions below.

#####  Windows - [video tutorial](https://www.youtube.com/watch?v=339AEqk9c-8)

1. Download the Git for Windows [installer](https://git-for-windows.github.io/)

2. Run the installer and follow the steps below:
    
    a) Click on "Next" four times (two times if you've previously
                installed Git).  You don't need to change anything
                in the Information, location, components, and start menu screens.
 
    b) Select “Use the nano editor by default” and click on “Next”.

    c) Keep "Use Git from the command line and..." selected and click on "Next".
                If you forgot to do this programs that you need for the workshop will not work properly.
                If this happens rerun the installer and select the appropriate option.
                
    d) Click on "Next"
    
    e) Keep "Checkout Windows-style, commit Unix-style line endings" selected and click on "Next".

    f) Select "Use Windows' default console window" and click on "Next".
    
    g) Ensure that "Default (fast-forward or merge) is selected and click "Next"

    h) Ensure that "Git Credential Manager Core" is selected and click on "Next".

    i) Ensure that "Enable file system caching" is selected and click on "Next". 
    
    j) Click on "Install"
    
    k) Click on "Finish"

3. If your "HOME" environment variable is not set (or you don't know what this is):

   a) Open command prompt (Open Start Menu then type <code>cmd</code> and press [Enter])

   b) Type the following line into the command prompt window exactly as shown:
     `setx HOME "%USERPROFILE%"`

   c) Press [Enter], you should see `SUCCESS: Specified value was saved.`
  
  d) Quit command prompt by typing `exit` then pressing [Enter]

This will provide you with both Git and Bash in the Git Bash program.

##### macOS

For macOS, install Git for Mac by downloading and running the most recent "mavericks" installer from [this list](https://sourceforge.net/projects/git-osx-installer/files/). Because this installer is not signed by the developer, you may have to right click (control click) on the .pkg file, click Open, and click Open on the pop up window. After installing Git, there will not be anything in your `/Applications` folder, as Git is a command line program. For older versions of OS X (10.5-10.8) use the most recent available installer labelled "snow-leopard" available [here](). 
       
See the Git installation <a href="https://www.youtube.com/watch?v=9LQhwETCdwY ">video tutorial</a>
        for an example on how to open the Terminal.

#### Jupyter

We will teach Python using the [Jupyter notebook][jupyter], a 
programming environment that runs in a web browser. Jupyter requires a reasonably 
up-to-date browser, preferably a current version of Chrome, Safari, or Firefox 
(note that Internet Explorer version 9 and below are *not* supported). Jupyter was installed as part of the Anaconda package for Python.

### Test your Setup

To check that this software has installed correctly, open Git bash (or terminal) and type the command:

~~~
$ jupyter notebook
~~~
{: .bash}

You should see a file browser pop up as a new tab on your browser. Select `new` and you should see `Python 3` listed as an option. Clicking on this will create a new Python 3 notebook file.

To start the Python interpreter without the notebook, you can open a terminal 
or Git Bash and type the command:

~~~
$ python
~~~
{: .bash}
