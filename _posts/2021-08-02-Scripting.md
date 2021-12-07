---
toc: false
layout: post
categories: [mathematics, numerical recipes]
title: Python scripts and the Unix terminal
sticky_rank: 8
hide: true
---

-------

Questions:
- How can I convert my Jupyter Notebook into a Python script?
- What are the basic Unix commands needed for running a Python script from the command line?
- How can the script read user-specified values (command line arguments?)

Objectives:
- Convert a Jupyter Notebook into a Python script
- Navigate around a computer using the Unix commands `ls`, `cd` and `pwd`, `./`, `..` and `~`
- Run a Python script from the command line
- Read in command line arguments using the `sys.argv` array

Keypoints:
- A Python script is a `.py` file that contains Python code only
- Use a plain text editor to write a Python script
- Use a shebang at the top of your file to indicate that it is Python code
- Terminals are a way to interact with a computer without using a Graphical User Interface (GUI)
- You can navigate around your computer using the Unix shell
- To run your python code type the filepath into the terminal
- Use `sys.argv` to read in command line arguments

-------

### A Python script is a `.py` file that contains Python code only

- In the course so far we have used Jupyter Notebooks (.ipynb files) to develop and share code.
- Jupyter Notebooks are useful as they allow us to develop a narrative (of code, text and images).
- However sometimes running the code as a Python script (.py file) is more suitable. For example, you may want to run code on a High-Performance-Computer which you interact with through the command line terminal. Or perhaps you want to avoid the problems that can arise from running Jupyter notebook cells out of order.
- A Python script is a `.py` file that contains Python code only (though comments with a # are still possible)

### Use a plain text editor to write a Python script

- To write a Python script you can use any plain text editor (*not* Microsoft Word).
- On Windows you could use Notepad. On a Mac you can use TextEdit but you must select `Make plain text` under the `Format` menu. The [Sublime](https://www.sublimetext.com/) text editor is free to download on an unlimited trial basis and is a popular option for both systems.

### Use a shebang at the top of your file to indicate that it is Python code

- At the top of your empty text file insert the following line: `#!/usr/bin/env python3`. 
- This is the Python shebang. This line is not mandatory but it has two benefits: a reader can quickly identify it as a Python script, and the script can be ran without using the `Python` command (more on this later).
- Beneath this you write the Python code. In this example, we will copy across code from an earlier [tutorial example](https://nu-cem.github.io/CompPhys/2021/08/02/Strange-Attractor). We will save the resulting plot to a file, and also print out some messages as the programme is running.
- Save your Python file with a `.py` extension - e.g. `Lorenz.py`

~~~python

#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

print("Initialising the simulation...")

# define function that describe the Lorenz system.
def Lorenz(sigma,r,b,xyz):
    
    x = xyz[0]
    y = xyz[1]
    z = xyz[2]
    
    fx = sigma*(y-x)
    fy = (r*x)-y-(x*z)
    fz = (x*y)-(b*z)
    
    return np.array([fx,fy,fz],float)

# Simulation parameters
start = 0                  # start time
end = 50                 # end time
num_steps = 3000         # number of time steps
h = (end-start) / num_steps  # time step size

# intitial conditions: x=0, y=1, z=0
xyz = np.array([0,1,0],float)

# constants
sigma = 10
r = 28
b = 8/3

# generate times at which to evaluate xyz
time_list = np.arange(start,end,h)

# create empty arrays to hold the calculated values
x_points = []
y_points = []
z_points = []

print("Applying Euler's method...")

# Apply Euler's method
for time in time_list:
    
    x_points.append(xyz[0])
    y_points.append(xyz[1])
    z_points.append(xyz[2])
    xyz += h*Lorenz(sigma,r,b,xyz)
    
print("Plotting the results...")

# Plot the strange attractor
plt.plot(x_points,z_points)
plt.savefig("Strange_attractor.png")

~~~

### Terminals are a way to interact with a computer without using a Graphical User Interface (GUI)

- To run a Python script we can use a terminal programme, A.K.A the command line shell.
- Terminals are a way to interact with a computer without using a Graphical User Interface (GUI).
- The Windows terminal uses the shell language `Powershell`, whilst Mac and Linux both use Unix-based shells.
- The Unix-based shells are most popular for programming, and so that is what we will use here.
- If you are on Windows open up `Git Bash` (which contains the Unix shell). If you are on Mac open up `Terminal`.

### You can navigate around your computer using the Unix shell

- `ls` short for `list` displays the contents of a folder
- `pwd` short for `print working directory` displays your current position in the system
- `cd` is used to change directory
- `cd ..` means change to the parent directory
- `cd ~` means change to the home directory
- `cd ./data` means change to the data directory. `./data` provides a path relative to our current position in the system.
- `cd /Users/lucy` means change to the `lucy` directory. `/Users/lucy` without a `.` is an absolute path.

There is much, much more you can do with the Unix shell! We won't discuss them here but for more details see [this workshop](https://swcarpentry.github.io/shell-novice/) from Software Carpentry.

### To run your python code type the filepath into the terminal

- For example, if I have a Python file at `/Users/lucy/Code/Lorenz.py` then I could run it using the command `/Users/lucy/Code/Lorenz.py`.
- Alternatively I could navigate to the folder and then type the filename:

~~~sh
cd /Users/lucy/Code/
Lorenz.py
~~~

- After your code has ran you should see a new file (Strange_attractor.png) appear. You should also see some messages printed to the terminal screen.

### Use `sys.argv` to read in command line arguments

- We have seen the script print messages to the terminal but what about the other way around - how can users at the terminal pass values into the script?
- For example, we may want a user to specify the `end_time` variable used by the simulation as an argument. 
- For this we can use `sys.argv` which is a list of arguments passed to the programme
- The first item in the list, `sys.argv[0]`, contains the name of the programme: in this case, `Lorenz.py`. The second item in the list, `sys.argv[1]`, contains the first argument from the command line, the third item, `sys.argv[2]`, contains the second argument from the command line and so on.
- First, we need to edit the script
    - To access the `sys.argv` list we import the sys library at the top of our script: `import sys`
    - We set the `end_time` equal to the first command line argument: `end_time = float(sys.argv[1])`
    - Note that the argument is automatically read in as a string so we convert it to a float.
- Now, if the user runs `Lorenz.py 30` then `end_time` will equal 30.

~~~python

#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import sys

print("Initialising the simulation...")

# define function that describe the Lorenz system.
def Lorenz(sigma,r,b,xyz):
    
    x = xyz[0]
    y = xyz[1]
    z = xyz[2]
    
    fx = sigma*(y-x)
    fy = (r*x)-y-(x*z)
    fz = (x*y)-(b*z)
    
    return np.array([fx,fy,fz],float)

# Simulation parameters
start = 0                                     # start time
end_time = float(sys.argv[1])                 # end time
num_steps = 3000                              # number of time steps
h = (end-start) / num_steps                   # time step size

# intitial conditions: x=0, y=1, z=0
xyz = np.array([0,1,0],float)

# constants
sigma = 10
r = 28
b = 8/3

# generate times at which to evaluate xyz
time_list = np.arange(start,end,h)

# create empty arrays to hold the calculated values
x_points = []
y_points = []
z_points = []

print("Applying Euler's method...")

# Apply Euler's method
for time in time_list:
    
    x_points.append(xyz[0])
    y_points.append(xyz[1])
    z_points.append(xyz[2])
    xyz += h*Lorenz(sigma,r,b,xyz)
    
print("Plotting the results...")

# Plot the strange attractor
plt.plot(x_points,z_points)
plt.savefig("Strange_attractor.png")

~~~

### TASKS

1. Adapt the programme `Lorenz.py` so that it accepts 3 command line arguments: one for the `start_time`, one for `end_time` and one for `num_steps`.
2. Each time the `Lorenz.py` script runs the previous `.png` file is overwritten. Adapt the script so that the plot filename contains the values of the `start_time`, `end_time` and `num_steps` variables. You may need to search the internet for hints on how to do this (hint: look-up string formatting)

