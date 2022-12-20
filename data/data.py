import pandas as pd
import numpy as np
import yfinance as yf

tickers = [
    "AAPL",
    "MSFT",
    "TSLA",
    "AMZN",
    "GOOG",
    "GOOGL",
    "META",
    "JPM",
    "BAC"
    ]

portfolio = pd.DataFrame()

def get_data(ticker, start_date, end_date):
  try:
    data = yf.download(ticker, start_date, end_date)
    data = data.dropna()
    portfolio[ticker] = data['Adj Close']
  except:
    print("Error retriving data")

start_date = '2015-01-01'
end_date = '2022-11-30'

for ticker in tickers:
  get_data(ticker, start_date, end_date)

portfolio.to_csv('portfolio.csv')

marketcap = pd.DataFrame()
for ticker in tickers:
    print(yf.Ticker(ticker).info)
    print("marketcap: for ticker: ", yf.Ticker(ticker).info['marketCap'],ticker)
    marketcap[ticker] = yf.Ticker(ticker).info['marketCap']

marketcap.to_csv('marketcap.csv')

roe = pd.DataFrame()
for ticker in tickers:
    roe[ticker] = yf.Ticker(ticker).info['trailingEps'] / yf.Ticker(ticker).info['forwardEps']

roe.to_csv('roe.csv')