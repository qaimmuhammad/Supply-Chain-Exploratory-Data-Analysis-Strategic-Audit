"""
Project configuration & constants for Supply Chain ML project.

This module centralizes all configuration variables used across
EDA and ML pipelines.
"""

import os
from pathlib import Path

# ============================================================================
# PROJECT PATHS
# ============================================================================

# Root project directory
PROJECT_ROOT = Path(__file__).parent.parent

# Data directories
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Output directories
REPORTS_DIR = PROJECT_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"
MODELS_DIR = PROJECT_ROOT / "models"

# Notebooks
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"
EDA_NOTEBOOKS_DIR = NOTEBOOKS_DIR / "eda"
ML_NOTEBOOKS_DIR = NOTEBOOKS_DIR / "ml"

# Create directories if they don't exist
for dir_path in [PROCESSED_DATA_DIR, REPORTS_DIR, FIGURES_DIR, MODELS_DIR]:
    dir_path.mkdir(parents=True, exist_ok=True)

# ============================================================================
# DATA FILES
# ============================================================================

RAW_DATA_FILE = RAW_DATA_DIR / "supply_chain_data.csv"
PROCESSED_DATA_FILE = PROCESSED_DATA_DIR / "supply_chain_processed.csv"

# ============================================================================
# RANDOM STATE
# ============================================================================

RANDOM_STATE = 42
"""Fixed random state for reproducibility across all models"""

# ============================================================================
# TRAIN-TEST SPLIT
# ============================================================================

TEST_SIZE = 0.2
"""Proportion of data used for testing (80/20 split)"""

CV_FOLDS = 5
"""Number of folds for cross-validation"""

# ============================================================================
# FEATURE GROUPS
# ============================================================================

# Supplier Performance Features
SUPPLIER_FEATURES = [
    'quality_score',
    'supplier_reliability_score',
    'defect_rate',
    'return_rate',
    'price_per_unit'
]

# Delivery Metrics
DELIVERY_FEATURES = [
    'delivery_time_days',
    'on_time_delivery_rate',
    'lead_time_variance',
    'delivery_mode',
    'delivery_term_code'
]

# Demand & Forecast
DEMAND_FEATURES = [
    'forecast_accuracy',
    'seasonality_index',
    'demand_volatility_index',
    'order_frequency_monthly',
    'avg_order_volume'
]

# Procurement
PROCUREMENT_FEATURES = [
    'procurement_action_code',
    'payment_term_days',
    'offer_validity_days',
    'items_requested',
    'items_offered'
]

# Temporal
TEMPORAL_FEATURES = ['temporal_month']

# Target Variable
TARGET_COLUMN = 'selected_supplier_flag'

# All numerical features
NUMERICAL_FEATURES = [
    'quality_score',
    'supplier_reliability_score',
    'defect_rate',
    'return_rate',
    'price_per_unit',
    'delivery_time_days',
    'on_time_delivery_rate',
    'lead_time_variance',
    'forecast_accuracy',
    'seasonality_index',
    'demand_volatility_index',
    'order_frequency_monthly',
    'avg_order_volume',
    'payment_term_days',
    'offer_validity_days',
    'items_requested',
    'items_offered'
]

# All categorical features
CATEGORICAL_FEATURES = [
    'delivery_mode',
    'delivery_term_code',
    'procurement_action_code',
    'temporal_month'
]

# ============================================================================
# ML MODEL PARAMETERS
# ============================================================================

# Linear Regression (Baseline)
LINEAR_REGRESSION_PARAMS = {
    'fit_intercept': True,
    'copy_X': True
}

# Random Forest Regressor (Q1: Delivery Prediction)
RF_REGRESSOR_PARAMS = {
    'n_estimators': 100,
    'random_state': RANDOM_STATE,
    'n_jobs': -1,
    'max_depth': None,
    'min_samples_split': 5,
    'min_samples_leaf': 2,
    'max_features': 'sqrt'
}

# Gradient Boosting Regressor (Q2: Cost Forecasting)
GBR_PARAMS = {
    'n_estimators': 200,
    'learning_rate': 0.05,
    'max_depth': 4,
    'min_samples_split': 5,
    'min_samples_leaf': 2,
    'random_state': RANDOM_STATE,
    'subsample': 0.8,
    'loss': 'squared_error'
}

# Logistic Regression (Q3: Supplier Selection Baseline)
LOGISTIC_REGRESSION_PARAMS = {
    'max_iter': 1000,
    'random_state': RANDOM_STATE,
    'class_weight': 'balanced',
    'solver': 'lbfgs'
}

# Random Forest Classifier (Q3: Supplier Selection)
RF_CLASSIFIER_PARAMS = {
    'n_estimators': 100,
    'random_state': RANDOM_STATE,
    'n_jobs': -1,
    'class_weight': 'balanced',
    'max_depth': None,
    'min_samples_split': 5,
    'min_samples_leaf': 2,
    'max_features': 'sqrt'
}

