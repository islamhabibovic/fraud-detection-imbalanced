"""
================================================================================
COMPARATIVE ANALYSIS OF RESAMPLING TECHNIQUES AND ENSEMBLE METHODS
FOR IMBALANCED CLASSIFICATION:
A CASE STUDY ON CREDIT CARD FRAUD DETECTION
================================================================================

Author:   Islam Habibovic
Course:   Rudarenje podataka (Data Mining)
Semester: Ljetni semestar 2026
Profesor: doc. dr. Adnan Dzelihodzic
Asistent: as. mr. Narcisa Hadzajlic

DATASET
-------
Kartik2112 "Credit Card Transactions Fraud Detection" (Kaggle):
    https://www.kaggle.com/datasets/kartik2112/fraud-detection

Files expected next to this script:
    fraudTrain.csv   (~1.3M rows)
    fraudTest.csv    (~555K rows)

REQUIREMENTS
------------
pip install pandas numpy scikit-learn imbalanced-learn xgboost matplotlib seaborn

This script:
 1. Loads the train/test CSV files.
 2. Performs feature engineering on temporal, geographic and demographic data.
 3. Applies four resampling techniques on the training set only.
 4. Trains Random Forest and XGBoost on each resampled training set.
 5. Evaluates 8 (resampling x model) configurations with six metrics each.
 6. Saves CSV of results and publication-quality figures.
================================================================================
"""
import os
import json
import warnings
from pathlib import Path
from math import radians, sin, cos, asin, sqrt

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    precision_score, recall_score, f1_score,
    roc_auc_score, average_precision_score,
    matthews_corrcoef, confusion_matrix,
    precision_recall_curve, roc_curve,
)
from sklearn.base import clone

from imblearn.over_sampling import RandomOverSampler, SMOTE
from imblearn.combine import SMOTETomek

from xgboost import XGBClassifier

warnings.filterwarnings("ignore")
sns.set_style("whitegrid")
RANDOM_STATE = 42
np.random.seed(RANDOM_STATE)

OUTPUT_DIR = Path(__file__).parent / "results"
OUTPUT_DIR.mkdir(exist_ok=True)
FIG_DIR = OUTPUT_DIR / "figures"
FIG_DIR.mkdir(exist_ok=True)


# =============================================================================
# 1. DATA LOADING
# =============================================================================
def load_data(train_path="fraudTrain.csv", test_path="fraudTest.csv"):
    """Load Kartik2112 fraud dataset from CSV files."""
    print(f"[INFO] Loading {train_path} ...")
    train = pd.read_csv(train_path)
    print(f"[INFO] Loading {test_path} ...")
    test = pd.read_csv(test_path)
    print(f"[INFO] Train shape: {train.shape}, Test shape: {test.shape}")
    return train, test


# =============================================================================
# 2. FEATURE ENGINEERING
# =============================================================================
def haversine(lat1, lon1, lat2, lon2):
    """Compute great-circle distance (km) between two points."""
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2
    return 6371 * 2 * np.arcsin(np.sqrt(a))


def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    """Create useful temporal, demographic and geographic features."""
    df = df.copy()

    # ----- temporal --------------------------------------------------------
    df["trans_date_trans_time"] = pd.to_datetime(df["trans_date_trans_time"])
    df["trans_hour"]     = df["trans_date_trans_time"].dt.hour
    df["trans_day"]      = df["trans_date_trans_time"].dt.day
    df["trans_dayofweek"]= df["trans_date_trans_time"].dt.dayofweek
    df["trans_month"]    = df["trans_date_trans_time"].dt.month

    # ----- age from dob ----------------------------------------------------
    df["dob"] = pd.to_datetime(df["dob"])
    df["age"] = ((df["trans_date_trans_time"] - df["dob"]).dt.days / 365.25).astype(int)

    # ----- geographic distance --------------------------------------------
    df["distance_km"] = haversine(df["lat"], df["long"],
                                  df["merch_lat"], df["merch_long"])

    # ----- drop unused identifier / leakage columns -----------------------
    drop_cols = ["Unnamed: 0", "cc_num", "first", "last", "street",
                 "city", "state", "zip", "dob", "trans_num",
                 "trans_date_trans_time", "unix_time"]
    df = df.drop(columns=[c for c in drop_cols if c in df.columns])

    return df


def encode_categoricals(train: pd.DataFrame, test: pd.DataFrame):
    """Label-encode categorical columns; fit on train, apply on test
    (unseen labels in test mapped to -1 to avoid leakage)."""
    cat_cols = ["merchant", "category", "gender", "job"]
    encoders = {}
    for col in cat_cols:
        le = LabelEncoder()
        train[col] = le.fit_transform(train[col].astype(str))
        # transform test, handling unseen labels
        test_vals = test[col].astype(str)
        test[col] = test_vals.map(lambda v: le.transform([v])[0]
                                  if v in le.classes_ else -1)
        encoders[col] = le
    return train, test, encoders


