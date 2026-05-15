"""
Supply Chain ML: Exploratory Data Analysis & Predictive Modelling

A comprehensive project for supply chain optimization addressing 7 CEO-level
business questions across 3 strategic pillars (EDA) and 4 predictive models (ML).

Modules:
    - eda: Exploratory data analysis workflows
    - ml: Machine learning pipelines
    - config: Project configuration
    - utils: Utility functions

Version: 1.0.0
Author: Supply Chain ML Team
"""

__version__ = '1.0.0'
__author__ = 'Supply Chain ML Team'
__date__ = 'May 2026'

from .config import (
    PROJECT_ROOT,
    DATA_DIR,
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    RANDOM_STATE,
    NUMERICAL_FEATURES,
    CATEGORICAL_FEATURES,
    TARGET_COLUMN
)

__all__ = [
    'PROJECT_ROOT',
    'DATA_DIR',
    'RAW_DATA_DIR',
    'PROCESSED_DATA_DIR',
    'RANDOM_STATE',
    'NUMERICAL_FEATURES',
    'CATEGORICAL_FEATURES',
    'TARGET_COLUMN'
]
