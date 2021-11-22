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
- Git uses a two-step process for version control: `git add` and `git commit`
- You can `add` and `commit` multiple files
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

In this lesson we will be using a version control system called git. You can install and use git locally on your own computer (without any internet connection). However there are several online services that will store remote copies of your git repositories. Remote copies are highly encouraged for two reasons:
- as a backup in case your computer dies
- to share your work with other people

In this lesson we will be using this most popular git-based tool - [Github](https://github.com). This is also where all of the [code for this website is stored](https://github.com/nu-cem/CompPhys). We will see later in the course that Github can also be used to host website and automate tasks.

### Use `git init` to initialise an empty git repository

First, let's create a folder to hold the files we want to version control:

~~~bash
mkdir my_project
cd my_project
ls
~~~

Second, create a file. You can use the in-built terminal editor (vim)[https://www.vim.org/] or [nano](https://www.nano-editor.org/), or any plain-text editor (such as Notepad). Whichever editor you use, you need to make sure you save the file in the `my_scripts` folder.

~~~bash
vim hello.py
~~~

> Note: To start writing in vim type `i`.

~~~python

def hello_world():
  print("hello_world")

if __name__ == "__main__":
  hello_world()
~~~

> Note: We are not writing the Python shebang as we treating this like a Python module (with functions/code you can import) rather than a Python script that is ran from top-to-bottom.

> Note: To save and exit vim you type `Esc`, `:wq`, `Enter`.

Third, create a git repository to version control this new file:

~~~bash
git init
~~~

The git repository is a hidden file so to see it we need to use the command:

~~~bash
ls -a
~~~

~~~output
.   ..   .git   hello.py
~~~

Git stores all of the repository data in the .git directory. To delete the repository you delete this hidden folder

~~~bash
rm -rf .git
~~~

> Warning: Always take care using the command `rm -rf`. This permenantly deletes a directory and everything within the directory - and it will not be available in the recylcing bin!

### Use `git status` for a summary of your repository

`git status` is a very useful command. It summarises the status of your git repository.

~~~bash
git status
~~~

~~~output
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	hello.py

nothing added to commit but untracked files present (use "git add" to track)
~~~

> Note: For a long time the default branch in most Git repositories was named "master". Fortunately, many people have become aware that this terminology should be replaced to something more inclusive: `main`. If you branch is called `master` you can rename it using `git branch -m master main`.

The git outputs are generally quite helpful. Here we are told that there is "nothing added to commit but untracked files present" and git suggests that we use "git add" to track. What is this all about?

### Git uses a two-step process for version control: `git add` and `git commit`

If you think of Git as taking snapshots of changes over the life of a project, `git add` specifies what will go in a snapshot (putting things in the staging area), and `git commit` then actually takes the snapshot, and makes a permanent record of it (as a commit). 

![]("./images/add-commit.svg")
![]("./images/add-commit2.svg")

First let's add our new file:

~~~bash
git add hello.py
git status
~~~

~~~output
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   hello.py
~~~

Second let's commit our file to the repository history. We provide a short commit message, describing what the changes are and/or why they were made:

~~~bash
git commit -m "function to demonstrate the if __name__ == __main__ syntax"
~~~

~~~output
[main (root-commit) 0f7a7b4] create a hello_world function
 1 file changed, 5 insertions(+)
 create mode 100644 hello.py
~~~

> Note: Good commit messages often describe *why* a change was made. For example "fixed a bug that was breaking the unit tests". Information about *what* changed can be gotten by asking git to compare different versions of the file (we'll see this later in the lesson).

The two stage process is useful because it means you can carefully craft your commit snapshots. For example, I may make several changes to several files. I then want to version control the changes. Instead of being forced to use a single commit for changes that are unrelated I can split my changes into several smaller commits - for example, one for "implementing a new algorithm to find the minima" and one for "improved function docstrings".

### See the changes made to a file using `git diff`

Now let's make an edit to the file

~~~bash
vim hello.py
~~~

~~~python

def hello_world():
  "function to greet the world"
  print("hello_world")

if __name__ == "__main__":
  hello_world()
~~~

We can see the difference between the latest version of the file and the version of the file stored in the git repository using `git diff`:

~~~bash
git diff
~~~

~~~output
diff --git a/hello.py b/hello.py
index cd6a6ec..df4dfe3 100644
--- a/hello.py
+++ b/hello.py
@@ -1,4 +1,5 @@
 def hello_world():
+    "function to greet the world"
     print("helloooo world")

 if __name__ == "__main__":
(END)
~~~

Commit this change to the repository:

~~~bash
git add 
git commit -m "include docstring as per project guidelines"
git status
~~~

~~~output
On branch main
nothing to commit, working tree clean
~~~

Use git log to see a record of the commits that have been made

~~~bash
git log
~~~

~~~output
commit b4bfc23897e6dd3c8faed6f101b5438ff0cc98c1 (HEAD -> main)
Author: Lucy Whalley <l.whalley@northumbria.ac.uk>
Date:   Mon Nov 22 20:40:14 2021 +0000

    include docstring as per project guidelines

commit 0f7a7b4e03439cd9f854dec2f438a85ffbd31fd9
Author: Lucy Whalley <l.whalley@northumbria.ac.uk>
Date:   Mon Nov 22 20:24:32 2021 +0000

    function to demonstrate the if __name__ == __main__ syntax
~~~

### You can `add` and `commit` multiple files

Create a new python module that we will import into out "hello.py" module:

~~~bash
vim bonjour.py
~~~

~~~python
def bonjour_le_monde():
 print("bonjour le monde!")
~~~

~~~bash
vim hello.py
~~~

~~~python
import bonjour

def hello_world():
  "function to greet the world"
  print("hello_world")

if __name__ == "__main__":
  hello_world()
  bonjour.bonjour_le_monde()
~~~

~~~python
python hello.py
~~~

~~~output
hello_world
bonjour le monde!
~~~

~~~bash
git status
~~~

~~~output
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   hello.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	__pycache__/
	bonjour.py

no changes added to commit (use "git add" and/or "git commit -a")
~~~

We can add and commit both files at the same time

~~~bash
git add hello.py bonjour.py
git commit -m "implement and import french translation"
~~~

~~~output
[main 8fb9bff] implement and import french translation
 2 files changed, 6 insertions(+), 1 deletion(-)
 create mode 100644 bonjour.py
~~~

### Use `git push` and `git pull` to communicate with a remote repository

Currently all of our files and changes are stored locally on our computer.

In practice, most programmers hold up-to-date copies of their files on a remote service such as Github. To create a remote repository on the Github servers follow these four steps:

1. Log into Github
2. Click on the "+" icon in the top right hand corner to create a new repository
3. Provide a name and description
4. Select "Add a README file" and "Choose a license"

> Note: To decide which open source license you would like to use visit [https://choosealicense.com/](https://choosealicense.com/). 

You now need to `push` your local repository to the remote server. To do so, follow the commands under "...or push an existing repository from the command line" into your terminal (you need to be in the `my_project` folder when you do this).

~~~bash
git remote add origin https://github.com/lucydot/my_project.git
git push -u origin main
~~~

If you make changes to the files on the remote Github repository, you can `pull` these changes to your local repository with

~~~bash
git pull
~~~

It is important to `git push` and `git pull` frequently so that your local and remote repositories stay up-to-date with one another.

### For some tasks the Github web interface is a useful alternative

We have already seen how to create a repository on Github. You can also use the interface ("drag and drop") to add and commit files.

### TASKS

Use Github to:
1. Create a repository for holding the work done in this module
2. Create a README.md and select an open source license
3. Use the Github drag-and-drop interface to upload the script(s) you wrote in the previous lesson

Extension:
3. Use the git command line to version control and upload the Jupyter Notebooks (or any other file) generated during this course
