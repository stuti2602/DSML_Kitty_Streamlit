"""
# title
import streamlit as st

st.title("This is a basic Webapp")
st.title("_Streamlit_ is :blue[cool] :sunglasses:")

# header

st.header("_Streamlit_ is :blue[cool] :sunglasses:")
st.header("This is a header with a divider", divider="gray")
st.header("These headers have rotating dividers", divider=True)
st.header("One", divider=True)
st.header("Two", divider=True)
st.header("Three", divider=True)
st.header("Four", divider=True)

# subheader

st.subheader("_Streamlit_ is :blue[cool] :sunglasses:")
st.subheader("This is a subheader with a divider", divider="gray")
st.subheader("These subheaders have rotating dividers", divider=True)
st.subheader("One", divider=True)
st.subheader("Two", divider=True)
st.subheader("Three", divider=True)
st.subheader("Four", divider=True)

# checkbox

agree = st.checkbox("I agree with stuti!")

if agree: # if we agree with this value next statement is getting print
    st.write("Great!")

# radio button /(choice option)

st.header("Radio Button")
genre = st.radio(
    "What's your favorite movie genre",
    ["Comedy", "Drama", "Documentary"]
)

if genre == "Comedy":
    st.write("You selected comedy")
else:
    st.write("You didn't selected comedy")
"""

import streamlit as st
import yfinance as yf
import numpy as np
import pandas as pd
import datetime

ticker_symbol = st.text_input("please enter ticker" ,"AAPL")
ticker_data = yf.Ticker(ticker_symbol)

# ask user for the start date and end date input

col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("please enter the starting date", datetime.date(2022, 1, 1))

with col2:
    end_date = st.date_input("please enter the ending date", datetime.date(2023,12,31))

ticker_df = ticker_data.history(period= "1d", start= start_date, end = end_date)

st.title("Stock Price Analyzer!")
st.write("here's the raw day wise stock movement:")
st.dataframe(ticker_df)

st.write("price Movement Over Time ")
st.line_chart(ticker_df["Close"])

st.write("volume over time")
st.line_chart(ticker_df["Volume"])