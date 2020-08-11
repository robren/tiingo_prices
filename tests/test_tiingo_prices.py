#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_tiingo_prices
----------------------------------

Tests for `tiingo_prices` module.
"""
import os
import subprocess
import pytest


#from tiingo_prices import tiingo_prices
import tiingo_prices


@pytest.fixture
def response():
    """Sample pytest fixture.
    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument.
    """
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string

def test_entrypoint():
    """Is the entrypoint script installed ? (setup.py)"""
    exit_status = os.system('tiingo_prices --help')
    assert exit_status == 0

def test_a_parameter():
    """Does the application accept a parameter"""
    exit_status = os.system('tiingo_prices --version')
    assert exit_status == 0


def test_run_as_a_module():
    """Can this package be run as a python module?"""
    exit_status = os.system('python -m tiingo_prices.tiingo_prices --help')
    assert exit_status == 0

def test_version(capsys):
    """Does the version flag work?"""

    result = subprocess.run(
        [
            "tiingo_prices",
            "--version",
        ],
        check=True,
        text=True,
        capture_output=True
    )
    #Could just do below. But using capys for lols
    #assert "0.3.0" in result.stdout
    # Needed this to get the output to stdout. capsys would not see it otherwise.
    print(result.stdout)
    captured = capsys.readouterr()
    assert "0.3.0" in captured.out
