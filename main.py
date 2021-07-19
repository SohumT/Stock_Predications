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

# Search Bar
prev_query = ""
user_input = streamlit.text_input('Please Enter Company Name', ' ')

# Side bar preferences
start_date = streamlit.sidebar.date_input("Start date", datetime.date(2019, 1, 1))
end_date = streamlit.sidebar.date_input("End date", datetime.date(2021, 1, 31))


def get_symbol(symbol):
    url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(symbol)
    result = requests.get(url).json()

    for x in result['ResultSet']['Result']:
        if x['symbol'] is symbol.upper():
            return x['name']


def get_Company(text):
    r = requests.get('https://api.iextrading.com/1.0/ref-data/symbols')
    stock_list = r.json()
    return process.extract(text, stock_list)


def isBlank(myString):
    if myString and myString.strip():
        return False
    return True


if streamlit.button('Search'):
    prev_query = user_input
    ticker_data = yfinance.Ticker(get_Company(user_input.upper()))
    print(ticker_data.info)


