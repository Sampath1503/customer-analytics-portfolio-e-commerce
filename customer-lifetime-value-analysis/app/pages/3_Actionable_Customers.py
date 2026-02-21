import streamlit as st
import plotly.express as px
from utils import load_clv_data

# --------------------------------------------------
# PAGE HEADER
# --------------------------------------------------
st.header("🚨 Actionable CLV Customers")

# --------------------------------------------------
# LOAD DATA (CACHED)
# --------------------------------------------------
@st.cache_data
def get_data():
    return load_clv_data()

df = st.session_state.get("data", get_data())

# --------------------------------------------------
# SIDEBAR FILTERS
# --------------------------------------------------
recency_range = st.sidebar.slider(
    "Recency (days)",
    int(df["recency"].min()),
    int(df["recency"].max()),
    (180, int(df["recency"].max()))
)

pred_range = st.sidebar.slider(
    "Predicted Purchases (6 months)",
    float(df["predicted_purchases_6m"].min()),
    float(df["predicted_purchases_6m"].max()),
    (0.0, 5.0)
)

# --------------------------------------------------
# FILTER ACTIONABLE CUSTOMERS
# --------------------------------------------------
action_df = df[
    (df["recency"] >= recency_range[0]) &
    (df["predicted_purchases_6m"] <= pred_range[1])
].copy()

# --------------------------------------------------
# BUSINESS LOGIC
# --------------------------------------------------
RETENTION_COST = 500  # assumed cost per customer (₹)

action_df["Retention_Cost"] = RETENTION_COST
action_df["Net_Value"] = action_df["clv_6m"] - RETENTION_COST
action_df["Worth_Saving"] = action_df["Net_Value"] > 0

def recommend_action(row):
    if row["recency"] > 300 and row["clv_6m"] > 3000:
        return "🔥 VIP Win-Back (Call + Incentive)"
    elif row["recency"] > 300:
        return "📧 Reactivation Email"
    elif row["predicted_purchases_6m"] < 1:
        return "🎯 Personalized Discount"
    else:
        return "📦 Loyalty Reward"

action_df["Recommended Action"] = action_df.apply(recommend_action, axis=1)

# --------------------------------------------------
# EXECUTIVE SUMMARY MODE
# --------------------------------------------------
exec_mode = st.toggle("🧠 Executive Summary Mode", value=False)

# --------------------------------------------------
# KPI METRICS
# --------------------------------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Customers Needing Action", action_df["CustomerID"].nunique())
col2.metric(
    "Customers Worth Saving",
    action_df[action_df["Worth_Saving"]].shape[0]
)
col3.metric(
    "Potential Revenue at Risk (₹)",
    f"{action_df[action_df['Worth_Saving']]['clv_6m'].sum():,.0f}"
)
col4.metric(
    "CLV Concentration %",
    f"{(action_df['clv_6m'].sum() / df['clv_6m'].sum() * 100):.2f}%"
)

# --------------------------------------------------
# EXECUTIVE VIEW
# --------------------------------------------------
if exec_mode:
    st.success("""
### Executive Summary
- Identified high-CLV customers showing churn risk
- Prioritized customers where retention ROI is positive
- Estimated potential revenue exposure if no action is taken
- Generated customer-level action recommendations
""")

# --------------------------------------------------
# DETAILED ANALYSIS VIEW
# --------------------------------------------------
else:
    st.divider()

    # ---------- TOP 10 AT-RISK CUSTOMERS ----------
    st.subheader("🏆 Top 10 At-Risk High-CLV Customers")

    top10 = action_df.sort_values("clv_6m", ascending=False).head(10)

    fig = px.bar(
        top10,
        x="clv_6m",
        y="CustomerID",
        orientation="h",
        text=top10["clv_6m"].round(0),
        labels={"clv_6m": "Predicted CLV (₹)", "CustomerID": "Customer ID"},
        title="Top 10 Customers Requiring Immediate Action"
    )

    fig.update_layout(
        height=450,
        xaxis_tickprefix="₹",
        yaxis=dict(autorange="reversed"),
        showlegend=False
    )

    fig.update_traces(textposition="outside")

    st.plotly_chart(fig, use_container_width=True)

    # ---------- PRIORITIZED ACTION TABLE ----------
    st.subheader("📋 Prioritized Action List")

    display_cols = [
        "CustomerID",
        "clv_6m",
        "recency",
        "predicted_purchases_6m",
        "Retention_Cost",
        "Net_Value",
        "Recommended Action"
    ]

    st.dataframe(
        action_df[action_df["Worth_Saving"]]
        .sort_values("clv_6m", ascending=False)[display_cols],
        use_container_width=True
    )

    # ---------- EXPORT ----------
    st.download_button(
        label="⬇️ Download Actionable Customer List",
        data=action_df.sort_values("clv_6m", ascending=False).to_csv(index=False),
        file_name="actionable_customers.csv",
        mime="text/csv"
    )
