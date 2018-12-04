import argparse
from datetime import datetime
import os
import sys

# pip install tiingo first
from tiingo import TiingoClient


def main():
    parser = argparse.ArgumentParser(description="Returns the most recent \
                closing prices and last years dividends for stocks")
    parser.add_argument('ticker_file', type=str,
                        help='Ticker file name: One ticker per line',)
    parser.add_argument('--output_file', type=str,
                        help='Output file name: Default writes to stdout')
    parser.add_argument('--version', action='version', version='0.2.0')
    args = parser.parse_args()
    out_file = args.output_file

    if out_file:
        if os.path.isfile(out_file):
            overwrite = yes_or_no('File {} exists, do you wish to overwrite it:'
                                  .format(out_file))
            if (overwrite is False):
                print('Aborting')
                sys.exit()

    if ('TIINGO_API_KEY' not in os.environ):
        print('Please set the TIINGO_API_KEY environment variable.')
        sys.exit()

    tiingo_key = os.environ['TIINGO_API_KEY']
    # print('TIINGO_API_KEY is set to {}'.format(tiingo_key))

    prices = get_prices(args.ticker_file, tiingo_key)

    if out_file:
        with open(args.output_file, 'w') as fh:
            for ticker, price, div in prices:
                fh.write(ticker + ',' + str(price) + ',' + str(div) + '\n')
    else:
        for ticker, price, div in prices:
            sys.stdout.write(ticker + ',' + str(price) + ',' + str(div) + '\n')


def get_prices(ticker_file, tiingo_key):

    """Obtains close of day prices for each ticker..
    Uses the tiingo API to retrive the price for tickers which are
     specified in the ticker_file.

    https://media.readthedocs.org/pdf/tiingo-python/latest/tiingo-python.pdf

    Args:
        ticker_file: A file with a ticker per line.
        tiingo_key: The tiingo API authentiaction key. End of day pricing data
        was free as of the time of writing Nov 2018.
    Returns:
        A list of tupless. Each tuple consisting of:
            - Ticker a string
            - Price a float

    """

    prices = []
    config = {}
    config['session'] = True
    config['api_key'] = tiingo_key

    # Calculate beginning and end of last year
    cur_year = datetime.today().strftime('%Y')
    last_year = str(int(cur_year) -1)
    start_date = last_year + '-' + '01' + '-' + '01'
    end_date = last_year + '-' + '12' + '-' + '31'


    client = TiingoClient(config)

    with open(ticker_file) as t_file:
        for line in t_file:  # Each line contains a ticker
            ticker = line.strip()

            try:
                price = client.get_ticker_price(ticker)
                ly_hist = client.get_dataframe(tickers=ticker, frequency='daily',
                                               startDate=start_date, endDate=end_date)
                tot_divs = ly_hist['divCash'].sum()
                print("Ticker = {} Price  = {} Divs = {:.2f}".format(ticker, price[0]['close'], tot_divs))
                prices.append((ticker, price[0]['adjClose'], round(tot_divs,3)))
            except Exception as ex:
                template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                message = template.format(type(ex).__name__, ex.args)
                print(message)
                print('tingo did not find {}'.format(ticker))
    return prices


def yes_or_no(question):
    reply = str(input(question+' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return True
    if reply[0] == 'n':
        return False
    else:
        return False

if __name__ == '__main__' :
    main()
