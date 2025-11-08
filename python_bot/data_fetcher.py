import yfinance as yf
import pandas as pd

class DataFetcher:
    def __init__(self, ticker="SPY"):
        self.ticker = ticker

    def fetch_historical(self, period="1y", interval="1d"):
        data = yf.download(self.ticker, period=period, interval=interval)
        data.reset_index(inplace=True)
        return data

    def fetch_recent(self, period="5d", interval="1m"):
        data = yf.download(self.ticker, period=period, interval=interval)
        data.reset_index(inplace=True)
        return data
