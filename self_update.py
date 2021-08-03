import requests
import time
import tkinter
import pycountry
from forex_python.converter import CurrencyCodes

from bs4 import BeautifulSoup


def get_Price(tickers_arr, market):
    base_url = 'http://google.com/finance/quote/'

    for x in tickers_arr:
        # problem different urls for different markets
        url = base_url + tickers_arr[x] + ":" + market

        page = url.get(url)

        soup = BeautifulSoup(page.content, 'html.parser')

        results = soup.find(class_="YMlKec fxKbKc")

        result = result = results.__str__()

        # Fix- here- maybe can get country from currency symbol or always use USD
        res = result.split("<")[0]

        return res
        # Splitting the price from currency symbol & changing string as necessary
