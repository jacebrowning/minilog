#!/usr/bin/env python

"""Setup script for the package."""

import os
import sys

import setuptools


PACKAGE_NAME = 'log'


def read_package_variable(key, filename='__init__.py'):
    """Read the value of a variable from the package without importing."""
    module_path = os.path.join(PACKAGE_NAME, filename)
    with open(module_path) as module:
        for line in module:
            parts = line.strip().split(' ', 2)
            if parts[:-1] == [key, '=']:
                return parts[-1].strip("'")
    sys.exit("'%s' not found in '%s'", key, module_path)


def build_description():
    """Build a description for the project from documentation files."""
    readme = open("README.md").read()
    changelog = open("CHANGELOG.md").read()
    return readme + '\n' + changelog


setuptools.setup(
    name=read_package_variable('__project__'),
    version=read_package_variable('__version__'),

    description="Minimalistic wrapper for Python logging.",
    url='https://github.com/jacebrowning/minilog',
    author='Jace Browning',
    author_email='jacebrowning@gmail.com',

    packages=setuptools.find_packages(),

    long_description=build_description(),
    long_description_content_type='text/markdown',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python',
        'Topic :: Software Development',
        'Topic :: System :: Logging',
    ],
)
