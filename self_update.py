import requests
import time
import tkinter
from bs4 import BeautifulSoup


def get_Price(tickers, country):
    base_url = 'http://google.com/finance/quote/'

    for x in tickers:

        url = base_url + tickers[x] + ":NSE?hl=en&gl=" + country

        page = url.get(url)

        soup = BeautifulSoup(page.content, 'html.parser')

        results = soup.find(class_="YMlKec fxKbKc")

        result = result = results.__str__()

        # Splitting the price from currency symbol





