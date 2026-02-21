import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Customer Lifetime Value Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

from pathlib import Path

@st.cache_data
def load_data():
    BASE_DIR = Path(__file__).resolve().parent.parent
    data_path = BASE_DIR / "data" / "processed" / "clv_scoring_dataset.csv"
    return pd.read_csv(data_path)

df = load_data()

st.title("📊 Customer Lifetime Value (CLV) Dashboard")
st.markdown(
    """
    This dashboard presents **6-month Customer Lifetime Value predictions**
    using BG/NBD and Gamma-Gamma models to support
    **retention, segmentation, and revenue optimization decisions**.
    """
)

st.markdown("### 👉 Use the left sidebar to navigate between sections.")
