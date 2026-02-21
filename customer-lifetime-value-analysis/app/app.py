import streamlit as st
import pandas as pd

import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Customer Lifetime Value Intelligence",
    page_icon="💰",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main {
    background-color: #ffffff;
}
.hero-title {
    font-size: 44px;
    font-weight: 800;
    text-align: center;
}
.hero-subtitle {
    font-size: 18px;
    text-align: center;
    color: #555;
    margin-bottom: 30px;
}
.kpi-card {
    padding: 20px;
    border-radius: 12px;
    background: #f8f9fa;
    text-align: center;
    box-shadow: 0px 2px 6px rgba(0,0,0,0.05);
}
.kpi-value {
    font-size: 26px;
    font-weight: 700;
}
.kpi-label {
    color: #666;
}
.section-title {
    font-size: 26px;
    font-weight: 700;
    margin-top: 50px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HERO SECTION ----------------
st.markdown("<div class='hero-title'>💰 Customer Lifetime Value Intelligence</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='hero-subtitle'>Predict • Segment • Monetize customers using probabilistic CLV models</div>",
    unsafe_allow_html=True
)

# ---------------- KPI SECTION ----------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-value">4,372</div>
        <div class="kpi-label">Total Customers</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-value">₹3,240</div>
        <div class="kpi-label">Avg 6-Month CLV</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-value">812</div>
        <div class="kpi-label">High-Value Customers</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-value">₹14.1M</div>
        <div class="kpi-label">Predicted Revenue</div>
    </div>
    """, unsafe_allow_html=True)

# ---------------- HOW IT WORKS ----------------
st.markdown("<div class='section-title'>🔍 How This System Works</div>", unsafe_allow_html=True)

st.markdown("""
1️⃣ **Customer Transaction History**  
2️⃣ **BG/NBD Model** → Predicts purchase frequency  
3️⃣ **Gamma-Gamma Model** → Estimates monetary value  
4️⃣ **6-Month CLV Prediction**  
5️⃣ **Customer Segmentation & Actionable Insights**
""")

# ---------------- BUSINESS IMPACT ----------------
st.markdown("<div class='section-title'>📈 Business Impact</div>", unsafe_allow_html=True)

st.info("""
• Identifies customers worth retaining vs ignoring  
• Optimizes marketing spend using predicted value  
• Improves revenue forecasting and campaign ROI  
• Enables data-driven customer prioritization
""")

# ---------------- TRUST SIGNALS ----------------
st.success("✔ Built using BG/NBD & Gamma-Gamma models | ✔ Deployed on Streamlit Cloud")
st.caption("Dataset: Online Retail (UCI Machine Learning Repository)")

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("## 📊 CLV Analytics Platform")
    st.markdown("Probabilistic modeling for customer value prediction")
    st.divider()
    st.markdown("### Navigate")
    st.markdown("• CLV Overview\n• High Value Analysis\n• Actionable Customers")

from pathlib import Path

@st.cache_data
def load_data():
    BASE_DIR = Path(__file__).resolve().parent.parent
    data_path = BASE_DIR / "data" / "processed" / "clv_scoring_dataset.csv"
    return pd.read_csv(data_path)

df = load_data()
