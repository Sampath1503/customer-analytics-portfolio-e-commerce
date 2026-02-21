---
📈 Customer Lifetime Value (CLV) Analysis & Prediction

🔍 Project Overview

This project predicts future customer value using transactional e-commerce data and converts model outputs into actionable business insights.

Instead of treating all customers equally, the project answers:

> Which customers are most valuable in the future, and where should retention efforts focus?



The solution combines probabilistic modeling, business segmentation, and interactive dashboards to support real-world decision-making.


---

🎯 Business Objectives

Predict 6-month Customer Lifetime Value (CLV)

Identify high-value customers

Detect high-value customers at inactivity risk

Support value-based retention strategies

Present insights in executive-ready dashboards



---

📊 Dataset

Source: E-commerce transactional data

Grain: Customer-level aggregated behavior

Time span: ~12 months of transactions


Key Raw Fields

CustomerID

InvoiceDate

Revenue



---

🧠 Methodology

1️⃣ Feature Engineering

From transaction history, customer-level features were derived:

Frequency – Number of repeat purchases

Recency – Time since last purchase

T – Customer age (observation window)

Monetary Value – Average revenue per transaction


These features align with industry-standard CLV modeling assumptions.


---

2️⃣ CLV Modeling (Probabilistic)

The project uses industry-proven probabilistic models:

🔹 BG/NBD Model

Predicts future purchase frequency

Handles customer inactivity naturally

Suitable for non-contractual businesses


🔹 Gamma-Gamma Model

Predicts expected monetary value

Used only for customers with repeat purchases


🔹 Final Output

Predicted purchases (6 months)

Expected monetary value

6-Month CLV estimate



---

3️⃣ Customer Segmentation

Customers are segmented into:

High Value

Medium Value

Low Value


Segmentation enables:

Focused retention spending

Executive-level prioritization

Clear communication to business users



---

📈 Key Insights

~33% of customers contribute ~88% of total 6-month CLV

High CLV is driven more by customer longevity and repeat behavior than by single large purchases

A small subset of high-value customers shows inactivity risk, requiring immediate retention action



---

📊 Dashboards (Power BI)

Page 1 – CLV Overview

Total Customers

Average CLV

Total CLV (6 months)

CLV contribution by segment


Page 2 – High-Value Customer Deep Dive

Purchase frequency patterns

Recency distribution

Spending behavior

Customer-level CLV table


Page 3 – Actionable CLV Customers

High-value customers needing immediate action

Recency & predicted purchase filters

Top customers driving CLV concentration


📁 Location:

dashboard/
├── CLV_Dashboard.pbix
└── screenshots/


---

🌐 Deployment (Streamlit)

A Streamlit web application was built to make CLV insights accessible to non-technical stakeholders.

Features

Multi-page navigation

CLV segment filters

Actionable customer tables

Business-friendly KPIs


📁 Location:

app/
├── app.py
├── utils.py
└── pages/


---

🗂️ Project Structure

customer-lifetime-value-analysis/
│
├── data/
│   ├── raw/
│   │   └── online_retail_raw.csv
│   └── processed/
│       ├── clv_modeling_dataset.csv
│       └── clv_scoring_dataset.csv
│
├── notebooks/
│   ├── 01_clv_eda.ipynb
│   ├── 02_clv_feature_engineering.ipynb
│   └── 03_clv_modeling.ipynb
│
├── dashboard/
│   ├── CLV_Dashboard.pbix
│   └── screenshots/
│
├── app/
│   ├── app.py
│   ├── utils.py
│   └── pages/
│
├── requirements.txt
└── README.md


---

🛠️ Tech Stack

Python: Pandas, NumPy

Modeling: Lifetimes (BG/NBD, Gamma-Gamma)

Visualization: Power BI

Deployment: Streamlit

Version Control: Git & GitHub



---
