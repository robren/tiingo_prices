#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'tiingo',
    'pandas'
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='tiingo_prices',
    version='0.1.0',
    description="A CLI tool to get close of day prices from tiingo",
    long_description=readme + '\n\n' + history,
    author="Robert Rennison",
    author_email='rob@robren.net',
    url='https://github.com/robren/tiingo_prices',
    packages=[
        'tiingo_prices',
    ],
    package_dir={'tiingo_prices':
                 'tiingo_prices'},
    entry_points={
        'console_scripts': [
            'tiingo_prices=tiingo_prices.tiingo_prices:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='tiingo_prices',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
