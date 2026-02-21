import pandas as pd
import streamlit as st

from pathlib import Path

@st.cache_data
def load_clv_data():
    BASE_DIR = Path(__file__).resolve().parent.parent
    data_path = BASE_DIR / "data" / "processed" / "clv_scoring_dataset.csv"
    return pd.read_csv(data_path)

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
