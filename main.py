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


if streamlit.button('Search'):

    # Ticker Information
    prev_query = user_input
    ticker_data = yfinance.Ticker(user_input.upper())
    ticker_history = ticker_data.history(period = '1d', start=start_date, end=end_date)

    string_logo = '<img src=%s>' % ticker_data.info['logo_url']
    streamlit.markdown(string_logo, unsafe_allow_html=True)

    string_name = ticker_data.info['longName']
    streamlit.header('**%s**' % string_name)

    string_summary = ticker_data.info['longBusinessSummary']
    streamlit.info(string_summary)

    # Ticker Data
    streamlit.header('**Ticker data**')
    streamlit.write(ticker_data)

    # Bollinger bands
    streamlit.header('**Bollinger Bans**')
    qf = cufflinks.QuantFig(ticker_data)
    qf.add_bollinger_bands()
    fig = qf.iplot(asFigure=True)
    streamlit.plotly_chart(fig)









