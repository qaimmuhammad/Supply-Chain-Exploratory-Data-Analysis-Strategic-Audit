# Environment Setup Guide

Complete guide to setting up the Supply Chain ML project environment.

---

## 📋 System Requirements

- **Python:** 3.8 or higher
- **OS:** Windows, macOS, or Linux
- **RAM:** 4 GB minimum (8+ GB recommended)
- **Disk Space:** 2+ GB for dependencies & data
- **Git:** For cloning the repository

---

## 🔧 Installation Methods

### **Method 1: pip (Recommended)**

#### Step 1: Clone Repository
```bash
git clone https://github.com/yourusername/supply-chain-ml.git
cd supply-chain-ml
```

#### Step 2: Create Virtual Environment
```bash
# Create venv
python -m venv venv

# Activate venv
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

#### Step 3: Install Dependencies
```bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

#### Step 4: Verify Installation
```bash
python -c "
import pandas as pd
import numpy as np
import sklearn
import matplotlib
print('✅ All core dependencies installed successfully!')
"
```

#### Step 5: Start Jupyter Lab
```bash
jupyter lab
```

---

### **Method 2: conda (Alternative)**

#### Step 1: Clone Repository
```bash
git clone https://github.com/yourusername/supply-chain-ml.git
cd supply-chain-ml
```

#### Step 2: Create conda Environment
```bash
conda env create -n supply-chain-ml python=3.10
conda activate supply-chain-ml
```

#### Step 3: Install from requirements.txt
```bash
pip install -r requirements.txt
```

#### Step 4: Verify & Launch
```bash
jupyter lab
```

---

## 🚀 Quick Setup (One-Liner)

**For experienced users:**

```bash
git clone https://github.com/yourusername/supply-chain-ml.git && \
cd supply-chain-ml && \
python -m venv venv && \
source venv/bin/activate && \
pip install -r requirements.txt && \
echo "✅ Setup complete! Run: jupyter lab"
```

---

## 📦 Dependency Details

### Core Data Science
- **pandas** — Data manipulation & analysis
- **numpy** — Numerical computing
- **scipy** — Scientific computing

### Machine Learning
- **scikit-learn** — ML models & preprocessing
- **imbalanced-learn** — Handling class imbalance

### Visualization
- **matplotlib** — Static plotting
- **seaborn** — Statistical visualizations
- **plotly** — Interactive plots

### Development
- **jupyter**, **jupyterlab** — Interactive notebooks
- **black** — Code formatting
- **flake8** — Code linting
- **pytest** — Unit testing

### Optional Advanced ML (commented in requirements.txt)
- **xgboost** — Gradient boosting
- **lightgbm** — Light gradient boosting
- **catboost** — Categorical boosting

To install optional dependencies:
```bash
pip install xgboost lightgbm catboost
```

---

## 🔍 Verification Checklist

After installation, verify everything works:

```bash
# 1. Check Python version
python --version  # Should be 3.8+

# 2. Test imports
python -c "import pandas, numpy, sklearn, matplotlib, seaborn; print('✅ Core packages')"

# 3. Test Jupyter
jupyter --version

# 4. List installed packages
pip list | grep -E "pandas|scikit-learn|matplotlib"

# 5. Run tests
pytest tests/ -v
```

---

## 📂 Project Structure After Setup

```
supply-chain-ml/
├── venv/                              # Virtual environment (don't commit)
├── data/
│   ├── raw/
│   │   └── supply_chain_data.csv      # Add your data here
│   └── processed/
├── notebooks/
│   ├── eda/
│   │   ├── 01_supplier_intelligence.ipynb
│   │   ├── 02_demand_readiness.ipynb
│   │   └── 03_cost_quality_efficiency.ipynb
│   └── ml/
│       ├── 01_delivery_prediction.ipynb
│       ├── 02_cost_forecasting.ipynb
│       ├── 03_supplier_selection.ipynb
│       └── 04_defect_risk.ipynb
├── src/
├── tests/
├── reports/
├── docs/
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🗂️ Data Setup

### Add Your Supply Chain Data

```bash
# Create data directory if it doesn't exist
mkdir -p data/raw

