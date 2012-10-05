#!/usr/bin/env python

import os
from setuptools import setup
import sys

PROJECT = 'testlap'

# Change docs/sphinx/conf.py too!
VERSION = '0.1'

try:
    long_description = open('README.rst', 'rt').read()
except IOError:
    long_description = ''


setup(
    name=PROJECT,
    version=VERSION,

    description='A Python framework to measure and compare the execution speed of different methods in a class.',
    long_description=long_description,

    author='Jelle Smet',
    author_email='development@smetj.net',

    url='https://github.com/smetj/testlap',
    download_url='https://github.com/smetj/molog/tarball/wishbone_based',

    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: Apache Software License',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Intended Audience :: Programmers',
                 ],

    platforms=['Any'],
    packages=['testlap'],
    scripts=[],

    provides=[],
    install_requires=['prettytable'],

    include_package_data=True,
    )
