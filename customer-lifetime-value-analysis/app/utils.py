import pandas as pd
import streamlit as st

@st.cache_data
def load_clv_data():
    path = "../data/processed/clv_scoring_dataset.csv"
    df = pd.read_csv(path)
    return df

    # Basic safety
    required_cols = {
        "CustomerID",
        "CLV Segment",
        "clv_6m",
        "frequency",
        "recency",
        "monetary_value",
        "predicted_purchases_6m"
    }

    missing = required_cols - set(df.columns)
    if missing:
        st.error(f"Missing columns: {missing}")
        st.stop()

    return df