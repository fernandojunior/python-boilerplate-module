.PHONY: clean-pyc clean-build clean
define BROWSER_PYSCRIPT
import os, webbrowser, sys
try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open('file://' + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT
BROWSER := python -c '$$BROWSER_PYSCRIPT'

help:
	@echo 'Usage: make [command]'
	@echo 'Commands:'
	@echo '  all          Run all test commands. '
	@echo '  build        Build a distribution package with setuptools.'
	@echo '  clean        Remove all Python, test and build artifacts.'
	@echo '  clean-pyc    Remove Python file artifacts.'
	@echo '  clean-test   Remove test and coverage artifacts.'
	@echo '  clean-build  Remove build artifacts.'
	@echo '  coverage     Code coverage measurement.'
	@echo '  deps         Install dependencies.'
	@echo '  env          Create a isolated development environment with its dependencies.'
	@echo '  lint         Check code style with flake8.'
	@echo '  test         Run tests quickly with pytest.'
	@echo '  test-all     Run tests in multiple Python versions with tox.'

env:
	virtualenv env && . env/bin/activate && make deps

deps:
	pip install -r requirements.txt

all: lint test test-all coverage clean-test

clean: clean-pyc clean-test clean-build

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .cache/
	rm -fr .tox/
	rm -fr htmlcov/
	rm -f .coverage

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

lint:
	flake8 --show-source --verbose --count

test:
	py.test

test-all:
	tox

coverage:
	coverage erase
	coverage run -m py.test
	coverage report --show-missing
	# coverage html
	# $(BROWSER) htmlcov/index.html

build:
	# python setup.py egg_info
	python setup.py sdist
	# python setup.py bdist_wheel
	ls -l dist
