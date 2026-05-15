# Machine Learning Approach & Methodology

Comprehensive guide to the machine learning strategy, model selection, and implementation across all 4 predictive questions.

---

## 🎯 Overview

The ML component extends the EDA insights into a full predictive audit with 4 regression and classification models.

| # | Question | Type | Primary Model | Performance Metric |
|---|----------|------|---------------|--------------------|
| Q1 | Delivery Time | Regression | Random Forest | R², RMSE |
| Q2 | Unit Cost | Regression | Gradient Boosting | R², MAE |
| Q3 | Supplier Selection | Classification | Random Forest | ROC-AUC, F1 |
| Q4 | Defect Risk | Classification | Gradient Boosting | Recall (High-Risk) |

---

## 🚀 Methodology

### **Phase 1: Data Preparation**

#### Objectives
- Clean & validate source data
- Handle missing values
- Detect & manage outliers
- Engineer domain-relevant features

#### Approach
1. **Data Loading** — Validate schema against expected dtypes
2. **Missing Value Analysis** — Document & impute where appropriate
3. **Outlier Detection** — IQR method (1.5× IQR multiplier)
4. **Feature Scaling** — StandardScaler for numerical features
5. **Encoding** — OneHotEncoder for categoricals

#### Decision Rules
- Missing values: **Mean imputation** for numerical, **mode** for categorical
- Outliers: **Retain with documentation** for price_per_unit (business-driven)
- Log transform: Apply if feature shows >1 skewness

---

### **Phase 2: Feature Engineering**

#### Domain-Driven Features

**Q1 & Q2:** Interaction terms
```python
# Not explicitly engineered, but Random Forest & GBR capture interactions
```

**Q2 Specific:** Pricing signals
```python
fulfillment_ratio = items_offered / (items_requested + 1)
demand_pressure = demand_volatility_index × seasonality_index
```

**Q3 & Q4:** All raw features used; let models discover importance

#### Feature Selection Criteria
1. **Business Relevance** — Can the feature logically influence the target?
2. **Availability** — For Q4, only pre-order features (no data leakage)
3. **Correlation** — Weak features removed if R² < 0.01
4. **Redundancy** — Remove if VIF > 5 (multicollinearity)

---

### **Phase 3: Train-Test Split**

#### Strategy
- **80/20 Split** with `random_state=42` for reproducibility
- **Stratified** on target variable (Q3, Q4) to balance classes
- **No data leakage** — preprocessing inside Pipeline

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2, 
    random_state=42,
    stratify=y  # For classification
)
```

---

### **Phase 4: Model Selection**

#### **Q1: Delivery Time Prediction (Regression)**

**Baseline:** LinearRegression
- **Why:** Interpretable lower bound
- **Expected R²:** 0.3–0.5
- **Purpose:** Establish baseline; justify ensemble

**Primary:** RandomForestRegressor
- **Why:** Captures non-linear delivery mode × time interactions
- **Expected R²:** 0.65–0.85
- **Justification:** Delivery time is driven by modal interactions (Air fast, Sea slow)

**Parameters:**
```python
RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1,
    max_depth=None,  # Full depth for flexibility
    min_samples_split=5
)
```

---

#### **Q2: Unit Cost Forecasting (Regression)**

**Model:** GradientBoostingRegressor
- **Why:** Cost is driven by sequential feature interactions (delivery term → quality → price)
- **Expected R²:** 0.60–0.80
- **Justification:** Gradient boosting excels at capturing feature interactions & non-linearities

**Parameters:**
```python
GradientBoostingRegressor(
    n_estimators=200,
    learning_rate=0.05,  # Conservative learning
    max_depth=4,         # Shallow trees for stability
    random_state=42,
    subsample=0.8        # Stochastic boosting
)
```

**Hyperparameter Tuning:**
- Grid search: `n_estimators ∈ {100, 200, 300}`, `max_depth ∈ {3, 4, 5}`
- Select based on cross-validation R² stability

---

#### **Q3: Supplier Selection Prediction (Classification)**

**Baseline:** LogisticRegression
- **Why:** Linear, interpretable, provides baseline AUC
- **Expected ROC-AUC:** 0.65–0.75
- **Class Balance:** Apply `class_weight='balanced'`

**Primary:** RandomForestClassifier
- **Why:** Captures non-linear selection logic (e.g., quality threshold effects)
- **Expected ROC-AUC:** 0.80–0.90
- **Justification:** Selection decisions often have threshold effects (e.g., quality > 80%)

**Parameters:**
```python
RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1,
    class_weight='balanced',  # Handle imbalance
    max_depth=None,
    min_samples_split=5
)
```

---

#### **Q4: Defect Risk Classification (Classification)**

**Model:** GradientBoostingClassifier
- **Why:** Defect risk is cumulative (quality + reliability + delivery stability)
- **Expected ROC-AUC:** 0.75–0.88
- **Optimization:** Maximize recall on high-risk class (false negatives costly)

**Parameters:**
```python
GradientBoostingClassifier(
    n_estimators=150,
    learning_rate=0.1,
    max_depth=3,
    random_state=42,
    subsample=0.8,
    loss='log_loss'
)
```

**Key Decision:** Threshold optimization
- **Aggressive:** Maximize recall (catch more high-risk)
- **Conservative:** Maximize precision at >70% (reduce false alarms)

---

### **Phase 5: Cross-Validation & Stability**

#### Strategy
- **5-Fold Cross-Validation** to assess generalization
- **Stratified K-Fold** for classification (maintain class balance)
- **Report:** Mean ± Std across folds

```python
from sklearn.model_selection import cross_val_score, StratifiedKFold

