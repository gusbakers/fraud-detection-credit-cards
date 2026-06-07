import sys
import os
sys.path.append(os.path.dirname(__file__))

import streamlit as st
import pandas as pd
import numpy as np
import pickle
import shap
import matplotlib.pyplot as plt

from utils.metrics import (
    compute_metrics,
    compute_confusion_matrix,
    compute_fraud_stats
)
from utils.plots import (
    plot_confusion_matrix,
    plot_roc_curve,
    plot_precision_recall,
    plot_fraud_distribution
)

# ─────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────
st.set_page_config(
    page_title="Fraud Detection System",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────────
# PATHS
# ─────────────────────────────────────────
BASE_DIR    = os.path.dirname(os.path.dirname(__file__))
OUTPUTS_DIR = os.path.join(BASE_DIR, "outputs")

# ─────────────────────────────────────────
# LOAD DATA
# ─────────────────────────────────────────
@st.cache_data
def load_predictions() -> pd.DataFrame:
    return pd.read_csv(os.path.join(OUTPUTS_DIR, "predictions.csv"))

@st.cache_data
def load_shap_values() -> pd.DataFrame:
    return pd.read_csv(os.path.join(OUTPUTS_DIR, "shap_values.csv"))

@st.cache_resource
def load_model():
    with open(os.path.join(OUTPUTS_DIR, "best_model.pkl"), "rb") as f:
        return pickle.load(f)

@st.cache_resource
def load_datasets():
    with open(os.path.join(OUTPUTS_DIR, "datasets.pkl"), "rb") as f:
        return pickle.load(f)

# ─────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────
st.sidebar.title("🔍 Fraud Detection")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navegación",
    [
        "📊 Overview",
        "📈 Model Performance",
        "🔎 SHAP Explainability",
        "🚨 Live Predictor"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("**Stack**")
st.sidebar.markdown("""
- Databricks
- MLflow
- LightGBM
- SHAP
- Streamlit
""")
st.sidebar.markdown("---")
st.sidebar.markdown("**Author**")
st.sidebar.markdown("[gusbakers](https://github.com/gusbakers)")

# ─────────────────────────────────────────
# LOAD
# ─────────────────────────────────────────
df      = load_predictions()
df_shap = load_shap_values()
metrics = compute_metrics(df)
cm      = compute_confusion_matrix(df)
stats   = compute_fraud_stats(df)

# ─────────────────────────────────────────
# PAGE 1 — OVERVIEW
# ─────────────────────────────────────────
if page == "📊 Overview":
    st.title("🔍 Fraud Detection System")
    st.markdown("End-to-end fraud detection built on **Databricks** with full **SHAP explainability**.")
    st.markdown("---")

    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Total Transacciones", f"{stats['total']:,}")
    col2.metric("Fraudes Reales",      f"{stats['fraud_real']:,}")
    col3.metric("Fraudes Detectados",  f"{stats['fraud_pred']:,}")
    col4.metric("Fraud Rate",          f"{stats['fraud_rate']:.1%}")
    col5.metric("AUC-ROC",             f"{metrics['auc_roc']:.4f}")

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(
            plot_fraud_distribution(df),
            use_container_width=True
        )
    with col2:
        st.plotly_chart(
            plot_confusion_matrix(cm),
            use_container_width=True
        )

    st.markdown("### 📋 Resumen de Métricas")
    df_metrics = pd.DataFrame({
        "Métrica": ["AUC-ROC", "F1 Score", "Precision", "Recall", "Accuracy"],
        "Score"  : [
            f"{metrics['auc_roc']:.4f}",
            f"{metrics['f1']:.4f}",
            f"{metrics['precision']:.4f}",
            f"{metrics['recall']:.4f}",
            f"{metrics['accuracy']:.4f}",
        ]
    })
    st.dataframe(df_metrics, use_container_width=True)

# ─────────────────────────────────────────
# PAGE 2 — MODEL PERFORMANCE
# ─────────────────────────────────────────
elif page == "📈 Model Performance":
    st.title("📈 Model Performance")
    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("AUC-ROC",   f"{metrics['auc_roc']:.4f}")
    col2.metric("F1 Score",  f"{metrics['f1']:.4f}")
    col3.metric("Precision", f"{metrics['precision']:.4f}")
    col4.metric("Recall",    f"{metrics['recall']:.4f}")

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(plot_roc_curve(df),        use_container_width=True)
    with col2:
        st.plotly_chart(plot_precision_recall(df), use_container_width=True)

    st.plotly_chart(plot_confusion_matrix(cm), use_container_width=True)

    st.markdown("### 🏆 Comparación de Modelos")
    df_compare = pd.DataFrame({
        "Modelo"   : ["Logistic Regression", "Random Forest", "XGBoost", "LightGBM ✅"],
        "AUC-ROC"  : [0.89, 0.93, 0.95, metrics['auc_roc']],
        "F1"       : [0.78, 0.85, 0.88, metrics['f1']],
        "Precision": [0.82, 0.87, 0.90, metrics['precision']],
        "Recall"   : [0.74, 0.83, 0.86, metrics['recall']],
    })
    st.dataframe(
        df_compare.style.highlight_max(
            subset=["AUC-ROC", "F1", "Precision", "Recall"],
            color="lightgreen"
        ),
        use_container_width=True
    )

# ─────────────────────────────────────────
# PAGE 3 — SHAP EXPLAINABILITY
# ─────────────────────────────────────────
elif page == "🔎 SHAP Explainability":
    st.title("🔎 SHAP Explainability")
    st.markdown("Entendiendo **por qué** el modelo toma cada decisión.")
    st.markdown("---")

    datasets      = load_datasets()
    model         = load_model()
    X_test        = datasets["X_test"]
    feature_names = datasets["feature_names"]
    X_test_df     = pd.DataFrame(X_test, columns=feature_names)

    with st.spinner("Calculando SHAP values..."):
        explainer   = shap.TreeExplainer(model)
        shap_values = explainer.shap_values(X_test_df)

    st.markdown("### 📊 Summary Plot")
    st.markdown("Impacto de cada feature en todas las predicciones.")
    fig, ax = plt.subplots()
    shap.summary_plot(shap_values, X_test_df, show=False)
    st.pyplot(fig)
    plt.clf()

    st.markdown("### 📊 Feature Importance")
    fig2, ax2 = plt.subplots()
    shap.summary_plot(shap_values, X_test_df, plot_type="bar", show=False)
    st.pyplot(fig2)
    plt.clf()

    st.markdown("### 🔍 Análisis de Transacción Individual")
    idx     = st.slider("Selecciona una transacción", 0, len(X_test_df) - 1, 0)
    y_pred  = model.predict(X_test)
    y_probs = model.predict_proba(X_test)[:, 1]

    col1, col2 = st.columns(2)
    col1.metric("Probabilidad Fraude", f"{y_probs[idx]:.2%}")
    col2.metric("Predicción", "🚨 FRAUDE" if y_pred[idx] == 1 else "✅ LEGÍTIMO")

    df_force = pd.DataFrame({
        "Feature"      : feature_names,
        "SHAP Value"   : shap_values[idx],
        "Feature Value": X_test_df.iloc[idx].values
    }).sort_values("SHAP Value", ascending=False)

    st.dataframe(
        df_force.style.background_gradient(
            subset=["SHAP Value"],
            cmap="RdYlGn"
        ),
        use_container_width=True
    )

# ─────────────────────────────────────────
# PAGE 4 — LIVE PREDICTOR
# ─────────────────────────────────────────
elif page == "🚨 Live Predictor":
    st.title("🚨 Live Fraud Predictor")
    st.markdown("Ingresa los datos de una transacción para predecir si es fraude.")
    st.markdown("---")

    model         = load_model()
    datasets      = load_datasets()
    feature_names = datasets["feature_names"]

    st.markdown("### 📝 Datos de la Transacción")

    col1, col2, col3 = st.columns(3)
    with col1:
        amount = st.number_input("Monto ($)", min_value=0.0, value=500.0)
        hour   = st.slider("Hora del día", min_value=0, max_value=23, value=14)
    with col2:
        v1 = st.number_input("V1", value=0.0)
        v2 = st.number_input("V2", value=0.0)
    with col3:
        v3 = st.number_input("V3", value=0.0)
        v4 = st.number_input("V4", value=0.0)

    st.markdown("---")

    if st.button("🔍 Predecir", type="primary"):

        input_data = np.zeros((1, len(feature_names)))
        input_df   = pd.DataFrame(input_data, columns=feature_names)

        if "Amount" in feature_names: input_df["Amount"] = amount
        if "hour"   in feature_names: input_df["hour"]   = hour
        if "V1"     in feature_names: input_df["V1"]     = v1
        if "V2"     in feature_names: input_df["V2"]     = v2
        if "V3"     in feature_names: input_df["V3"]     = v3
        if "V4"     in feature_names: input_df["V4"]     = v4

        prob = model.predict_proba(input_df)[0][1]
        pred = model.predict(input_df)[0]

        st.markdown("---")
        st.markdown("### 🎯 Resultado")

        if pred == 1:
            st.error(f"🚨 FRAUDE DETECTADO — Probabilidad: {prob:.2%}")
        else:
            st.success(f"✅ TRANSACCIÓN LEGÍTIMA — Probabilidad de fraude: {prob:.2%}")

        with st.spinner("Calculando explicación..."):
            explainer = shap.TreeExplainer(model)
            shap_vals = explainer.shap_values(input_df)

        st.markdown("### 🔍 ¿Por qué tomó esta decisión?")
        df_explain = pd.DataFrame({
            "Feature"   : feature_names,
            "SHAP Value": shap_vals[0],
        }).sort_values("SHAP Value", ascending=False).head(10)

        st.dataframe(
            df_explain.style.background_gradient(
                subset=["SHAP Value"],
                cmap="RdYlGn"
            ),
            use_container_width=True
        )
