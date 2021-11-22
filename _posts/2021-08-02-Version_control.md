---
toc: false
layout: post
categories: [version control, unix]
title: Version control and Github
sticky_rank: 10
hide: true
---

-------

Questions:
- What is version control and why is it useful?
- How can I use Git to version control my files?
- What is the difference between Git and Github?

Objectives:
- Describe the benefits of version control
- Initialise a Git repository from the command line or through the Github interface
- Use command line git to version control your work locally
- Use git and Github to store and share a remote copy of your work

Keypoints:
- Version control is the ultimate undo button for code
- Github is very widely used in academia and industry
- Use `git init` to initialise an empty git repository
- Use `git status` for a summary of your repository
- Use `git add` and `git commit` to version control your files
- Ignore particular files and folders using a `.gitignore` file
- Use `git push` and `git pull` to communicate with a remote repository
- For some tasks the Github web interface is a useful alternative

-------

### Version control is the ultimate undo button for code

![]("./images/Final.png")

There are several benefits to version control:

- Nothing that is committed to version control is ever lost, unless you work really, really hard at it. 
- You can go back in time to see exactly who wrote what on a particular day, or what version of a program was used to generate a particular set of results.
- We can revert to a previous version, much like the “undo” feature in an editor.
- When several people collaborate in the same project, it’s possible to accidentally overlook or overwrite someone’s changes. The version control system automatically notifies users whenever there’s a conflict between one person’s work and another’s.

Version control is what software professionals use to keep track of what they’ve done and to collaborate with other people. Every large software development project relies on it, and most programmers use it for their small jobs as well. And it isn’t just for software: books, papers, small data sets, and anything that changes over time or needs to be shared can and should be stored in a version control system.

> Note: Version control is not well-suited to binary files as much of the functionality that we will see later does not work efficiently with these types of file. 

### Github is very widely used in academia and industry

In this lesson we will be using a version control system called git. You can install and use git locally on your own computer (without any internet connection). However there are several online services that will store remote copies of your repositories. Remote copies are highly encouraged for two reasons:
- as backup in case your computer dies
- to share your work with other people



### TASKS

Use Github to:
1. Create a repository for holding the work done in this module
2. Create a README.md and select an open source license
3. Upload the script(s) you developed last week

Extension:
3. Use the git command line to version control and upload the Jupyter Notebooks (or any other file) generated during this course
