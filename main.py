import streamlit
import yfinance
import pandas
import cufflinks
import datetime


streamlit.markdown('''

#Stock Price Web App

An interactive application that evaluates the safety of stock investments and shows 
projections of stocks using LTSM

''')

streamlit.write('---')

user_input = streamlit.text_input("Enter Stock Name or Ticker", " ")



