Title: Building and Distributing Packages
Slug: building-distributing-packages
Date: 2018-03-16 12:52
Category: posts
Tags: python, module, package, publishing
Author: Gabriel Rezzonico
Summary: What I have learnt from publishing my first python module.

# Building and Distributing Packages

## Python packages

Creating your own python package can be a daunting task. A lot of things to take into account, best practices for package development, project structure, unit test configuration, test coverage, publishing the package, and the list continues...

I wrote a sample project to use it as an easy way to start the development of new packages and avoid all the boilerplate needed. The source can be found at: [github](https://github.com/gabrielrezzonico/python_package_quickstart). 


## How to get started

* First clone, fork or download the [repo](https://github.com/gabrielrezzonico/python_package_quickstart)

*Note: delete the .git folder if you cloned the repo.

*  Project structure

| File or folder  | Description  |
|---|---|
| setup.py  | Module configuration.  |
| setup.cfg  | PyPi configuration.  |
| README.md  | this file.  |
| python_package_quickstart/  | The actual package/module. Where all the code resides.  |
| tests/  | Sample unit test using py.test.  |


* Create a virtualenv for development packages

It's allways a good idea to create an enviroment for the module.

```bash
conda create --name packages_p3 python=3.5
source activate packages_p3
conda install virtualenv
virtualenv venv
```

* Installing dev and test dependencies
```bash
pip install -e .[dev,test]
```

* Run the tests to check everything works
```bash
py.test tests
```

* Change the project name every where

* Change/add your package code

* To publish your package follow [this check list](https://github.com/gabrielrezzonico/python_package_quickstart#checklist-for-publishing)


## Further reading

There are tons of material to read about developing your own package and publishing it:

* [Official tutorial](https://packaging.python.org/tutorials/distributing-packages/)

* [Building and Distributing Packages with Setuptools](https://setuptools.readthedocs.io/en/latest/setuptools.html#id3)

* [Using TestPyPI](https://packaging.python.org/guides/using-testpypi/#using-test-pypi)

* [Heavily based this project on this tutorial](http://sherifsoliman.com/2016/09/30/Python-package-with-GitHub-PyPI/#do-you-have-a-setuppy)

* [Another blog](https://blog.ionelmc.ro/2014/05/25/python-packaging/)

* [Great explanation](https://jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/)