# =============================================================================
# 3. EDA
# =============================================================================
def perform_eda(train: pd.DataFrame) -> dict:
    """Run quick EDA and save standard plots."""
    counts = train["is_fraud"].value_counts()
    fraud_pct = 100 * counts.get(1, 0) / counts.sum()
    stats = {
        "n_train_rows":   int(len(train)),
        "n_features":     int(train.shape[1] - 1),
        "n_fraud_train":  int(counts.get(1, 0)),
        "n_legit_train":  int(counts.get(0, 0)),
        "fraud_pct":      float(fraud_pct),
        "missing_values": int(train.isnull().sum().sum()),
    }

    # ---- class distribution ----------------------------------------------
    fig, ax = plt.subplots(1, 2, figsize=(12, 4))
    ax[0].bar(["Legitimate", "Fraud"],
              [counts.get(0, 0), counts.get(1, 0)],
              color=["#3498db", "#e74c3c"])
    ax[0].set_title("Class distribution - counts")
    ax[0].set_ylabel("Number of transactions")
    ax[0].set_yscale("log")

    ax[1].bar(["Legitimate", "Fraud"],
              [100 - fraud_pct, fraud_pct],
              color=["#3498db", "#e74c3c"])
    ax[1].set_title("Class distribution - %")
    ax[1].set_ylim(0, 105)
    plt.suptitle("Severe class imbalance", fontweight="bold")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "class_distribution.png", dpi=140)
    plt.close()

    # ---- amount distribution ---------------------------------------------
    plt.figure(figsize=(10, 4))
    plt.hist(train.loc[train["is_fraud"] == 0, "amt"], bins=80,
             color="#3498db", alpha=0.6, label="Legitimate", log=True)
    plt.hist(train.loc[train["is_fraud"] == 1, "amt"], bins=80,
             color="#e74c3c", alpha=0.8, label="Fraud", log=True)
    plt.xlabel("Transaction amount (USD)")
    plt.ylabel("Frequency (log scale)")
    plt.title("Transaction-amount distribution by class")
    plt.legend()
    plt.tight_layout()
    plt.savefig(FIG_DIR / "amount_distribution.png", dpi=140)
    plt.close()

    # ---- fraud rate by hour ----------------------------------------------
    hr = train.groupby("trans_hour")["is_fraud"].mean() * 100
    plt.figure(figsize=(10, 4))
    hr.plot(kind="bar", color="#16a085")
    plt.xlabel("Hour of the day")
    plt.ylabel("Fraud rate (%)")
    plt.title("Fraud rate by hour of transaction")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "fraud_by_hour.png", dpi=140)
    plt.close()

    print("[EDA] train shape: ", train.shape)
    print("[EDA] fraud rate : {:.4f}%".format(fraud_pct))
    return stats


# =============================================================================
# 4. PREPROCESSING
# =============================================================================
def prepare_xy(train, test):
    """Scale numeric columns; return X_train, y_train, X_test, y_test."""
    num_cols = ["amt", "lat", "long", "city_pop", "merch_lat", "merch_long",
                "age", "distance_km", "trans_hour", "trans_day",
                "trans_dayofweek", "trans_month"]

    scaler = StandardScaler()
    train[num_cols] = scaler.fit_transform(train[num_cols])
    test[num_cols]  = scaler.transform(test[num_cols])

    X_train = train.drop("is_fraud", axis=1)
    y_train = train["is_fraud"].values
    X_test  = test.drop("is_fraud", axis=1)[X_train.columns]   # same order
    y_test  = test["is_fraud"].values
    return X_train, y_train, X_test, y_test


# =============================================================================
# 5. RESAMPLING + MODELS
# =============================================================================
def get_resamplers():
    return {
        "None (baseline)":   None,
        "RandomOverSampler": RandomOverSampler(random_state=RANDOM_STATE),
        "SMOTE":             SMOTE(random_state=RANDOM_STATE, k_neighbors=5),
        "SMOTE+Tomek":       SMOTETomek(random_state=RANDOM_STATE),
    }


def get_models():
    return {
        "Random Forest": RandomForestClassifier(
            n_estimators=200, max_depth=14, min_samples_split=10,
            n_jobs=-1, random_state=RANDOM_STATE),
        "XGBoost": XGBClassifier(
            n_estimators=300, max_depth=6, learning_rate=0.1,
            subsample=0.9, colsample_bytree=0.9,
            eval_metric="aucpr", use_label_encoder=False,
            random_state=RANDOM_STATE, n_jobs=-1),
    }


def evaluate(y_true, y_pred, y_proba):
    return {
        "Precision":  precision_score(y_true, y_pred, zero_division=0),
        "Recall":     recall_score(y_true, y_pred),
        "F1":         f1_score(y_true, y_pred),
        "AUC-ROC":    roc_auc_score(y_true, y_proba),
        "AUC-PR":     average_precision_score(y_true, y_proba),
        "MCC":        matthews_corrcoef(y_true, y_pred),
    }