# Copy your CSV file
cp /path/to/your/supply_chain_data.csv data/raw/
```

**Expected file structure:**
```
data/
├── raw/
│   └── supply_chain_data.csv          # 22 columns, N rows
└── processed/
    └── (auto-generated from notebooks)
```

---

## 🐍 Troubleshooting

### Issue: `python` command not found

**Windows:**
- Ensure Python is added to PATH during installation
- Use `python --version` instead of `python3`

**macOS/Linux:**
```bash
# If python3 not found, install Python
brew install python3  # macOS
sudo apt-get install python3  # Ubuntu
```

### Issue: Virtual Environment Not Activating

```bash
# Check venv activation script
ls venv/bin/activate       # macOS/Linux
dir venv\Scripts\activate  # Windows

# Try explicit activation
source venv/bin/activate.fish  # Fish shell
```

### Issue: `pip install` Permission Denied

```bash
# Upgrade pip first
python -m pip install --upgrade pip

# Then install with --user flag if needed
pip install --user -r requirements.txt
```

### Issue: Jupyter Not Found After Install

```bash
# Reinstall jupyter
pip uninstall jupyter jupyterlab -y
pip install jupyter jupyterlab

# Or use python -m
python -m jupyter lab
```

### Issue: ImportError for sklearn/pandas

```bash
# Verify installation
pip list | grep -E "scikit-learn|pandas"

# Reinstall if needed
pip install --force-reinstall scikit-learn pandas
```

---

## 🧪 Running Tests

After installation, verify functionality with tests:

```bash
# Install testing dependencies (if not in requirements.txt)
pip install pytest pytest-cov

# Run all tests
pytest tests/ -v

# Run with coverage report
pytest tests/ --cov=src --cov-report=html

# Run specific test file
pytest tests/test_preprocessing.py -v
```

---

## 📝 Environment Variables (Optional)

Create `.env` file in project root for configuration:

```
# .env
DATA_PATH=data/raw/supply_chain_data.csv
OUTPUT_PATH=reports/
LOG_LEVEL=INFO
RANDOM_STATE=42
```

Load in Python:
```python
from dotenv import load_dotenv
import os

load_dotenv()
data_path = os.getenv('DATA_PATH', 'data/raw/supply_chain_data.csv')
```

---

## 🔄 Updating Dependencies

Keep dependencies up-to-date:

```bash
# Check outdated packages
pip list --outdated

# Update all packages
pip install --upgrade -r requirements.txt

# Update single package
pip install --upgrade pandas

# Save updated versions
pip freeze > requirements.txt
```

---

## 🗑️ Cleanup & Uninstall

### Remove Virtual Environment
```bash
# Deactivate first
deactivate

# Remove directory
rm -rf venv           # macOS/Linux
rmdir /s venv         # Windows
```

### Clean Build Artifacts
```bash
rm -rf build/ dist/ *.egg-info __pycache__
find . -type d -name __pycache__ -exec rm -r {} +
```

---

## ✅ Next Steps After Setup

1. **Verify installation** — Run the verification checklist above
2. **Add your data** — Place CSV in `data/raw/`
3. **Start Jupyter** — `jupyter lab`
4. **Run notebooks** — Start with `notebooks/eda/01_supplier_intelligence.ipynb`
5. **Explore output** — Check `reports/` folder for generated figures

---

## 🆘 Getting Help

- **Installation issues:** See Troubleshooting section above
- **Python version issues:** Check with `python --version`
- **Package conflicts:** Try `pip install --upgrade pip` first
- **Still stuck?** Open an [issue on GitHub](https://github.com/yourusername/supply-chain-ml/issues)

---

**Happy analysing!** 🚀
