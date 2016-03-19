# project_name

The awesome project_name project.

* Author: [@github_username](https://github.com/github_username/)
* GitHub repository: [project_name](https://github.com/github_username/project_name/)
* Free software: [The MIT License](/LICENSE)

## Features

* Hello World

## Examples

* Hello World:

  ```sh
  $ python module_name.py
  Hello World
  ```

## Install

TODO

[//]: # (If you want to your users install the project using pip see the setup.py file)
[//]: # (http://python-packaging-user-guide.readthedocs.org/en/latest/distributing/)
[//]: # (http://python-packaging-user-guide.readthedocs.org/en/latest/distributing/#packaging-your-project)
[//]: # (http://python-packaging-user-guide.readthedocs.org/en/latest/distributing/#uploading-your-project-to-pypi)

## Developers

Here is how to set up the `project_name` [repository](https://help.github.com/articles/creating-a-new-repository/) for local development.

1. If you are a contributor, fork the `project_name` repository on GitHub (optional for [collaborators](https://help.github.com/articles/permission-levels-for-a-user-account-repository/)).

  See `CONTRIBUTING.md` for more information.

2. [Clone](https://help.github.com/articles/cloning-a-repository/) your repository locally.

  ```sh
  $ git clone git@github.com:your_username/project_name.git
  ```

3. Make sure your system is up to date.

  ```sh
  # Example for Ubuntu users.
  $ apt-get update
  $ apt-get upgrade
  $ apt-get install -y build-essential
  $ apt-get install -y python2-dev python2-software-properties  # or
  $ apt-get install -y python3-dev python3-software-properties
  ```

4.  Configure your repository for local development with [virtualenv](https://virtualenv.pypa.io/) and [pip](https://pip.pypa.io/).

  ```sh
  $ cd project_name/
  $ virtualenv env
  $ source env/bin/activate
  $ pip install -r requirements/dev.txt
  ```

5. If you are a contributor, create a branch for local development.

  ```sh
  $ git checkout -b name-of-your-fix-or-feature
  ```

6. Make changes in your repository files (`module_name.py`, `tests.py`, `requirements*`, etc.) locally.

7. When you are done making changes, check that your changes pass [flake8](https://flake8.readthedocs.org/), [pytest](http://pytest.org/), [tox](https://tox.readthedocs.org/) and [coverage.py](https://coverage.readthedocs.org/):

  ```sh
  $ flake8
  $ py.test
  $ tox
  $ coverage run -m py.test && coverage report --show-missing
  ```

  You can also try build the project with `python setup.py sdist` that creates a directory called dist and builds a package to install with `pip install package.tar.gz`.

8. Stage the files for the first commit to your repository.

  ```sh
  $ git add .
  # Adds the files in the local repository and stages them for commit.
  # To unstage a file, use 'git reset HEAD YOUR-FILE'.
  ```

7. Commit the files that you've staged in your local repository.

  ```sh
  $ git commit -m "Your detailed description of your changes."
  # Commits the tracked changes and prepares them to be pushed to a remote repository.
  ```

8. [Push the changes](Push the changes in your local repository to GitHub.) in your local repository to GitHub.

  ```sh
  $ git push origin master  # if you are the repository owner or collaborator
  $ git push origin name-of-your-fix-or-feature  # if you are contributor
  # Pushes the changes in your local repository up to the remote repository
  ```

9. If you are a contributor, submit a [pull request](https://help.github.com/articles/using-pull-requests/) through the GitHub.

## Credits

This project was created based on [python-boilerplate-module](https://github.com/fernandojunior/python-boilerplate-module) by [@fernandojunior](https://github.com/fernandojunior/).
