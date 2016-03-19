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
	@echo 'clean - remove all python, test and build artifacts'
	@echo 'clean-pyc - remove Python file artifacts'
	@echo 'clean-test - remove test and coverage artifacts'
	@echo 'clean-build - remove build artifacts'
	@echo 'lint - check style with flake8'
	@echo 'test - run tests quickly with the default Python'
	@echo 'test-all - run tests on every Python version with tox'
	@echo 'coverage - check code coverage quickly with the default Python'
	@echo 'build - create source packages'

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
	python setup.py bdist_wheel
	ls -l dist
