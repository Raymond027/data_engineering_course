import streamlit as st
from crypto_service import get_crypto_prices
import pandas as pd
import time

st.set_page_config(page_title="Crypto Dashboard", layout="centered")

st.title("📊 Crypto Live Dashboard")

# placeholder for live updates
placeholder = st.empty()

# Control refresh interval (seconds)
REFRSH_INTERVAL = 5


# Keep history for chart
if "btc_history" not in st.session_state:
    st.session_state.history = []

while True:
    data = get_crypto_prices()
    btc_price = data['bitcoin']['usd']
    eth_price = data['ethereum']['usd']

    # store history
    st.session_state.btc_history.append(btc_price)
   
    with placeholder.container():
        st.metric("Bitcoin (BTC)", f"${btc_price:,.3f}")
        st.metric("Etherem (ETH)", f"${eth_price:,.3f}")
   
df = pd.DataFrame(st.session_state.btc_
history, columns = ["BTC Price"])

st.write("Price History:")
st.line_chart(df)
