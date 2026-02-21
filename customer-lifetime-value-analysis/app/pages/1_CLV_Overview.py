import plotly.express as px
import streamlit as st
from utils import load_clv_data

df = load_clv_data()

st.header("📈 CLV Overview")

segment = st.multiselect(
    "CLV Segment",
    options=df["CLV Segment"].unique(),
    default=df["CLV Segment"].unique()
)

filtered_df = df[df["CLV Segment"].isin(segment)]

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Customers", filtered_df["CustomerID"].nunique())
col2.metric("Average CLV", f"₹ {filtered_df['clv_6m'].mean():.2f}")
col3.metric("Total CLV", f"₹ {filtered_df['clv_6m'].sum():,.2f}")
col4.metric(
    "High Value %",
    f"{(filtered_df['CLV Segment'].eq('High Value').mean() * 100):.2f}%"
)

clv_contrib = (
    filtered_df
    .groupby("CLV Segment", as_index=False)["clv_6m"]
    .sum()
)

fig_contrib = px.bar(
    clv_contrib,
    x="clv_6m",
    y="CLV Segment",
    orientation="h",
    text=clv_contrib["clv_6m"].round(2),
    title="CLV Contribution by Segment (6 Months)",
    labels={"clv_6m": "Total CLV (₹)"}
)

fig_contrib.update_traces(textposition="outside")
fig_contrib.update_layout(height=350)

st.plotly_chart(fig_contrib, use_container_width=True)

avg_clv = (
    filtered_df
    .groupby("CLV Segment", as_index=False)["clv_6m"]
    .mean()
)

fig_avg = px.bar(
    avg_clv,
    x="CLV Segment",
    y="clv_6m",
    text=avg_clv["clv_6m"].round(2),
    title="Average CLV by Segment",
    labels={"clv_6m": "Average CLV (₹)"}
)

fig_avg.update_traces(textposition="outside")
fig_avg.update_layout(height=350)

st.plotly_chart(fig_avg, use_container_width=True)

# ---------------- CUSTOMER MIX BY CLV SEGMENT (%) ----------------

segment_counts = (
    filtered_df
    .groupby("CLV Segment", as_index=False)["CustomerID"]
    .nunique()
    .rename(columns={"CustomerID": "Customers"})
)

segment_counts["Percentage"] = (
    segment_counts["Customers"] / segment_counts["Customers"].sum() * 100
).round(2)

fig_mix = px.bar(
    segment_counts,
    x="Percentage",
    y="CLV Segment",
    orientation="h",
    text=segment_counts["Percentage"].astype(str) + "%",
    color="CLV Segment",
    color_discrete_map={
        "High Value": "#1f77b4",
        "Medium Value": "#ff7f0e",
        "Low Value": "#d62728"
    },
    title="Customer Mix by CLV Segment (%)"
)

fig_mix.update_layout(
    xaxis_title="Percentage of Customers",
    yaxis_title="CLV Segment",
    showlegend=False,
    height=350
)

fig_mix.update_traces(textposition="outside")

st.plotly_chart(fig_mix, use_container_width=True)

st.caption(
    "Insight: A smaller proportion of high-value customers contributes a disproportionately large share "
    "of total predicted CLV, indicating strong retention leverage."
)
