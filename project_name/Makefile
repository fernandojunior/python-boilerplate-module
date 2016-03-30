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
	@echo '  clean-build  Remove build artifacts.'
	@echo '  clean-pyc    Remove Python file artifacts.'
	@echo '  clean-test   Remove test and coverage artifacts.'
	@echo '  coverage     Code coverage measurement.'
	@echo '  deps         Install dependencies.'
	@echo '  env          Create an isolated development environment.'
	@echo '  install      Build and install a local dist package with pip.'
	@echo '  lint         Check code style with flake8.'
	@echo '  test         Run tests quickly with pytest.'
	@echo '  test-all     Run tests in multiple Python versions with tox.'

all: lint test test-all coverage clean-test

build:
	python setup.py egg_info sdist bdist_wheel
	ls -l dist

clean: clean-pyc clean-test clean-build

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

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

coverage:
	coverage erase
	coverage run -m py.test
	coverage report --show-missing
	# coverage html
	# $(BROWSER) htmlcov/index.html

deps:
	test -f requirements.txt && \
	pip install -r requirements.txt || echo "requirements.txt doesn't exists"

env:
	virtualenv env && . env/bin/activate && make deps

install: build
	pip install dist/*.tar.gz

lint:
	flake8 --show-source --verbose --count

test:
	py.test

test-all:
	tox
