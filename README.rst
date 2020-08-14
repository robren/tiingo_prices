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


A CLI tool to get a close of day price and annual dividends for a set of
tickers. Uses the tiingo python API.

* Free software: MIT license


Features
--------

* Uses the tiingo python API to obtain most recent closing prices for a number
  of tickers. The tickers being specified in a text file, one ticker per line.
* Last years dividends are also obtained and calculated for each ticker.
* Output is either written to stdout or to a specified file. Output is written in CSV
  format with Ticker,Price,Dividend on each line of the file.

Installation
------------

.. code:: bash

    pip install tiingo_prices

Usage
------

Set the environment variable TIINGO_API_KEY to the API key associated with your
tiingo account.

.. code:: bash

	  export TIINGO_API_KEY='YourTiingoAPIKey'

For these close of day prices and divdends the API key
provided with the free "starter" account will work.

.. code:: bash

	  $ tiingo_prices -h
	  usage: tiingo_prices [-h] [--output_file OUTPUT_FILE] [--nyse_pref][--version] ticker_file

	  Returns the most recent closing prices and last years dividends for stocks

	  positional arguments:
	  ticker_file           Ticker file name: One ticker per line

	  optional arguments:
	  -h, --help            Show this help message and exit.
	  --output_file OUTPUT_FILE
	                        Output file name: Default writes to stdout.
	  --nyse_pref           Attempt to recognize NYSE Preferred ticker symbols
	                        and convert to tiingo friendly format. Warning may
                                produce incorrect results for non NYSE stocks with PR
                                in their ticker name.
	  --version             Show program's version number and exit.

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
