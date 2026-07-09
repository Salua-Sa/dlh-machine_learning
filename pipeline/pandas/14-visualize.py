#!/usr/bin/env python3
"""This module visualizes cryptocurrency data using pandas and matplotlib"""
import matplotlib.pyplot as plt
import pandas as pd
from_file = __import__('2-from_file').from_file

df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')


df = df.drop(columns='Weighted_Price')  # drop column

df = df.rename(columns={"Timestamp": "Date"})  # rename column

df['Date'] = pd.to_datetime(df["Date"], unit="s")  # convert to date

df = df.set_index('Date')  # set index

df['Close'] = df['Close'].ffill()  # fill by deafult previous row

df['High'] = df['High'].fillna(df['Close'])
df['Low'] = df['Low'].fillna(df['Close'])
df['Open'] = df['Open'].fillna(df['Close'])  # fill by same row value

df['Volume_(Currency)'] = df['Volume_(Currency)'].fillna(0)
df['Volume_(BTC)'] = df['Volume_(BTC)'].fillna(0)  # fill missing values by 0

df = df.loc["2017":]  # keep data from 2017

df = df.resample("D").agg({
    "High": "max",
    "Low": "min",
    "Open": "mean",
    "Close": "mean",
    "Volume_(BTC)": "sum",
    "Volume_(Currency)": "sum"})  # resample to daily frequency and aggregate

df.plot()
plt.show()