# =============================================================================
# 6. EXPERIMENT RUNNER
# =============================================================================
def run_experiments(X_train, y_train, X_test, y_test):
    resamplers = get_resamplers()
    models = get_models()
    results, roc_data, pr_data, cms = [], {}, {}, {}

    for r_name, r_obj in resamplers.items():
        if r_obj is None:
            Xr, yr = X_train, y_train
        else:
            print(f"[RESAMPLE] {r_name} ...")
            Xr, yr = r_obj.fit_resample(X_train, y_train)
        print(f"           -> resampled size {Xr.shape}, "
              f"frauds = {int(np.array(yr).sum())}")

        for m_name, m_obj in models.items():
            print(f"  [MODEL]   {m_name}  on  {r_name}")
            model = clone(m_obj)
            model.fit(Xr, yr)
            y_pred  = model.predict(X_test)
            y_proba = model.predict_proba(X_test)[:, 1]

            metrics = evaluate(y_test, y_pred, y_proba)
            metrics["Resampling"] = r_name
            metrics["Model"] = m_name
            results.append(metrics)

            key = f"{r_name} | {m_name}"
            fpr, tpr, _   = roc_curve(y_test, y_proba)
            prec, rec, _  = precision_recall_curve(y_test, y_proba)
            roc_data[key] = (fpr, tpr, metrics["AUC-ROC"])
            pr_data[key]  = (rec, prec, metrics["AUC-PR"])
            cms[key]      = confusion_matrix(y_test, y_pred)

    return pd.DataFrame(results), roc_data, pr_data, cms


# =============================================================================
# 7. VISUALISATION
# =============================================================================
def plot_results(df_res, roc_data, pr_data, cms):
    metrics = ["Precision", "Recall", "F1", "AUC-ROC", "AUC-PR", "MCC"]
    fig, axes = plt.subplots(2, 3, figsize=(17, 9))
    for ax, m in zip(axes.flatten(), metrics):
        piv = df_res.pivot(index="Resampling", columns="Model", values=m)
        piv = piv.loc[["None (baseline)", "RandomOverSampler", "SMOTE", "SMOTE+Tomek"]]
        piv.plot(kind="bar", ax=ax, color=["#2ecc71", "#9b59b6"], edgecolor="black")
        ax.set_title(m, fontweight="bold")
        ax.set_ylim(0.7, 1.0)
        ax.tick_params(axis="x", rotation=15)
        ax.legend(fontsize=8)
        ax.grid(axis="y", alpha=0.3)
    plt.suptitle("Metric comparison across configurations",
                 fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "metrics_comparison.png", dpi=140)
    plt.close()

    # ROC curves
    colors = plt.cm.tab10(np.linspace(0, 1, len(roc_data)))
    plt.figure(figsize=(9, 7))
    for (k, (fpr, tpr, auc)), c in zip(roc_data.items(), colors):
        plt.plot(fpr, tpr, label=f"{k}  (AUC={auc:.3f})", color=c, linewidth=1.6)
    plt.plot([0, 1], [0, 1], "k--", alpha=0.4)
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC curves - all configurations")
    plt.legend(fontsize=8, loc="lower right")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "roc_curves.png", dpi=140)
    plt.close()

    # PR curves
    plt.figure(figsize=(9, 7))
    for (k, (rec, prec, ap)), c in zip(pr_data.items(), colors):
        plt.plot(rec, prec, label=f"{k}  (AP={ap:.3f})", color=c, linewidth=1.6)
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.title("Precision-Recall curves")
    plt.legend(fontsize=8, loc="lower left")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "pr_curves.png", dpi=140)
    plt.close()

    # confusion matrix of best
    best = df_res.sort_values("AUC-PR", ascending=False).iloc[0]
    name = f"{best['Resampling']} | {best['Model']}"
    cm = cms[name]
    plt.figure(figsize=(5.5, 4.5))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
                xticklabels=["Legit", "Fraud"],
                yticklabels=["Legit", "Fraud"])
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title(f"Confusion matrix - best model\n{name}")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "confusion_matrix_best.png", dpi=140)
    plt.close()


# =============================================================================
# 8. MAIN
# =============================================================================
def main():
    print("\n" + "=" * 72)
    print(" CREDIT CARD FRAUD DETECTION - RESAMPLING x ENSEMBLE STUDY ")
    print("=" * 72 + "\n")

    train_raw, test_raw = load_data("fraudTrain.csv", "fraudTest.csv")
    train = feature_engineering(train_raw)
    test  = feature_engineering(test_raw)
    train, test, _ = encode_categoricals(train, test)

    stats = perform_eda(train)
    X_train, y_train, X_test, y_test = prepare_xy(train, test)

    df_res, roc_data, pr_data, cms = run_experiments(
        X_train, y_train, X_test, y_test)

    df_res = df_res[["Resampling", "Model", "Precision", "Recall",
                     "F1", "AUC-ROC", "AUC-PR", "MCC"]]
    df_res.to_csv(OUTPUT_DIR / "results_table.csv", index=False)

    with open(OUTPUT_DIR / "eda_stats.json", "w") as f:
        json.dump(stats, f, indent=2)

    plot_results(df_res, roc_data, pr_data, cms)

    print("\n[RESULTS]\n", df_res.round(4).to_string(index=False))
    print(f"\n[OK] All artifacts saved to {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
