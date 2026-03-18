# 🚀 Customer Analytics System – Revenue-Focused Retention Intelligence

## 💡 Business Impact

- ₹197K projected revenue at risk (~27.5% exposure)
- ~33% of customers contribute ~88% of total revenue
- High-value customers with churn risk identified for targeted retention

This system transforms customer behavior into **financial decision-making**, combining churn prediction, CLV forecasting, and revenue-at-risk modeling.

---

## 🎯 Core Business Question

Which customers should we prioritize to protect future revenue?

This project answers that by combining:
- **Risk (Churn Probability)**
- **Value (6-Month CLV)**

→ to quantify **revenue exposure and retention priority**

---

## 🏗 System Architecture

customer-analytics-portfolio/
│
├── customer-churn-risk-analysis/
├── customer-lifetime-value-analysis/
├── customer-retention-intelligence/
│
├── requirements.txt
└── README.md


---

## 🔴 Churn Risk Prediction

Identifies customers likely to disengage within a 90-day window.

### Key Highlights
- ~98% accuracy | ~87% recall on churn class
- Risk segmentation: High / Medium / Low
- Enables targeted retention instead of blanket campaigns

### Output
- Power BI dashboard with risk distribution and customer drill-down

![Churn Risk](customer-churn-risk-analysis/dashboard/screenshots/page2_risk_distribution.png)

### Insight
Churn risk is concentrated within a small subset → enabling focused intervention.

---

## 🟢 Customer Lifetime Value (6-Month CLV)

Predicts future customer value using probabilistic modeling.

### Key Highlights
- ~33% customers contribute ~88% of revenue
- High-value customers identified for prioritization
- CLV driven by longevity and repeat purchase behavior

### Output
- CLV segmentation dashboard (High / Medium / Low value)

![CLV Analysis](customer-lifetime-value-analysis/dashboards/screenshots/page2_high_value_deep_dive_rfm.png)

### Insight
Revenue is highly concentrated → retention should focus on high-value segments.

---

## 🟣 Revenue-at-Risk Intelligence

Combines churn probability with CLV to quantify financial exposure.

### Formula
Revenue at Risk = Churn Probability × CLV (6 Months)

### Key Highlights
- ₹197K projected revenue at risk (~27.5%)
- Identifies high-value customers at financial risk
- Enables retention budget prioritization

### Output
- Executive dashboard linking risk with revenue impact

![Revenue at Risk](customer-retention-intelligence/dashboard/screenshots/executive_view.png)

### Insight
Even moderate churn rates can create high financial impact if concentrated among high-value customers.

---

## 🔗 System Integration

| Component             | Business Question Answered                  |
|---------------------|--------------------------------------------|
| Churn Model         | Who is likely to leave?                    |
| CLV Model           | Who is valuable?                           |
| Revenue-at-Risk     | Where is revenue exposed?                  |

---

## 🛠 Tech Stack

- Python (Pandas, NumPy, Scikit-learn) → Data processing & modeling
- Lifetimes → CLV forecasting (BG/NBD, Gamma-Gamma)
- Power BI → Business dashboards
- Streamlit → Interactive applications
- Git → Version control

---

## 🚀 Why This Project Matters

This project demonstrates the ability to:

- Translate data into financial impact
- Move beyond prediction to decision-making
- Build end-to-end analytics systems
- Support real-world business strategy

This is not just a model — it is a **decision-support system**.

---

## 📌 Future Enhancements

- Revenue uplift modeling
- Churn probability calibration
- Automated retention scoring pipeline
- Campaign impact simulation

---

## 👤 Author

Sampath  
Data Analyst | Customer Analytics | Revenue Intelligence
