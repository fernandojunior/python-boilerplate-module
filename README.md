# python-boilerplate-module

A [boilerplate](https://en.wikipedia.org/wiki/Boilerplate_code) to create a Python module based project. [Clone](https://help.github.com/articles/cloning-a-repository/   ) or [download](https://github.com/fernandojunior/python-boilerplate-module/archive/master.zip) it.

* Author: [@fernandojunior](https://github.com/fernandojunior/)
* GitHub repository: [python-boilerplate-module](https://github.com/fernandojunior/python-boilerplate-module)
* Free software: [The MIT License](/LICENSE)

## Features

* Build and distribute with [setuptools](https://pythonhosted.org/setuptools/setuptools.html)
* Check code style with [flake8](https://flake8.readthedocs.org/)
* Make and run tests with [pytest](http://pytest.org/)
* Run tests on every Python version with [tox](https://tox.readthedocs.org/)
* Code coverage with [coverage.py](https://coverage.readthedocs.org/)

## Glossary
*The following terms are needed in order to understand the capabilities offered by this boilerplate.*

* `dependency` - A `distribution package` that is required to `build`, install and use a `project`.
* `build` - Refers to preparing a project in a `distribution package` that users can install and use easily.
* `distribution package` - A archive file with `packages`, `modules` or other resources used to distribute a `release`.
* `module` - A .py file that serves as a unit of Python source code which can expose variables, functions and classes.
* `package` - A directory containing an \_\_init\_\_.py file and which can contain `modules` or recursively, other `packages`.
* `pip` - The preferred package manager system for installing `distribution packages`.
* `project` - A library, framework, script, plugin, application, or other resources or some combination thereof.
* `release` - A snapshot of a `project` at a particular point in time, denoted by a version identifier.
* `virtualenv` - A tool to isolate a environment of a `project` and its `dependencies` from a Python installation.

Other glossaries:
* [Python](https://docs.python.org/3/glossary.html)
* [Python Packaging User Guide](https://python-packaging-user-guide.readthedocs.org/en/latest/glossary/)
* [Setuptools](http://pythonhosted.org/setuptools/pkg_resources.html)

## Structure

[Structure](http://docs.python-guide.org/en/latest/writing/structure/) of the project in [tree](http://stackoverflow.com/questions/3455625/linux-command-to-print-directory-structure-in-the-form-of-a-tree) format.

```sh
├── CONTRIBUTING.md
├── LICENSE
├── Makefile
├── MANIFEST.in
├── module_name.py
├── README.md
├── requirements
│   ├── dev.txt
│   └── prod.txt
├── requirements.txt
├── setup.cfg
├── setup.py
├── tests.py
└── tox.ini
```

## Keywords

Description of each keyword present in the boilerplate project:

* author_name: Full name of the author
* author_email: Author email address
* github_username: GitHub username
* project_name: Short name of your project using [slug style](https://en.wikipedia.org/wiki/Semantic_URL#Slug)
* module_name: Name of the module using [PEP8 style](https://www.python.org/dev/peps/pep-0008/#package-and-module-names)

You can use your preferred text editor or IDE to find the keywords. In [Sublime](https://www.sublimetext.com/) and [Atom](https://atom.io/) this is done by `Ctrl + Shift + F`.
