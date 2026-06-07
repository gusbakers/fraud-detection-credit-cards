import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import streamlit as st
import pandas as pd
import numpy as np
import pickle
import shap
import matplotlib.pyplot as plt

from dashboards.utils.metrics import (
    compute_metrics,
    compute_confusion_matrix,
    compute_fraud_stats
)
from dashboards.utils.plots import (
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
# PATHS + DEBUG
# ─────────────────────────────────────────
OUTPUTS_DIR = "/mount/src/fraud-detection-credit-cards/outputs"

st.write("📁 Buscando en:", OUTPUTS_DIR)
try:
    st.write("📂 Archivos:", os.listdir(OUTPUTS_DIR))
except Exception as e:
    st.error(f"❌ {e}")
    st.write("📂 Raíz:", os.listdir("/mount/src/fraud-detection-credit-cards/"))
st.stop()
