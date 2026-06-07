import pandas as pd
import numpy as np
from sklearn.metrics import (
    accuracy_score, f1_score,
    roc_auc_score, precision_score,
    recall_score, confusion_matrix
)

def compute_metrics(df: pd.DataFrame) -> dict:
    return {
        "auc_roc"   : roc_auc_score(df["y_true"], df["fraud_probability"]),
        "f1"        : f1_score(df["y_true"], df["y_pred"]),
        "precision" : precision_score(df["y_true"], df["y_pred"]),
        "recall"    : recall_score(df["y_true"], df["y_pred"]),
        "accuracy"  : accuracy_score(df["y_true"], df["y_pred"]),
    }

def compute_confusion_matrix(df: pd.DataFrame) -> np.ndarray:
    return confusion_matrix(df["y_true"], df["y_pred"])

def compute_fraud_stats(df: pd.DataFrame) -> dict:
    total      = len(df)
    fraud_real = int(df["y_true"].sum())
    fraud_pred = int(df["y_pred"].sum())
    fraud_rate = fraud_real / total
    return {
        "total"      : total,
        "fraud_real" : fraud_real,
        "fraud_pred" : fraud_pred,
        "fraud_rate" : fraud_rate,
        "legit_total": total - fraud_real,
    }
