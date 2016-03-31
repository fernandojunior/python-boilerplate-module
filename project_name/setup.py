'''
Contains informations necessaries to build, release and install a distribution.

For more information:
    https://pythonhosted.org/setuptools/setuptools.html
    https://packaging.python.org/en/latest/distributing.html
    http://python-packaging-user-guide.readthedocs.org/en/latest/distributing/#packaging-your-project
    http://python-packaging-user-guide.readthedocs.org/en/latest/distributing/#uploading-your-project-to-pypi
'''
from setuptools import setup
from pip.req import parse_requirements as parse

# Parse a requirements file to string list
requirements = lambda f: [str(i.req) for i in parse(f, session=False)]

setup(
    name='project_name',
    version='0.0.1',
    author='author_name',
    url='https://github.com/github_username/project_name',
    license='MIT License',
    description='The awesome project_name project.',
    platforms='any',
    py_modules=['module_name'],
    install_requires=requirements('requirements.txt'),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Operating System :: OS Independent',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 3',
    ],  # see more at https://pypi.python.org/pypi?%3Aaction=list_classifiers
    zip_safe=False
)
