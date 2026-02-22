# 📊 Customer Analytics Portfolio – Revenue-Focused Retention Intelligence

This repository demonstrates an end-to-end **customer analytics system** for e-commerce, integrating:

* **Customer Churn Risk Prediction**
* **Customer Lifetime Value (CLV) Forecasting**
* **Revenue-at-Risk Executive Prioritization**

The objective is not just prediction — but converting behavioral analytics into **financial decision-making**.

---

# 🎯 Core Business Question

> Which customers should we prioritize to protect future revenue?

This portfolio answers that by combining **risk (churn probability)** and **value (6-month CLV)** into measurable revenue exposure.

---

# 🏗 Portfolio Architecture

```
customer-analytics-portfolio/
│
├── customer-churn-risk-analysis/        # ML-based churn prediction system
├── customer-lifetime-value-analysis/    # Probabilistic CLV forecasting + Streamlit app
├── customer-retention-intelligence/     # Integrated revenue-at-risk dashboard
│
├── requirements.txt
└── README.md
```

---

# 🔴 Project 1 — Customer Churn Risk Prediction

## 🔍 Business Objective

Identify customers likely to disengage within a 90-day inactivity window and prioritize retention actions.

---

## 🧠 Methodology

* Transaction-level aggregation → customer-level dataset
* RFM-style feature engineering
* Behavioral signal extraction
* Logistic Regression classifier
* Class imbalance handling (SMOTE)
* Recall-focused evaluation

---

## 📈 Model Performance

* Accuracy: ~98%
* Recall (Churned Customers): ~87%
* ROC-AUC: ~0.99

> Recall was prioritized to minimize missed churners.

---

## 📊 Deliverables

Power BI dashboard including:

* Executive churn overview
* Risk distribution segmentation
* High-risk customer drill-down

---

## 📌 Insight

Churn risk is concentrated within a limited customer subset, enabling targeted and cost-effective retention intervention.

---

# 🟢 Project 2 — Customer Lifetime Value (6-Month CLV)

## 🔍 Business Objective

Forecast forward-looking customer revenue to prioritize high-impact accounts and optimize marketing allocation.

---

## 🧠 Modeling Framework

* **BG/NBD** → Predict future purchase frequency
* **Gamma-Gamma** → Predict expected transaction value
* Combined to compute 6-month CLV

---

## ⚙ Key Features

* Frequency
* Recency
* Customer age (T)
* Monetary value
* Expected purchases
* Expected monetary value

---

## 📊 Deliverables

* Power BI CLV dashboard
* Customer segmentation (High / Medium / Low Value)
* Deployed Streamlit web application

---

## 📌 Insight

A minority of customers contributes the majority of projected revenue, emphasizing the importance of value-based prioritization.

---

# 🟣 Project 3 — Revenue-at-Risk Executive Dashboard (Integrated Layer)

## 🔍 Business Objective

Quantify projected revenue exposure by combining churn probability with forward-looking CLV.

---

## 🧠 Integration Logic

[
Revenue\ at\ Risk = Churn\ Probability \times CLV_{6M}
]

This transforms behavioral risk into measurable financial exposure.

---

## 📊 Executive Dashboard Highlights

* Total Projected 6-Month CLV
* Total Revenue at Risk
* % Revenue Exposure
* CLV vs Churn Risk distribution
* Revenue exposure by value tier
* Top customers by financial risk

---

## 📌 Strategic Insight

A moderate overall churn rate can still create significant revenue exposure if concentrated among high-value customers.

This dashboard enables:

* Retention budget prioritization
* Financial risk assessment
* Executive-level decision support

---

# 🔗 How the System Works Together

| Component             | Answers                                      |
| --------------------- | -------------------------------------------- |
| Churn Model           | Who is likely to disengage?                  |
| CLV Model             | Who generates the most future value?         |
| Revenue-at-Risk Layer | Where is future revenue financially exposed? |

---

# 🛠 Tech Stack

* Python (Pandas, NumPy, Scikit-learn)
* Lifetimes (BG/NBD, Gamma-Gamma)
* Power BI
* Streamlit
* Git & GitHub

---

# 🚀 Why This Portfolio Matters

This repository demonstrates:

* End-to-end analytics pipeline
* Behavioral feature engineering
* Predictive modeling
* Probabilistic revenue forecasting
* Financial exposure quantification
* Executive dashboard development
* Deployment capability

It mirrors real-world customer analytics workflows in e-commerce environments.

---

# 📌 Future Enhancements

* Revenue uplift modeling
* Churn probability calibration
* Automated retention scoring pipeline
* Campaign impact simulation

---

# 👤 Author

Sampath
Aspiring Data Scientist
Customer Analytics | Churn Modeling | CLV Forecasting | Retention Intelligence

---
