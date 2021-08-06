import requests
import time
import tkinter
import pycountry
from forex_python.converter import CurrencyCodes

from bs4 import BeautifulSoup


def get_Price(ticker):
    base_url = 'https://finance.yahoo.com/quote/'

    url = base_url + ticker + '?p=' + ticker

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    # Some problem with the class in the html file- check html file again
    text = soup.find(class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")

    result = text.__str__()

    res = result.split("<")

    print(res)

    return res



