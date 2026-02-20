import streamlit as st
from utils import load_clv_data

df = load_clv_data()
df = df[df["CLV Segment"] == "High Value"]

st.header("💎 High-Value Customer Deep Dive")

col1, col2, col3 = st.columns(3)
col1.metric("High-Value Customers", df["CustomerID"].nunique())
col2.metric("Average CLV", f"₹ {df['clv_6m'].mean():.2f}")
col3.metric("Total CLV", f"₹ {df['clv_6m'].sum():,.2f}")

st.subheader("Customer Distribution")

st.bar_chart(df["frequency"].value_counts().sort_index())