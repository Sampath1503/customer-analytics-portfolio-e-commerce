import streamlit as st

st.set_page_config(
    page_title="Customer Lifetime Value Dashboard",
    layout="wide"
)

st.sidebar.title("📊 Customer Analytics")
st.sidebar.info(
    "CLV modeling using BG/NBD + Gamma-Gamma\n\n"
    "Built for business decision-making"
)

st.title("📈 Customer Lifetime Value Dashboard")
st.markdown(
    """
    Use the sidebar to navigate between:
    - CLV Overview
    - High-Value Customer Analysis
    - Actionable Customers
    """
)