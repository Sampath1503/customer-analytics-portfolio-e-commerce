---
# 📉 Customer Churn Risk Analysis (E-Commerce)

🔍 Project Overview

This project focuses on identifying customers at risk of churn using historical transaction data and customer behavior features.
The goal is to help businesses prioritize retention efforts, reduce revenue loss, and target high-risk customers effectively.

The final output is a churn risk scoring dataset and an interactive Power BI dashboard designed for business stakeholders.


---

🧠 Business Problem

Customer churn directly impacts revenue and growth. Businesses need to answer:

Which customers are likely to churn?

What behavioral patterns indicate churn risk?

Which customers should be prioritized for retention campaigns?


This project addresses these questions by combining:

Behavioral feature engineering

Predictive modeling

Business-oriented dashboards



---

🗂 Dataset

Source: Online Retail transactional dataset

Granularity: Transaction-level
Time period: ~12 months
Customers: ~4,300 unique customers

Key Raw Fields

CustomerID

InvoiceDate

Quantity

UnitPrice


Engineered Customer-Level Features

Frequency (number of purchases)

Monetary value (total spend)

Average basket value

Recency (days since last purchase)

Customer lifetime

Purchase velocity

Return ratio



---

🛠 Methodology

1️⃣ Data Cleaning & Preparation

Removed cancelled and invalid transactions

Filtered non-positive quantities and prices

Created revenue feature

Aggregated transaction data to customer-level metrics



---

2️⃣ Exploratory Data Analysis (EDA)

Revenue concentration analysis

Customer behavior distribution

Identification of heavy vs light customers

Churn vs active customer comparison



---

3️⃣ Churn Label Definition

Customers were labeled as churned if:

They had no purchases in the last 90 days of the observation window


This converts churn into a binary classification problem.


---

4️⃣ Feature Engineering

Key churn indicators engineered:

Recency

Purchase velocity

Customer lifetime

Return behavior

Spending patterns


Special care was taken to:

Handle division-by-zero cases

Remove data leakage

Ensure model stability



---

5️⃣ Modeling

Multiple models were evaluated.
Logistic Regression was selected due to:

Strong performance

High interpretability

Business-friendly coefficients


Model Performance (Final)

Accuracy: ~98%

ROC-AUC: ~0.99

Recency identified as the strongest churn signal


The model was used to generate churn probabilities for all customers.


---

📊 Dashboard (Power BI)

An interactive Power BI dashboard was created using the churn scoring dataset.

🔹 Page 1 – Executive Overview

Total customers

Churn rate

Active vs churned customers

Overall churn risk summary


🔹 Page 2 – Risk Distribution

Customer distribution by churn risk (Low / Medium / High)

Behavioral comparisons across risk groups


🔹 Page 3 – High-Risk Customers

High-risk customer list

Behavioral indicators

Priority customers for retention actions


📌 This dashboard is designed for decision-makers and marketing teams.


---

🗂 Project Structure

customer-churn-risk-analysis/
│
├── dashboard/
│   ├── Customer_Churn_Risk_Dashboard.pbix
│   ├── Customer_Churn_Risk_Dashboard_e-commerce.pbix
│   └── screenshots/
│       ├── page1_executive_overview.png
│       ├── page2_risk_distribution.png
│       └── page3_high_risk_customers.png
│
├── data/
│   ├── raw/
│   │   └── online_retail_raw.csv
│   └── processed/
│       ├── cleaned_transactions.csv
│       ├── modeling_dataset.csv
│       └── churn_scoring_dataset.csv
│
├── Notebooks/
│   ├── 01_data_cleaning_eda.ipynb
│   ├── 02_customer_behavior_eda.ipynb
│   ├── 03_feature_engineering.ipynb
│   └── 04_modeling_scoring.ipynb
│
└── README.md


---

🧪 Tech Stack

Python

Pandas, NumPy

Scikit-learn

Logistic Regression

Power BI

Matplotlib / Seaborn



---

📌 Key Insights

Recency is the strongest churn predictor

High spenders can still churn if inactive

Churn risk is highly skewed toward a small customer segment

Early identification enables targeted retention strategies



---

🔮 Future Enhancements

Combine churn probability with CLV for revenue-at-risk analysis

Test tree-based models with explainability (SHAP)

Deploy churn scoring via Streamlit for wider accessibility

Add campaign uplift modeling



---

👤 Author

Chintu
Aspiring Data Scientist | Customer Analytics | Churn & CLV Modeling


---

