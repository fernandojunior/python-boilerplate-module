"""
Provides details about how to build and install the a package.

For more information:
    https://pythonhosted.org/setuptools/setuptools.html
    https://packaging.python.org/en/latest/distributing.html
    http://python-packaging-user-guide.readthedocs.org/en/latest/distributing/#packaging-your-project
    http://python-packaging-user-guide.readthedocs.org/en/latest/distributing/#uploading-your-project-to-pypi
"""

from setuptools import setup

# Read the README file
with open("README.md") as f:
    README = f.read()

setup(
    name='project_name',
    version='0.0.1',
    author='author_name',
    author_email='author_email',
    url='https://github.com/github_username/project_name',
    license='MIT License',
    description='The awesome project_name project.',
    py_modules=['module_name'],
    long_description=README,
    zip_safe=False,
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]  # see more at https://pypi.python.org/pypi?%3Aaction=list_classifiers
)
