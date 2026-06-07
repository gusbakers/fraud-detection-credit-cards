import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.metrics import roc_curve, auc, precision_recall_curve

def plot_confusion_matrix(cm: np.ndarray) -> go.Figure:
    labels = ["Legítimo", "Fraude"]
    fig = go.Figure(data=go.Heatmap(
        z=cm,
        x=labels,
        y=labels,
        colorscale="Blues",
        text=cm,
        texttemplate="%{text:,}",
        textfont={"size": 18}
    ))
    fig.update_layout(
        title="Confusion Matrix",
        xaxis_title="Predicho",
        yaxis_title="Real",
        height=400
    )
    return fig

def plot_roc_curve(df: pd.DataFrame) -> go.Figure:
    fpr, tpr, _ = roc_curve(df["y_true"], df["fraud_probability"])
    roc_auc     = auc(fpr, tpr)
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=fpr, y=tpr,
        mode="lines",
        name=f"LightGBM (AUC = {roc_auc:.4f})",
        line=dict(color="royalblue", width=2)
    ))
    fig.add_trace(go.Scatter(
        x=[0, 1], y=[0, 1],
        mode="lines",
        name="Random Classifier",
        line=dict(color="gray", dash="dash")
    ))
    fig.update_layout(
        title="ROC Curve",
        xaxis_title="False Positive Rate",
        yaxis_title="True Positive Rate",
        height=400
    )
    return fig

def plot_precision_recall(df: pd.DataFrame) -> go.Figure:
    precision, recall, _ = precision_recall_curve(
        df["y_true"],
        df["fraud_probability"]
    )
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=recall, y=precision,
        mode="lines",
        name="LightGBM",
        line=dict(color="green", width=2)
    ))
    fig.update_layout(
        title="Precision-Recall Curve",
        xaxis_title="Recall",
        yaxis_title="Precision",
        height=400
    )
    return fig

def plot_fraud_distribution(df: pd.DataFrame) -> go.Figure:
    fig = go.Figure()
    fig.add_trace(go.Histogram(
        x=df[df["y_true"] == 0]["fraud_probability"],
        name="Legítimo",
        opacity=0.7,
        marker_color="royalblue"
    ))
    fig.add_trace(go.Histogram(
        x=df[df["y_true"] == 1]["fraud_probability"],
        name="Fraude",
        opacity=0.7,
        marker_color="red"
    ))
    fig.update_layout(
        title="Distribución de Probabilidades",
        xaxis_title="Probabilidad de Fraude",
        yaxis_title="Cantidad",
        barmode="overlay",
        height=400
    )
    return fig
