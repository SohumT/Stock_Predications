import streamlit
import yfinance
import requests
from fuzzywuzzy import process
import pandas
import cufflinks
import datetime

from web_scrape import *

streamlit.markdown('''

#Stock Price Web App

An interactive application that evaluates the safety of stock investments and shows 
projections of stocks using LTSM

''')


streamlit.write('---')

# Search Bar
prev_query = ""
user_input = streamlit.text_input('Please Enter Company Name', '')

# Side bar preferences
start_date = streamlit.sidebar.date_input("Start date", datetime.date(2019, 1, 1))
end_date = streamlit.sidebar.date_input("End date", datetime.date(2021, 1, 31))


def isBlank(myString):
    if myString and myString.strip():
        return False
    return True


if streamlit.button('Search'):
    prev_query = user_input
    ticker_data = yfinance.Ticker(user_input)
    print(ticker_data.info)


