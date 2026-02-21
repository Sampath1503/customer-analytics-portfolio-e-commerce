import streamlit as st
from utils import load_clv_data

df = load_clv_data()
df = df[df["CLV Segment"] == "High Value"]

st.header("💎 High-Value Customer Deep Dive")

col1, col2, col3 = st.columns(3)
col1.metric("High-Value Customers", df["CustomerID"].nunique())
col2.metric("Average CLV", f"₹ {df['clv_6m'].mean():.2f}")
col3.metric("Total CLV", f"₹ {df['clv_6m'].sum():,.2f}")

import plotly.express as px

# ---------------- TOP HIGH-VALUE CUSTOMERS ----------------
st.subheader("🏆 Top 20 High-Value Customers by Predicted CLV")

top_customers = (
    df.sort_values("clv_6m", ascending=False)
      .head(20)
)

fig_top = px.bar(
    top_customers,
    x="clv_6m",
    y="CustomerID",
    orientation="h",
    text=top_customers["clv_6m"].round(2),
    labels={"clv_6m": "Predicted CLV (₹)", "CustomerID": "Customer ID"},
)

fig_top.update_layout(
    height=500,
    xaxis_tickprefix="₹",
    yaxis=dict(autorange="reversed"),
    title="Top 20 Customers Driving Maximum CLV"
)

fig_top.update_traces(textposition="outside")

st.plotly_chart(fig_top, use_container_width=True)

# ---------------- PARETO ANALYSIS ----------------
st.subheader("📈 Pareto Analysis (80/20 Rule)")

pareto_df = df.sort_values("clv_6m", ascending=False).reset_index(drop=True)
pareto_df["Cumulative_CLV"] = pareto_df["clv_6m"].cumsum()
pareto_df["Cumulative_Percentage"] = (
    pareto_df["Cumulative_CLV"] / pareto_df["clv_6m"].sum() * 100
)

fig_pareto = px.line(
    pareto_df,
    y="Cumulative_Percentage",
    labels={"Cumulative_Percentage": "Cumulative CLV (%)"},
)

fig_pareto.add_hline(y=80, line_dash="dash", line_color="red")

fig_pareto.update_layout(
    height=400,
    yaxis_ticksuffix="%",
    title="Cumulative Contribution of High-Value Customers to Total CLV"
)

st.plotly_chart(fig_pareto, use_container_width=True)

st.caption(
    "Insight: A small subset of high-value customers contributes a disproportionate share of total CLV, "
    "highlighting strong opportunities for retention, personalization, and VIP-focused strategies."
)
