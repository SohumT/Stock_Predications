import requests
import time
import tkinter
import pycountry
from forex_python.converter import CurrencyCodes

from bs4 import BeautifulSoup


def get_Price(tickers_arr):
    base_url = 'http://google.com/finance/quote/'

    for x in tickers_arr:
        # problem different urls for different markets
        url = base_url + tickers_arr[x] + ":" + get_Market(tickers_arr[x])

        page = url.get(url)

        soup = BeautifulSoup(page.content, 'html.parser')

        results = soup.find(class_="YMlKec fxKbKc")

        result = results.__str__()

        # Fix- here- maybe can get country from currency symbol or always use USD
        res = result.split("<")[0]

        return res
        # Splitting the price from currency symbol & changing string as necessary


def get_Market(ticker):
    base_url = 'https://www.google.com/search?q='

    url = base_url + ticker

    page = url.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    text = soup.find(class_="EFkvDd")

    result = text.__str__()

    res = result.split(":")[0]

    return res
