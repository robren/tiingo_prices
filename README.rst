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

usage: tiingo_prices [-h] [--ticker_file TICKER_FILE]
                     [--output_file OUTPUT_FILE] [--version]

optional arguments:
  -h, --help            show this help message and exit
  --ticker_file TICKER_FILE
                        What is the ticker file name, default tickers.txt
  --output_file OUTPUT_FILE
                        What is the output file name, default writes to stdout
  --version             show program's version number and exit




Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

