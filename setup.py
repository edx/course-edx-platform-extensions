#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='course-edx-platform-extensions',
    version='4.0.0',
    description='Course metadata management extension for edX platform',
    long_description=open('README.rst').read(),
    author='edX',
    url='https://github.com/edx-solutions/course-edx-platform-extensions.git',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Django>=2.2,<2.3",
    ],
)
