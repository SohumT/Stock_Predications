import requests
import time
import tkinter
import pycountry
from forex_python.converter import CurrencyCodes

from bs4 import BeautifulSoup


def get_Price(tickers, country):
    base_url = 'http://google.com/finance/quote/'

    for x in tickers:
        #problem different urls for different markets
        url = base_url + tickers[x] + ":NSE?hl=en&gl=" + country

        page = url.get(url)

        soup = BeautifulSoup(page.content, 'html.parser')

        results = soup.find(class_="YMlKec fxKbKc")

        result = result = results.__str__()

        res = result.split(get_currency(country))[1].split("<")[0]


        # Splitting the price from currency symbol & changing string as necessary


def get_currency(code):
    country = pycountry.countries.get(alpha_2=code)
    currency = pycountry.currencies.get(numeric=country.numeric)
    country_codes = CurrencyCodes()
    country_codes.get_symbol(currency.alpha_3)
