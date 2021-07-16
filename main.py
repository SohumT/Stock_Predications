import streamlit
import yfinance
import requests
from fuzzywuzzy import process
import pandas
import cufflinks
import datetime

streamlit.markdown('''

#Stock Price Web App

An interactive application that evaluates the safety of stock investments and shows 
projections of stocks using LTSM

''')

streamlit.write('---')

user_input = streamlit.text_input('Please Enter the Stock Ticker', ' ')


def get_symbol(symbol):
    url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(symbol)
    result = requests.get(url).json()

    for x in result['ResultSet']['Result']:
        if x['symbol'] == symbol:
            return x['name']


def getCompany(text):
    r = requests.get('https://api.iextrading.com/1.0/ref-data/symbols')
    stock_list = r.json()
    return process.extract(text, stock_list)


mod_text = user_input.upper()
ticker_data = yfinance.Ticker(mod_text)


if ticker_data.ticker is not None:
    pass
elif ticker_data is None and yfinance.Ticker(getCompany(mod_text)) is not None:
    print('here')
    ticker_data = yfinance.Ticker(getCompany(mod_text))
elif ticker_data is None and yfinance.Ticker(getCompany(mod_text)) is None:
    print('here')
    streamlit.warning('Please Input a Valid Ticker or Stock Name')


