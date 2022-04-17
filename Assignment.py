import pandas as pd
import streamlit as st
import requests
import locale

locale.setlocale(locale.LC_ALL, '')

#st.header('Bitcoin Prices')
st.markdown("<h1 style='text-align: center; color: black;'>Bitcoin Prices</h1>", unsafe_allow_html=True)
days = st.slider('No of days',1,365)

st.markdown("<h4 style='text-align: center; color: black;'>Currency</h1>", unsafe_allow_html=True)
currency = st.radio('',('CAD','USD','INR','GBP'))

st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center}</style>', unsafe_allow_html=True)

payload = {'vs_currency': currency, 'days': days, 'interval':'daily'}
req = requests.get('https://api.coingecko.com/api/v3/coins/bitcoin/market_chart', params=payload)
if req.status_code == 200:
    r = req.json()
    
df = pd.DataFrame(r['prices'], columns= ['Date',currency])
df['Date'] = pd.to_datetime(df['Date'],unit='ms')
df = df.set_index('Date')
average_price = df[currency].mean()
st.line_chart(df[currency])

num = 10000000
print(f"{num:,}")

num = round(average_price,2)
num = f"{num:,}"
val = str(num) + " " + currency
st.markdown("<h4 style='text-align: center; color: black;'>Average Price during this time was " + val + " </h1>", unsafe_allow_html=True)
