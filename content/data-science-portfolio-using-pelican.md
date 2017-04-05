Title: Data science portfolio using pelican
Slug: data-science-portfolio-using-pelican
Date: 2017-04-04 20:00
Category: machine leaning
Tags: data science, machine learning, portfolio, pelican
Author: Gabriel Rezzonico
Summary: How to set up a data science portfolio using pelican to generate static content.

# Data science portfolio using pelican

I'm going to explain how I set up this machine learning/data science/programming blog to be used as a portfolio and to have a place to keep track of all the projects I will be doing. The blog is going to be a static file, it's going to be hosted in github. To generate the content we are going to use a software called pelican.

I already have a website hosted in my user github page. So I'm going to be using a project. This can change a few this in regard to were is the content generated and how to setup github!

## Set up a conda enviroment

I'm going to be using conda enviroments to isoled all the dependencies I'm going to install to write the blog. It's going to be easy to activate the enviroment when ever I want to write a post and test everything. I'm using anaconda enviroments because I have anaconda already installed for my machine learning projects. If you don't have anaconda installed, [read this](https://docs.continuum.io/anaconda/install). If you want to know more about anaconda enviroments, [read this](https://conda.io/docs/using/envs.html ).

Create an enviroment with the following command, I'm going to call it "jupyter_blog_3.5", I'm going to be using python 3.5:

```bash
(jupyter_blog_3.5)$  conda create --name jupyter_blog_3.5 python=3.5
```
Activate the enviroment (this command is for linux, in windows is "activate env_name"):

```bash
(jupyter_blog_3.5)$  source activate jupyter_blog_3.5
```

Install pelican, a few dependencies and tools:

```bash
(jupyter_blog_3.5)$  conda install -c conda-forge pelican
(jupyter_blog_3.5)$  conda install jupyter ghp-import ipython nbconvert markdown
```

## Run the initial setup

Create a folder for the blog:

```bash
(jupyter_blog_3.5)$  mkdir jupyter-blog
```


Initialize an empty git repository
```bash
(jupyter_blog_3.5)$  git init
```

Run pelican wuickstart:

```bash
(jupyter_blog_3.5)$  pelican-quickstart
```

Follow the instructions and the following files and directories are going to be created:

```
    output
    content
    .gitignore
    develop_server.sh
    fabfile.py
    Makefile
    requirements.txt
    pelicanconf.py
    publishconf.py
```


## Install jupyter notebooks plugin

In order to use jupyter notebooks in our blog we need to install a plugin:


```bash
(jupyter_blog_3.5)$  mkdir plugins
(jupyter_blog_3.5)$  cd plugins/
(jupyter_blog_3.5)$  git submodule add git://github.com/danielfrg/pelican-ipynb.git plugins/ipynb
```

We need to tell pelican about the plugin, open the file called "pelicanconf.py" located in the root blog directory:

```bash
(jupyter_blog_3.5)$  nano pelicanconf.py
```

And add the following content:

```python
MARKUP = ('md', 'ipynb')

PLUGIN_PATH = './plugins'
PLUGINS = ['ipynb.markup']
```

Since I'm going to be using a project page the content can be generated in the docs/ folder:

```bash
mkdir docs
```
And add the following content to pelicanconf.py:

```python
OUTPUT_PATH = 'docs/'
```

## The first two post

We are going to write two post, one using simple markdown and the other using a jupyter notebook. Copy this files to the content folder in your blog:

https://raw.githubusercontent.com/gabrielrezzonico/blog/master/content/first-post.ipynb

https://raw.githubusercontent.com/gabrielrezzonico/blog/master/content/first-post.ipynb-meta

https://raw.githubusercontent.com/gabrielrezzonico/blog/master/content/test-md-post.md

Change the titles and author if you want.

## Testing the blog

To test the blog we first have to generate the static content:

```bash
(jupyter_blog_3.5)$  mkdir docs
(jupyter_blog_3.5)$  pelican content
```

This is going to generate the content in the "docs" folder (this is because I already have a github page and I using a project page to host this blog. [more info](https://pages.github.com/)). 

We are going to use python simple server to test that its working:

```bash
(jupyter_blog_3.5) jupyter-blog $ cd docs
(jupyter_blog_3.5) jupyter-blog/docs$  python -m pelican.server
```

Open the browser and go to "localhost:8000"


## Create a github page

I'm going to be using a github project page (like username.github.io/project). You can also use a github user page (like username.github.io).

First create a repository, I'm going to be calling mine "blog" (if you want to use your github use page you have to name the repository with your usename)

![image](images/create_repo.png?raw=true)

In the github page configuration make sure that the source is set to "master branch/docs folder".


## Publishing the blog (pushing to github)

Add your github repo url as a remote in your project:

```bash
(jupyter_blog_3.5)$  git remote add origin git@github.com:gabrielrezzonico/blog.git
```

Generate the content for publishing:

```bash
(jupyter_blog_3.5)$  pelican content -s publishconf.py
```

When ever you want to publish the content you are going to have to run this command.

```bash
(jupyter_blog_3.5)$  git add .
(jupyter_blog_3.5)$  git commit -m "initial commit"
(jupyter_blog_3.5)$  git push -u origin master
```

## Add a custom domain 

I'm going to be using a custom github page domain, blog.gabrielrezzonico.com (I already have another website at gabrielrezzonico.com)), so I need to change the custom domain in the github repository configuration page:

![image](images/repo_options.png?raw=true)

Change the publishing configuration in the "publishconf.py in the root folder of your blog:

```
SITEURL = 'http://blog.gabrielrezzonico.com'
```

We have to pull the changes from github.

```bash
(jupyter_blog_3.5)$ git pull
```


```bash
(jupyter_blog_3.5)$  git add .
(jupyter_blog_3.5)$  git commit -m "initial commit"
(jupyter_blog_3.5)$  git push -u origin master
```


Now you can open your browser and go to you url to check the live blog: ( in this case http://blog.gabrielrezzonico.com)

## Install a pelican theme

I'm going to be using [this theme](https://github.com/gilsondev/pelican-clean-blog), you can check all the available themes at: [http://www.pelicanthemes.com/](http://www.pelicanthemes.com/).





Create a folder for the themes. We are going to be installing the theme as a git submodule.

```bash
(jupyter_blog_3.5)$  mkdir themes
```

Add the submodule:

```bash
git submodule add https://github.com/gilsondev/pelican-clean-blog.git themes/pelican-clean-blog
```

Now add the following lines to pelicanconf.py config to tell pelican to use the new theme:

```python
THEME = 'themes/pelican-clean-blog'
```

Now to test your blog run

```bash
(jupyter_blog_3.5)$  pelican content
```

```bash
(jupyter_blog_3.5) jupyter-blog/docs$  python -m pelican.server
```

And to publish your changes:

```bash
(jupyter_blog_3.5)$ pelican content -s publishconf.py
```

```bash
(jupyter_blog_3.5)$  git add .
(jupyter_blog_3.5)$  git commit -m "plugin"
(jupyter_blog_3.5)$  git push -u origin master
```