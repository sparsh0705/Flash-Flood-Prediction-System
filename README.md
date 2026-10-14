# Flash Flood Prediction System for Hilly Regions

**Hyperlocal • Predictive • Resilient**

A starter prototype for a hyperlocal flash-flood early-warning system designed for vulnerable hilly regions.

## Problem

Existing flood-monitoring systems can provide broad river- or watershed-level information, but vulnerable hill streams, tributaries, and local communities may still lack real-time, location-specific monitoring.

## Proposed Solution

Our system combines:

- Ground sensor data: rainfall intensity, water level, and soil moisture
- Satellite and terrain information
- Machine-learning-based risk prediction
- Citizen and authority alerts

The intended workflow is:

**Ground Sensors + Satellite/Terrain Data → Data Processing & Fusion → XGBoost → Risk Prediction → Alerts**

## Repository Status

This repository is a **starter prototype**. It currently contains a sample dataset and an initial XGBoost training pipeline for demonstrating the ML workflow.

The following components are planned for later development:

- Live IoT sensor integration
- Satellite data ingestion
- Terrain/DEM feature integration
- Real-time backend/API
- Citizen application
- Authority dashboard
- Field testing and calibration

## Project Structure

```text
flash-flood-prediction-system/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   └── sample-data.csv
└── model/
    └── train_xgboost.py
```

## Prototype Features

The starter ML pipeline uses these example inputs:

- `rainfall_intensity_mm_hr`
- `water_level_m`
- `soil_moisture_percent`

The example output is a flood-risk class:

- `Low`
- `Medium`
- `High`

> The included dataset is synthetic demonstration data. It must not be used for real-world flood warnings or safety decisions.

## Getting Started

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd flash-flood-prediction-system
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it and install the dependencies:

```bash
pip install -r requirements.txt
```

### 3. Train the starter model

```bash
python model/train_xgboost.py
```

The script loads the sample data, trains an XGBoost classifier, prints evaluation results, and saves the trained model under `model/artifacts/`.

## Planned System Architecture

1. **Sense** — IoT nodes collect rainfall, water-level, and soil-moisture data.
2. **Fuse** — Ground readings are combined with satellite and terrain features.
3. **Predict** — An XGBoost-based model estimates local flood risk.
4. **Classify** — Risk is represented as Low, Medium, or High.
5. **Act** — Alerts are delivered to citizens and authorities.

## Planned Data Sources

The project design considers satellite/terrain sources such as:

- INSAT-3DR
- NASA GPM/IMERG
- Sentinel-1 SAR
- Copernicus DEM GLO-30

These integrations are **not yet implemented** in this starter repository.

## Future Work

- Collect and validate real field data
- Integrate live sensor nodes
- Add satellite and terrain features
- Tune and validate the prediction model
- Build real-time alert APIs
- Develop citizen and authority interfaces
- Pilot the system in a vulnerable hilly region
- Scale from pilot location to district and state deployments

## Disclaimer

This repository is an early-stage educational/prototype implementation. Predictions produced using the sample data are not validated for emergency management and must not be used as operational flood warnings.
