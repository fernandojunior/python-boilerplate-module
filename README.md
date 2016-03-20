# python-boilerplate-module

A boilerplate to create a Python module based project. [Clone](https://help.github.com/articles/cloning-a-repository/   ) or [download](https://github.com/fernandojunior/python-boilerplate-module/archive/master.zip) it.

* Author: [@fernandojunior](https://github.com/fernandojunior/)
* GitHub repository: [python-boilerplate-module](https://github.com/fernandojunior/python-boilerplate-module)
* Free software: [The MIT License](/LICENSE)

## Features
*Preconfigured tools to facilitate the project development.*

* [setuptools](https://pythonhosted.org/setuptools/setuptools.html) - Easily download, build, install, upgrade, and uninstall distribution packages.
* [Flake8](https://flake8.readthedocs.org/) - The modular source code checker: pep8, pyflakes and co.
* [pytest](http://pytest.org/) - A mature full-featured Python testing tool.
* [tox](https://tox.readthedocs.org/) - Builds and tests distribution packages in multiple Python versions using isolated and configurable environments.
* [coverage.py](https://coverage.readthedocs.org/) - Code coverage measurement.

## Glossary
*Terms to understand the capabilities offered by the boilerplate.*

* `dependency` - A `distribution package` that is required to `build`, install and use a `project`.
* `build` - Refers to preparing a project in a `distribution package` that users can install and use easily.
* `distribution package` - A archive file with `packages`, `modules` or other resources used to distribute a `release`.
* `module` - A .py file that serves as a unit of Python source code which can expose variables, functions and classes.
* `package` - A directory containing an \_\_init\_\_.py file and which can contain `modules` or recursively, other `packages`.
* `pip` - The preferred package manager system for installing `distribution packages`.
* `project` - A library, framework, script, plugin, application, or other resources or some combination thereof.
* `release` - A snapshot of a `project` at a particular point in time, denoted by a version identifier.
* `virtualenv` - A tool to isolate a environment of a `project` and its `dependencies` from a Python installation.

Other nice glossaries at [Python Documentation](https://docs.python.org/3/glossary.html), [Python Packaging User Guide](https://python-packaging-user-guide.readthedocs.org/en/latest/glossary/) and [Setuptools' Documentation](http://pythonhosted.org/setuptools/pkg_resources.html).

## Structure
*Structure of the project in [tree](http://stackoverflow.com/questions/3455625/linux-command-to-print-directory-structure-in-the-form-of-a-tree) format.*

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
*Description of each keyword of the boilerplate.*

* author_name - Full name of the author.
* author_email - Author email address.
* github_username - GitHub username.
* project_name - Short name of your project using [slug style](https://en.wikipedia.org/wiki/Semantic_URL#Slug).
* module_name - Name of the module using [PEP8 style](https://www.python.org/dev/peps/pep-0008/#package-and-module-names).

You can use your preferred text editor or IDE to find the keywords. In [Sublime](https://www.sublimetext.com/) and [Atom](https://atom.io/) this is done by `Ctrl + Shift + F`.
