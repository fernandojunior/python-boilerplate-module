# Contributing

Contributions are welcome, and they are greatly appreciated! Every little bit helps, and credit will always be given.

See [the GitHub guidelines](https://guides.github.com/activities/contributing-to-open-source/) before get started contributing to this project.

## Get started!

Here is how to set up the `project_name` [repository](https://help.github.com/articles/creating-a-new-repository/) for local development.

1. Fork the `project_name` repository on GitHub.

2. [Clone](https://help.github.com/articles/cloning-a-repository/) your repository locally.

  ```sh
  $ git clone git@github.com:your_username/project_name.git
  ```

3.  Configure your repository for local development with [virtualenv](https://virtualenv.pypa.io/) and [pip](https://pip.pypa.io/).

  ```sh
  $ cd project_name/
  $ virtualenv env && source env/bin/activate
  $ pip install -r requirements/dev.txt
  ```

4. Create a branch for local development.

  ```sh
  $ git checkout -b name-of-your-fix-or-feature
  ```

5. Make changes in your repository files locally.

6. When you are done making changes, check that your changes pass [flake8](https://flake8.readthedocs.org/), [pytest](http://pytest.org/), [tox](https://tox.readthedocs.org/) and [coverage.py](https://coverage.readthedocs.org/):

  ```sh
  $ flake8
  $ py.test
  $ tox
  $ coverage run -m py.test && coverage report --show-missing
  ```

  You can run all these commands automatically with `make all`. Run `make help` for more information.

7. Stage the files for the first commit to your repository.

  ```sh
  $ git add .
  # Adds the files in the local repository and stages them for commit.
  # To unstage a file, use 'git reset HEAD YOUR-FILE'.
  ```

8. Commit the files that you've staged in your local repository.

  ```sh
  $ git commit -m 'Your detailed description of your changes.'
  # Commits the tracked changes and prepares them to be pushed to a remote repository.
  ```

9. [Push the changes](https://help.github.com/articles/pushing-to-a-remote/) in your branch created previously.

  ```sh
  $ git push origin name-of-your-fix-or-feature
  ```

10. Submit a [pull request](https://help.github.com/articles/using-pull-requests/) through the GitHub.
