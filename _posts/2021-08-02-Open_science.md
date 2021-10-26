---
toc: flase
layout: post
categories: [unix, Github]
title: Build-your-own website 
sticky_rank: 11
hide: true
---

Questions:
- How can I create a project website?

Objectives:
- Differentiate between git, Github and Github pages.
- Use Github pages and markdown to create a single page website.
- Customise the website using the `_config.yml` file
- Use Github pages, markdown and Jekyll to create a multipage website

Keypoints:
- Github pages is a static site hosting service that takes HTML files from a Github repository and publishes a website.
- We can create a simple website in three short steps.
- Github pages can be combined with a variety of static site generators to create a customised website.
- A single page project site can be created using an `index.md` file on the `gh-pages` branch.
- Github pages combined with Jekyll top matter can be used to create quick multipage sites.
- Github has a range of Jekyll themes to choose from.
- To access a wider range of themes and customisation options you can add a `_config.yml` file.
- Other static site generators can be combined with Github actions for more flexibility.

### Github pages takes HTML files from a Github repository and publishes a website.

- First we should differentiate between three similar sounding tools:
  - [Git](https://git-scm.com/) is an open-source version control system that can be used online or locally.
  - [Github](https://github.com/) is a website (owned by Microsoft) that is built on top of git. It can be used to store and share files in project repositories.
  - [Github pages](https://pages.github.com/) is a service provided by Github. Github pages takes HTML from a repository and publishes it as a website.

> Note: Github is not the only option for hosting your code. Other services include [Gitlab](https://about.gitlab.com/) (which is an open source project) and [Bitbucket](https://bitbucket.org/product).

### We can create a simple website in three short steps

- To see the most simple example of how Github pages works we can create 1) create a repository 2) create a `gh-pages` branch and 3) add a html file.

- Step 1: Create a repository
  - Register for a Github account (if you do not already have one) and login
  - Create a new repository by clicking the `plus` sign at the top-right hand corner
  - Give your repository a name e.g. `website-example`
  - Give your repository a description e.g. `A simple example of a website generated using gh-pages`
  - Select `Add a README file`
  - Select `Choose a license` and select a license 
  - Click `Create repository`

> Important: You don't need to select a license at this stage but it's recommended that you do. The MIT License is a popular choice as it is simple and permissive (people do almost anything they want with your project). If you are not clear which license to use you can visit [https://choosealicense.com/](https://choosealicense.com/).

- Step 2: Create a gh-pages branch
  - Click `main` towards the top-left hand corner
  - Type `gh-pages` into the text box (Find or create a branch) 
  - Select `Create branch: gh-pages from 'main'

A branch in Git is similar to the branch of a tree. A tree branch is attached to the main part of the tree. While branches can generate and fall off, the main central part of the tree continues. Similarly, a branch in Git is a way of developing new features or fixing bugs without affecting the main part of the project (the `main` branch). The main branch is created when we create the git repository.

> Important: Github pages will automatically publish any html on the `gh-pages` branch only.

- Step 3: 
  - Click `Add file` (make sure you are on the gh-pages branch)
  - Click `Create new file`
  - Name the file `Hello-world.html`
  - Paste the following code

```
    <!DOCTYPE html>
    <html>
        <head>
            <title>Hello World!</title>
        </head>
        <body>
            <p>Soooo nice to meet you.</p>
        </body>
    </html>
```
  - Click `Commit new file`

You can access your project webpages using the address format `username.github.io/repository-name/filename.html`. If you have followed the suggested naming in this example you can access your Hello-world webpage at `https://username.github.io/website-example/Hello-world.html`

### Github pages can be combined with a variety of static site generators to create a customised website.

- It would take a lot of time to write our website using html (unless we want a really, really simple website)
- Instead there are several static site generators which will take plain text files (formatted using a markup language such as markdown or reStructuredText) and convert these into html.
