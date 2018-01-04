#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='course-edx-platform-extensions',
    version='1.0.3',
    description='Course metadata management extension for edX platform',
    long_description=open('README.rst').read(),
    author='edX',
    url='https://github.com/edx-solutions/course-edx-platform-extensions.git',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "django>=1.8",
    ],
)