cv = StratifiedKFold(n_splits=5, random_state=42, shuffle=True)
cv_scores = cross_val_score(model, X_train, y_train, cv=cv, scoring='r2')

print(f"CV R² (mean): {cv_scores.mean():.3f} ± {cv_scores.std():.3f}")
```

#### Interpretation
- **Stable CV:** Mean ≈ Test Score (model generalizes)
- **Unstable CV:** Std > 0.05 (investigate data structure)

---

### **Phase 6: Evaluation & Interpretation**

#### **Regression Metrics**

**MAE (Mean Absolute Error)**
- **Interpretation:** Average prediction error in original units
- **Business Use:** SLA thresholds (Q1), cost forecasting accuracy (Q2)

**RMSE (Root Mean Squared Error)**
- **Interpretation:** Penalizes large errors
- **Business Use:** Model stability assessment

**R² Score**
- **Interpretation:** % variance explained
- **Target:** Q1 > 0.70, Q2 > 0.65

---

#### **Classification Metrics**

**Precision & Recall Trade-off**
- **Precision:** Of predicted positives, how many correct? (minimize false alarms)
- **Recall:** Of actual positives, how many caught? (minimize misses)
- **F1-Score:** Harmonic mean (balanced metric)

**ROC-AUC**
- **Interpretation:** Model discrimination across all thresholds
- **Target:** Q3 > 0.80, Q4 > 0.75

**Confusion Matrix**
- **Visual:** Breakdown of TP, FP, TN, FN
- **Business:** Quantify business cost of each error type

---

### **Phase 7: Feature Importance & Interpretation**

#### For Tree-Based Models (RF, GBR, GBC)

**feature_importances_** (built-in)
```python
importance_df = pd.DataFrame({
    'Feature': feature_names,
    'Importance': model.feature_importances_
}).sort_values('Importance', ascending=False)
```

**Interpretation:**
- Top features = leverage points for business intervention
- E.g., Q1: If `lead_time_variance` dominates → standardize supplier contracts

#### Permutation Importance (Model-Agnostic)
```python
from sklearn.inspection import permutation_importance

perm_imp = permutation_importance(model, X_test, y_test, n_repeats=10)
```

**Advantage:** Works with any model; shows feature contribution after training

#### SHAP (Optional, Advanced)
For detailed interaction analysis:
```python
import shap

explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)
shap.summary_plot(shap_values, X_test)
```

---

## 📊 Model Comparison Strategy

### Baseline vs. Advanced

| Question | Baseline | Primary | Lift Target |
|----------|----------|---------|------------|
| Q1 | Linear Reg (R² ~0.4) | Random Forest (R² ~0.8) | +100% |
| Q2 | Linear Reg (R² ~0.5) | GBR (R² ~0.75) | +50% |
| Q3 | Logistic Reg (AUC ~0.70) | RF (AUC ~0.85) | +21% |
| Q4 | — | GBC (Recall ~0.90) | — |

### Interpretation
- Baseline establishes floor
- Primary model lift = value of non-linear learning
- If lift < 5%, question whether complexity justified

---

## 🔍 Model Validation

### Residual Analysis (Regression)

```python
residuals = y_test - y_pred

# Check 1: Mean ≈ 0 (unbiased)
assert abs(residuals.mean()) < 0.1 * residuals.std()

# Check 2: Homoscedasticity (constant variance)
# Plot residuals vs. predicted → should be random scatter

# Check 3: Normality (especially for inference)
# Histogram of residuals → should be roughly normal
```

### Threshold Optimization (Classification)

For Q4 (Defect Risk):
```python
from sklearn.metrics import precision_recall_curve

precision, recall, thresholds = precision_recall_curve(y_test, y_pred_proba)

# Find F1-maximizing threshold
f1_scores = 2 * (precision * recall) / (precision + recall + 1e-10)
optimal_threshold = thresholds[np.argmax(f1_scores)]

# Find conservative threshold (Precision > 70%)
conservative_idx = np.where(precision > 0.70)[0][0]
conservative_threshold = thresholds[conservative_idx]
```

---

## 🚀 Deployment Considerations

### Model Serialization
```python
import pickle

# Save model
with open('models/delivery_model.pkl', 'wb') as f:
    pickle.dump(pipeline, f)

# Load model
with open('models/delivery_model.pkl', 'rb') as f:
    pipeline = pickle.load(f)
```

### Feature Requirements
- **Input:** Must match training features exactly
- **Preprocessing:** Must use same pipeline (StandardScaler, OneHotEncoder)
- **Monitoring:** Track prediction distribution drift

### Batch Prediction
```python
new_data = pd.read_csv('new_orders.csv')
predictions = pipeline.predict(new_data)
probabilities = pipeline.predict_proba(new_data)  # For classification

# Log results
results_df = new_data.copy()
results_df['prediction'] = predictions
results_df['probability'] = probabilities[:, 1]
results_df.to_csv('predictions.csv', index=False)
```

---

## 📈 Success Criteria

### Business Acceptance
1. **Accuracy:** Model beats manual baseline (80%+ accuracy on heuristics)
2. **Interpretability:** Top 5 features align with domain knowledge
3. **Deployment:** Can run in <1s on new order
4. **Stability:** Performance consistent month-to-month

### Technical Acceptance
1. **Generalization:** Test score ≥ 95% of CV score
2. **Robustness:** Works on new data distributions
3. **Reproducibility:** Same results with `random_state=42`
4. **Documentation:** Code, parameters, decisions all tracked

---

## 🔄 Iteration & Improvement

### If Model Underperforms

**Regression (Q1, Q2):**
1. Check residual plots → non-normal suggests transformation needed
2. Try log-transforming target
3. Engineer new features (interaction terms, ratios)
4. Increase tree depth or ensemble size
5. Consider XGBoost or CatBoost

**Classification (Q3, Q4):**
1. Check class balance → oversample minority if <30:70
2. Tune decision threshold → may improve F1 without retraining
3. Try different `class_weight` strategy
4. Engineer threshold features (e.g., quality > 80)
5. Ensemble multiple models (voting)

### If Model Overfits

**Symptoms:** CV R² >> Test R² (gap > 0.10)

**Fixes:**
1. Increase `min_samples_split`, `min_samples_leaf`
2. Reduce tree depth (`max_depth`)
3. Reduce `n_estimators` or increase `learning_rate`
4. Add regularization (L1/L2 for linear models)
5. Reduce feature count (feature selection)

---

## 📚 References

- **scikit-learn:** https://scikit-learn.org/
- **Model Tuning:** https://scikit-learn.org/stable/modules/grid_search.html
- **Feature Importance:** https://scikit-learn.org/stable/modules/permutation_importance.html
- **Threshold Optimization:** https://en.wikipedia.org/wiki/Precision_and_recall

---

**Last Updated:** May 2026
