import streamlit
import yfinance
import pandas
import cufflinks
import datetime

from web_scrape import *

streamlit.markdown('''

# Stock Price Web App

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


def display_Graph(history):
    # Bollinger bands
    streamlit.header('**Bollinger Bands**')
    qf = cufflinks.QuantFig(ticker_history, title='Quant Figure', legend='top', name='GS')
    qf.add_bollinger_bands()
    fig = qf.iplot(asFigure=True)
    streamlit.plotly_chart(fig)


def display_Stock_Info(ticker):

    string_name = ticker.info['longName']
    streamlit.header('**%s**' % string_name)

    string_logo = '<img src=%s>' % ticker.info['logo_url']
    streamlit.markdown(string_logo, unsafe_allow_html=True)
    streamlit.markdown('''\n''')

    string_summary = ticker.info['longBusinessSummary']
    streamlit.info(string_summary)

    # Ticker Data
    streamlit.header('**Current Stock Price**')
    # stock price data


if streamlit.button('Search'):

    # Ticker Information
    prev_query = user_input
    ticker_data = yfinance.Ticker(user_input.upper())
    ticker_history = ticker_data.history(period='1d', start=start_date, end=end_date)

    if ticker_data.ticker == '':
        streamlit.warning('Stock Ticker or Symbol Not Found. Please Enter the Stock Ticker Again')
    else:
        # Display Stock Components: Logo, Description and Real-Time Stock Price
        display_Stock_Info(ticker_data)

        # Display Graph
        display_Graph(ticker_history)