# Gradient Boosting Classifier (Q4: Defect Risk)
GBC_PARAMS = {
    'n_estimators': 150,
    'learning_rate': 0.1,
    'max_depth': 3,
    'min_samples_split': 5,
    'min_samples_leaf': 2,
    'random_state': RANDOM_STATE,
    'subsample': 0.8,
    'loss': 'log_loss'
}

# ============================================================================
# PREPROCESSING PARAMETERS
# ============================================================================

SCALING_STRATEGY = 'standard'
"""Options: 'standard' (StandardScaler), 'minmax' (MinMaxScaler)"""

HANDLE_MISSING = 'mean'
"""Strategy for handling missing values: 'mean', 'median', 'drop'"""

OUTLIER_METHOD = 'iqr'
"""Method for outlier detection: 'iqr', 'zscore'"""

OUTLIER_IQR_MULTIPLIER = 1.5
"""IQR multiplier for outlier detection (1.5 is standard)"""

# ============================================================================
# EVALUATION METRICS
# ============================================================================

# Regression Metrics
REGRESSION_METRICS = ['mae', 'rmse', 'r2', 'mape']

# Classification Metrics
CLASSIFICATION_METRICS = ['precision', 'recall', 'f1', 'roc_auc']

# ============================================================================
# VISUALIZATION
# ============================================================================

# Plot style
PLOT_STYLE = 'seaborn-v0_8-whitegrid'
"""Matplotlib style for plots"""

# Figure sizes
FIGURE_SIZE_SMALL = (10, 6)
FIGURE_SIZE_MEDIUM = (12, 8)
FIGURE_SIZE_LARGE = (15, 10)

# Color palettes
COLOR_PALETTE = 'husl'
"""Seaborn color palette"""

# ============================================================================
# BUSINESS THRESHOLDS
# ============================================================================

# Delivery Time Error Thresholds (Q1)
DELIVERY_THRESHOLD_ACCEPTABLE = 2  # days
DELIVERY_THRESHOLD_REVIEW = 5  # days
DELIVERY_THRESHOLD_CRITICAL = float('inf')  # > 5 days

# Defect Risk Threshold (Q4)
DEFECT_RISK_THRESHOLD_AGGRESSIVE = None  # Will be computed from F1-max
DEFECT_RISK_THRESHOLD_CONSERVATIVE = None  # Will be computed from precision > 70%

# ============================================================================
# LOGGING & DEBUG
# ============================================================================

LOG_LEVEL = 'INFO'
"""Logging level: 'DEBUG', 'INFO', 'WARNING', 'ERROR'"""

VERBOSE = True
"""Print progress messages during processing"""

# ============================================================================
# ENVIRONMENT
# ============================================================================

# Check if running in development or production
DEBUG_MODE = os.getenv('DEBUG', 'False').lower() == 'true'

# ============================================================================
# FEATURE ENGINEERING
# ============================================================================

# Features to engineer for ML models
ENGINEERED_FEATURES = {
    'fulfillment_ratio': {
        'formula': 'items_offered / (items_requested + 1)',
        'description': 'Supplier capability to fulfill requested items'
    },
    'demand_pressure': {
        'formula': 'demand_volatility_index * seasonality_index',
        'description': 'Combined demand stress signal'
    }
}

# ============================================================================
# DATA VALIDATION
# ============================================================================

# Expected data types
EXPECTED_DTYPES = {
    # Numerical
    'quality_score': 'float64',
    'supplier_reliability_score': 'float64',
    'defect_rate': 'float64',
    'return_rate': 'float64',
    'price_per_unit': 'float64',
    'delivery_time_days': 'int64',
    'on_time_delivery_rate': 'float64',
    'lead_time_variance': 'float64',
    'forecast_accuracy': 'float64',
    'seasonality_index': 'float64',
    'demand_volatility_index': 'float64',
    'order_frequency_monthly': 'int64',
    'avg_order_volume': 'float64',
    'payment_term_days': 'int64',
    'offer_validity_days': 'int64',
    'items_requested': 'int64',
    'items_offered': 'int64',
    # Categorical
    'delivery_mode': 'object',
    'delivery_term_code': 'object',
    'procurement_action_code': 'object',
    'temporal_month': 'int64',
    # Target
    'selected_supplier_flag': 'int64'
}

# Value ranges for validation
VALUE_RANGES = {
    'quality_score': (0, 100),
    'supplier_reliability_score': (0, 100),
    'defect_rate': (0, 1),
    'return_rate': (0, 1),
    'on_time_delivery_rate': (0, 1),
    'forecast_accuracy': (0, 1),
    'seasonality_index': (0, None),  # Can exceed 1
    'demand_volatility_index': (0, None),
    'temporal_month': (1, 12),
    'selected_supplier_flag': (0, 1)
}

# ============================================================================
# VERSION
# ============================================================================

PROJECT_VERSION = '1.0.0'
LAST_UPDATED = 'May 2026'
