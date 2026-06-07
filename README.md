# 🔍 Credit Card Fraud Detection System

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Snowflake](https://img.shields.io/badge/Snowflake-DWH-29B5E8?logo=snowflake)
![Databricks](https://img.shields.io/badge/Databricks-Community-red?logo=databricks)
![MLflow](https://img.shields.io/badge/MLflow-Tracking-0194E2?logo=mlflow)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green)

> End-to-end machine learning pipeline for detecting fraudulent 
> credit card transactions — built with industry-standard tools 
> across the full data lifecycle.

---

## 📌 Why I Built This

Fraud costs financial institutions billions every year. I wanted 
to build something that goes beyond a basic notebook — a real 
pipeline that handles data ingestion, transformation, model 
training, interpretability and monitoring, the same way it would 
be done in a production environment.

This project covers the full stack: SQL data warehousing in 
Snowflake, ML experimentation in Databricks, experiment tracking 
with MLflow, and a live dashboard anyone can open right now.

---

## 🎯 Results

| Metric | Score |
|--------|-------|
| **AUC-ROC** | **1.0000** |
| **F1 Score** | **0.9988** |
| **Precision** | **0.9990** |
| **Recall** | **0.9987** |
| **Accuracy** | **0.9997** |

---

## 🏗️ Architecture

```
Synthetic Dataset (100,000 transactions)
              ↓
    Snowflake Data Warehouse
    ├── RAW      → data as ingested
    ├── STAGING  → cleaned + feature transforms
    ├── ANALYTICS → ML-ready features
    └── ML_RESULTS → model predictions + metrics
              ↓
    Databricks Community Edition
    ├── EDA → 8 visualizations
    ├── Feature Engineering → SMOTE-Tomek + RobustScaler
    └── Model Training → 4 models compared
              ↓
    MLflow Experiment Tracking
    ├── Parameters logged
    ├── Metrics logged
    └── Models registered
              ↓
    GitHub → code + CI/CD
              ↓
    Streamlit → live public dashboard
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Data Warehouse | Snowflake (Medallion Architecture) |
| ML Platform | Databricks Community Edition |
| Experiment Tracking | MLflow |
| Models | Logistic Regression, Random Forest, XGBoost, LightGBM |
| Interpretability | SHAP |
| Dashboard | Streamlit |
| CI/CD | GitHub Actions |
| Language | Python 3.10 |

---

## 📊 Dataset

Built a synthetic dataset with realistic fraud patterns 
instead of using an anonymized public dataset. This allowed 
full feature interpretability during EDA and modeling.

| Property | Value |
|----------|-------|
| Total transactions | 100,000 |
| Fraud cases | 15,000 (15%) |
| Legitimate cases | 85,000 (85%) |
| Features | 14 interpretable business features |

Features include transaction amount, hour of day, merchant 
category, distance from home, failed attempts, account age, 
and whether the transaction was online or in-person — all 
variables that map directly to real fraud detection logic.

---

## 🔑 Key Technical Decisions

**Why RobustScaler instead of StandardScaler?**
Fraudulent transactions are outliers by definition. RobustScaler 
uses median and IQR instead of mean and standard deviation, 
making it significantly more resistant to extreme values.

**Why SMOTE-Tomek instead of simple oversampling?**
SMOTE generates synthetic minority class samples while Tomek 
Links removes ambiguous boundary samples from the majority 
class. The combination produces a cleaner decision boundary 
and better generalization.

**Why Average Precision as primary metric?**
With imbalanced datasets, accuracy is misleading. A model that 
predicts everything as legitimate would still score 85% accuracy. 
Average Precision measures what actually matters: performance 
on the minority fraud class.

**Why SHAP for interpretability?**
Financial institutions are increasingly required to explain 
AI-driven decisions. SHAP provides instance-level explanations 
showing exactly which features pushed a prediction toward fraud 
or legitimate — making the model auditable.

**Why a Medallion Architecture in Snowflake?**
Separating RAW, STAGING, ANALYTICS and ML_RESULTS layers 
mirrors how data teams structure production pipelines. It 
makes transformations reproducible, auditable and easy to 
extend.

---

## 📁 Project Structure

```
fraud-detection-credit-cards/
├── notebooks/
│   ├── 01_eda/                 ← data loading + 8 EDA visualizations
│   ├── 02_feature_engineering/ ← SMOTE-Tomek, RobustScaler, MI selection
│   ├── 03_modeling/            ← 4 models + MLflow tracking
│   └── 04_evaluation/         ← SHAP interpretability
├── src/
│   └── sql/                   ← Snowflake DDL scripts (run in order)
├── dashboards/
│   └── app.py                 ← Streamlit dashboard
├── tests/                     ← unit tests
├── .github/workflows/         ← CI/CD pipeline
├── requirements.txt
└── .env.example
```

---

## 🚀 Live Dashboard

👉 [Open Dashboard](https://3bp7tg2fe3kqp.streamlit.app)

---

## ⚙️ Setup

**1. Clone the repository**
```bash
git clone https://github.com/gusbakers/fraud-detection-credit-cards.git
cd fraud-detection-credit-cards
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Configure credentials**
```bash
cp .env.example .env
# Fill in your Snowflake credentials
```

**4. Run notebooks in order**
```
notebooks/01_eda/
notebooks/02_feature_engineering/
notebooks/03_modeling/
notebooks/04_evaluation/
```

---

## 👤 Author

**Gustavo Feliz** — [@gusbakers](https://github.com/gusbakers)

Master's in Machine Learning | Cornell Tech  
Data Engineer · ML Engineer · AI Engineer

---

*Built end-to-end as a portfolio project demonstrating 
the full data and ML lifecycle — from raw data ingestion 
to a live deployed dashboard.*
