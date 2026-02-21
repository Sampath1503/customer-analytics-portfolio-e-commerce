---
# 📊 Customer Analytics Portfolio – E-Commerce

This repository demonstrates **production-style customer analytics** using real transactional data, combining **customer churn risk** and **customer lifetime value (CLV)** to support **retention decision-making**.

The focus is not just modeling — but **turning data into clear business actions** using machine learning, Power BI dashboards, and a deployed Streamlit application.

---

## 🚀 Projects Included

1. **Customer Churn Risk Analysis** (Power BI + Machine Learning)  
2. **Customer Lifetime Value (CLV) Prediction & Actionable Segmentation** (ML + Power BI + Streamlit)

Both projects mirror real industry workflows:  
**data cleaning → modeling → insights → decision-making**

---

## 📁 Repository Structure (High Level)

```

customer-analytics-portfolio/
├── customer-churn-risk-analysis/      # ML + Power BI churn system
├── customer-lifetime-value-analysis/  # CLV modeling + Streamlit app
├── requirements.txt
└── README.md

```

---

## 🔴 Project 1: Customer Churn Risk Analysis

### 🔍 Business Problem
Customer churn leads to direct revenue loss and increased acquisition costs.  
The objective is to identify **high-risk customers early** so that retention actions can be prioritized.

---

### 🧠 Approach
- Transaction-level data aggregation  
- RFM-style behavioral feature engineering  
- Supervised ML classification  
- Risk bucket segmentation for business users  

---

### ⚙️ Key Features Engineered
- Recency (days since last purchase)  
- Purchase frequency  
- Monetary value  
- Customer lifetime (days)  
- Return ratio  
- Purchase velocity  

---

### 🤖 Modeling
- Handled class imbalance using **SMOTE**  
- Models evaluated using **recall-focused metrics**

#### 📈 Model Performance
- **~98% Accuracy**  
- **~87% Recall on churned customers**

> Recall was prioritized to minimize missed churn cases.

---

### 📊 Power BI Dashboard
**Pages included**
1. **Executive Overview**
   - Total customers  
   - Overall churn rate  
   - Risk distribution  

2. **Churn Risk Distribution**
   - Low / Medium / High risk segmentation  
   - Interactive slicers  

3. **High-Risk Customers**
   - Customer-level drill-down  
   - Actionable churn list  

📸 Dashboard screenshots are available in `/dashboard/screenshots/`

> ⚠️ Power BI `.pbix` file is provided for local exploration.  
> Cloud publishing is not used due to organizational email requirements.

---

### 📌 Key Insight
> A small subset of customers accounts for a disproportionate share of churn risk — targeted intervention can significantly reduce revenue leakage.

---

## 🟢 Project 2: Customer Lifetime Value (CLV) Analysis & Prediction

### 🔍 Business Problem
Not all customers are equal.  
This project predicts future customer value to help businesses:
- Prioritize retention budgets  
- Identify high-impact customers  
- Design value-based engagement strategies  

---

### 🧠 Modeling Framework
- **BG/NBD** → Predict future purchase frequency  
- **Gamma-Gamma** → Predict average monetary value  
- Combined to compute **6-month CLV**

---

### ⚙️ Features Used
- Frequency  
- Recency  
- Customer “age” (T)  
- Monetary value  
- Predicted purchases (6 months)  
- Expected monetary value  
- CLV (6 months)  

---

### 📊 Customer Segmentation
Customers are segmented into:
- High Value  
- Medium Value  
- Low Value  

Based on **CLV quantiles**.

---

### 📊 Power BI Dashboards (Screenshots)

**Page 1 – CLV Overview**
- Total customers  
- Average CLV (₹)  
- Total CLV (₹)  
- CLV contribution by segment  

**Page 2 – High-Value Customer Deep Dive**
- Frequency patterns  
- Recency behavior  
- Spending distribution  
- Customer-level exploration  

**Page 3 – Actionable CLV Customers**
- High-CLV customers with inactivity risk  
- Top CLV contributors  
- Action status indicators  

📸 Screenshots available in `/dashboard/screenshots/`

---

## 🚀 Streamlit Deployment

The CLV project is deployed using **Streamlit** to demonstrate real-world usability.

**App Pages**
1. CLV Overview  
2. High-Value Analysis  
3. Actionable Customers  

### ▶️ Run Locally
```

streamlit run app/app.py

```

### 🌐 Deployment Options
- Streamlit Community Cloud (recommended)  
- Hugging Face Spaces  

---

## 🔗 How Churn and CLV Work Together

These projects are intentionally designed to answer one real business question:

### **“Which customers should we save first?”**

| Metric      | Answers |
|------------|---------|
| Churn Risk | Who is likely to leave? |
| CLV        | Who contributes the most value? |

**Business Rule**

> **High CLV + High Churn Risk = Highest Retention Priority**

This mirrors how retention strategy is executed in real e-commerce organizations.

---
