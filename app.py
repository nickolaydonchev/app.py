import streamlit as st
import pandas as pd

st.set_page_config(page_title="Shipping AI Terminal", layout="wide")

st.title("🚢 Shipping AI Trading Terminal")

data = pd.DataFrame({
    "Route": ["TD3 AG-CHINA", "TD20 WAF-UKCONT", "TD15 WAF-CHINA", "TD9 CARRIBS"],
    "WS": [76, 101, 74, 145],
    "Change": [3, 2, -1, 1]
})

st.subheader("📊 Market Overview")
st.dataframe(data)

st.subheader("🚨 Alerts")

for _, row in data.iterrows():
    if row["Change"] > 2:
        st.write(f"🚀 {row['Route']} breakout (+{row['Change']})")
    elif row["Change"] < -2:
        st.write(f"🔻 {row['Route']} breakdown")

st.subheader("🎯 Top Signals")

sorted_data = data.sort_values("Change", ascending=False)

for _, row in sorted_data.iterrows():
    st.write(f"{row['Route']} → {row['Change']}")

st.success("✅ SYSTEM LIVE")
