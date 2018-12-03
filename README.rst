===============================
tiingo_prices
===============================


.. image:: https://img.shields.io/pypi/v/tiingo_prices.svg
        :target: https://pypi.python.org/pypi/tiingo_prices

.. image:: https://img.shields.io/travis/robren/tiingo_prices.svg
        :target: https://travis-ci.org/robren/tiingo_prices

.. image:: https://readthedocs.org/projects/tiingo-prices/badge/?version=latest
        :target: https://tiingo-prices.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/robren/tiingo_prices/shield.svg
     :target: https://pyup.io/repos/github/robren/tiingo_prices/
     :alt: Updates


A CLI tool to get close of day prices from tiingo


* Free software: MIT license


Features
--------

* Uses the tiingo python API to obtain most recent closing prices for a number
  of tickers. The tickers being specified in a text file, one ticker per line.
* Last years dividends are also obtained anc calculated for each ticker.
* Output is either written to stdout or to a specified file. Output is written in csv
  format with Ticker,Price,Dividend

Installation
------------

This is not commited to pypi so the best way of installing is to:

- Git clone the repo
- Optional:  Create a virtual environment if desired.
- Install locally with 
  
.. code:: bash

   pip install --user -e .


Usage
-----

Set the environment variable TIINGO_API_KEY to the API key associated with your
tiingo account.  For these close of day prices and divdends the API key
provided with the free "starter" account will work. 

$ tiingo_prices -h
usage: tiingo_prices [-h] [--output_file OUTPUT_FILE] [--version] ticker_file

Returns the most recent closing prices and last years dividends for stocks

positional arguments:
  ticker_file           Ticker file name: One ticker per line

optional arguments:
  -h, --help            show this help message and exit
  --output_file OUTPUT_FILE
                        Output file name: Default writes to stdout
  --version             show program's version number and exit



Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

