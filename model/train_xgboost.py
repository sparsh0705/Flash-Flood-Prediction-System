"""Starter XGBoost model for the Flash Flood Prediction System.

This is a demonstration pipeline using synthetic sample data.
It is NOT validated for real-world flood warning or safety decisions.
"""

from pathlib import Path

import joblib
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier


BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = BASE_DIR / "data" / "sample-data.csv"
ARTIFACT_DIR = BASE_DIR / "model" / "artifacts"

FEATURES = [
    "rainfall_intensity_mm_hr",
    "water_level_m",
    "soil_moisture_percent",
]
TARGET = "risk_level"


def main():
    data = pd.read_csv(DATA_PATH)

    X = data[FEATURES]
    y_text = data[TARGET]

    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(y_text)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=42,
        stratify=y,
    )

    model = XGBClassifier(
        n_estimators=100,
        max_depth=3,
        learning_rate=0.08,
        subsample=0.9,
        colsample_bytree=0.9,
        objective="multi:softprob",
        eval_metric="mlogloss",
        random_state=42,
    )

    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    print("Classes:", list(label_encoder.classes_))
    print("\nConfusion matrix:")
    print(confusion_matrix(y_test, predictions))
    print("\nClassification report:")
    print(
        classification_report(
            y_test,
            predictions,
            target_names=label_encoder.classes_,
            zero_division=0,
        )
    )

    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, ARTIFACT_DIR / "xgboost_flood_risk.joblib")
    joblib.dump(label_encoder, ARTIFACT_DIR / "risk_label_encoder.joblib")

    example = pd.DataFrame(
        [{
            "rainfall_intensity_mm_hr": 72.0,
            "water_level_m": 2.4,
            "soil_moisture_percent": 86.0,
        }]
    )
    encoded_prediction = model.predict(example)[0]
    risk = label_encoder.inverse_transform([encoded_prediction])[0]
    print(f"\nExample prototype prediction: {risk}")
    print("\nModel artifacts saved to:", ARTIFACT_DIR)


if __name__ == "__main__":
    main()
