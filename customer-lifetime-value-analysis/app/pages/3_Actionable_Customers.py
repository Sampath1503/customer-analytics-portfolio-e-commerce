import streamlit as st
import plotly.express as px
from utils import load_clv_data

st.header("🚨 Actionable CLV Customers")

@st.cache_data
def get_data():
    return load_clv_data()

df = st.session_state.get("data", get_data())


recency_range = st.sidebar.slider(
    "Recency (days)",
    int(df["recency"].min()),
    int(df["recency"].max()),
    (180, int(df["recency"].max()))
)

pred_range = st.sidebar.slider(
    "Predicted Purchases (6m)",
    float(df["predicted_purchases_6m"].min()),
    float(df["predicted_purchases_6m"].max()),
    (0.0, 5.0)
)

action_df = df[
    (df["recency"] >= recency_range[0]) &
    (df["predicted_purchases_6m"] <= pred_range[1])
]

col1, col2 = st.columns(2)
col1.metric("Customers Needing Action", action_df["CustomerID"].nunique())
col2.metric(
    "CLV Concentration %",
    f"{(action_df['clv_6m'].sum()/df['clv_6m'].sum()*100):.2f}%"
)

st.divider()

fig = px.bar(
    action_df.sort_values("clv_6m", ascending=False).head(10),
    x="CustomerID",
    y="clv_6m",
    title="Top 10 At-Risk High CLV Customers"
)
st.plotly_chart(fig, use_container_width=True)

st.dataframe(
    action_df.sort_values("clv_6m", ascending=False)
)
