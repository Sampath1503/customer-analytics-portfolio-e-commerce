import streamlit as st
from utils import load_clv_data

df = load_clv_data()
df = df[df["CLV Segment"] == "High Value"]

st.header("🚨 Actionable High-Value Customers")

recency_threshold = st.slider(
    "Recency (days)",
    int(df["recency"].min()),
    int(df["recency"].max()),
    180
)

action_df = df[df["recency"] > recency_threshold]

st.metric("Customers Needing Action", action_df.shape[0])

st.dataframe(
    action_df.sort_values("clv_6m", ascending=False)[
        [
            "CustomerID",
            "clv_6m",
            "predicted_purchases_6m",
            "monetary_value",
            "recency",
            "frequency"
        ]
    ],
    use_container_width=True
)