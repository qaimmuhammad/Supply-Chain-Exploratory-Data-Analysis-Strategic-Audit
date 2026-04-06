# Supply Chain EDA: Strategic Audit & Analysis

A comprehensive **Exploratory Data Analysis (EDA)** project investigating three critical business questions across supply chain operations. This analysis transforms raw procurement, logistics, and delivery data into actionable strategic insights for executive decision-making.

---

## 📋 Overview

This project applies a structured three-pillar analytical framework to real-world supply chain operations spanning **22 features** across logistics and manufacturing industries.

**Dataset:** 3,090 supplier transactions | **Duration:** 12-month period | **Scope:** Procurement, quality, delivery, and demand patterns

**Key Output:** Three boardroom-ready strategic reports with visualizations and statistical analysis.

---

## 🎯 The 3 CEO Strategic Questions

### **Question 1: Supplier Intelligence** ✓ [`eda_q1.ipynb`](eda_q1.ipynb)
**"Are we selecting the right suppliers, or just the available ones?"**

Do our chosen suppliers actually outperform the rest in quality, reliability, and cost efficiency?

**6-Step Analysis:**
1. Supplier selection ratio baseline
2. Quality & reliability head-to-head comparison (quality_score, supplier_reliability_score, defect_rate, return_rate)
3. Price justification analysis
4. Delivery behavior across selected vs. non-selected groups
5. Procurement action correlation study
6. Executive summary scorecard

**Key Deliverable:** Supplier Performance Scorecard Table

---

### **Question 2: Demand Readiness** ✓ [`eda_q2.ipynb`](eda_q2.ipynb)
**"Is our demand unpredictability silently breaking our supply chain?"**

During high-volatility months, does demand forecasting collapse and drag delivery performance with it?

**7-Step Analysis:**
1. Year-round volatility mapping (temporal_month vs. demand_volatility_index)
2. Seasonality vs. volatility layering (dual-axis analysis)
3. Forecast accuracy under pressure (scatter + correlation)
4. Volume behavior during volatile months
5. Delivery consequences of demand chaos (heatmap analysis)
6. Volatility distribution deep dive
7. Month-by-month narrative summary

**Key Deliverable:** Seasonal Intelligence Report Table (12 months × 5 metrics)

---

### **Question 3: Cost-Quality Efficiency** ✓ [`eda_q3.ipynb`](eda_q3.ipynb)
**"Are we paying a quality premium — or just paying a premium?"**

Does higher price per unit actually buy better quality and fewer defects, or are we overspending for no gain?

**7-Step Analysis:**
1. Price distribution analysis (histogram + box plot)
2. Price vs. quality correlation (scatter + regression)
3. Price vs. defect rate relationship
4. Price bucket segmentation (Low / Medium / High / Premium)
5. Procurement action & pricing strategy analysis
6. Return rate as ultimate quality verdict
7. Comprehensive correlation heatmap (5×5 matrix)

**Key Deliverable:** Price-Quality Correlation Heatmap

---

## 📊 Dataset Features (22 Columns)

| Category | Features |
|----------|----------|
| **Pricing & Cost** | price_per_unit |
| **Quality Metrics** | quality_score, defect_rate, return_rate, supplier_reliability_score |
| **Delivery Performance** | delivery_time_days, on_time_delivery_rate, lead_time_variance, delivery_mode, delivery_term_code |
| **Demand & Forecasting** | demand_volatility_index, forecast_accuracy, seasonality_index, order_frequency_monthly, avg_order_volume |
| **Procurement** | procurement_action_code, payment_term_days, offer_validity_days, items_requested, items_offered |
| **Temporal** | temporal_month |
| **Target Variable** | selected_supplier_flag (1 = selected, 0 = not selected) |

---

## 🛠️ Technology Stack

- **Language:** Python 3.x
- **Core Libraries:**
  - `pandas` — Data manipulation and analysis
  - `numpy` — Numerical computations
  - `matplotlib` — Static visualizations
  - Additional utilities: `calendar` (temporal analysis)

---

## 📁 Project Structure

```
supply-chain-eda-strategic-audit/
├── README.md                    # This file
├── dataset.csv                  # 3,090 transactions × 22 features
├── eda_q1.ipynb                 # Supplier Intelligence Analysis
├── eda_q2.ipynb                 # Demand Readiness Analysis
├── eda_q3.ipynb                 # Cost-Quality Efficiency Analysis
└── outputs/
    ├── q1_supplier_scorecard.csv
    ├── q2_seasonal_summary.csv
    └── q3_correlation_matrix.png
```

---

## 🚀 Quick Start

### Prerequisites
```bash
pip install pandas numpy matplotlib
```

### Running the Analysis

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/supply-chain-eda-strategic-audit.git
   cd supply-chain-eda-strategic-audit
   ```

2. **Run individual analyses:**
   ```bash
   jupyter notebook eda_q1.ipynb
   jupyter notebook eda_q2.ipynb
   jupyter notebook eda_q3.ipynb
   ```

3. **Execute all analyses in sequence:**
   ```bash
   python run_all_analyses.py  # (if batch script available)
   ```

---

## 📈 Key Findings Structure

Each notebook follows a consistent pattern:

### **Step Workflow:**
1. **Data Preparation** — Load, validate, and prepare specific features
2. **Statistical Analysis** — Calculate means, correlations, distributions
3. **Visualization** — Generate publication-quality charts
4. **Interpretation** — Translate findings into business implications
5. **Actionable Insights** — Board-ready recommendations

### **Output Format:**
- **Visualizations:** Histograms, scatter plots, box plots, heatmaps, line charts
- **Summary Tables:** Styled pandas DataFrames with grouped metrics
- **Correlation Coefficients:** Pearson r-values with statistical significance
- **Annotated Charts:** Key findings directly labeled on visualizations

---

## 📊 Analysis Highlights

### **Q1 — Supplier Intelligence**
- **Key Metric:** Supplier Performance Scorecard comparing selected vs. non-selected suppliers across 4 quality dimensions
- **Critical Question:** Is selection driven by measurable performance or arbitrary choice?
- **Use Case:** Procurement strategy validation and supplier rationalization

### **Q2 — Demand Readiness**
- **Key Metric:** Month-by-month volatility, forecast accuracy, and on-time delivery correlation
- **Critical Question:** Are high-volatility months destroying forecast accuracy and on-time delivery?
- **Use Case:** Demand planning improvement and safety stock optimization

### **Q3 — Cost-Quality Efficiency**
- **Key Metric:** 5×5 correlation heatmap linking price to quality across all dimensions
- **Critical Question:** Does paying premium prices actually deliver premium quality?
- **Use Case:** Procurement budget reallocation and vendor consolidation

---

## 🎓 Methodology

### **Statistical Techniques Used:**
- Pearson correlation coefficient (linear relationships)
- Grouped aggregation and comparison analysis
- Distribution analysis (histogram + KDE)
- Box plots for outlier detection
- Regression trend lines for trend analysis
- Heatmap correlation matrices
- Dual-axis time series analysis

### **Data Quality Checks:**
- Missing value validation
- Outlier flagging in price and performance metrics
- Supplier selection ratio verification
- Temporal coverage confirmation (12 months)

---

## 💡 How to Use This Project

### **For Data Analysts:**
- Use as a template for supply chain EDA projects
- Adapt the three-question framework to your dataset
- Reference the statistical techniques and visualization patterns

### **For Supply Chain Managers:**
- Review individual notebooks for operational insights
- Use summary tables for supplier performance reviews
- Cross-reference demand volatility with procurement planning

### **For Executives:**
- Focus on the final summary table in each notebook
- Reference the correlation heatmaps for strategic decisions
- Use findings to justify procurement policy changes

---

## 📝 Key Takeaways per Question

| Question | Key Finding Output | Executive Action |
|----------|-------------------|------------------|
| **Q1** | Supplier Scorecard | Validate/revise supplier selection criteria |
| **Q2** | Seasonal Summary Table | Adjust demand planning by volatility month |
| **Q3** | Correlation Heatmap | Optimize procurement budget allocation |

---

## 🔧 Customization & Extension

To adapt this project to your dataset:

1. **Replace `dataset.csv`** with your supply chain data
2. **Update column mappings** in the first cell of each notebook
3. **Adjust price buckets** in Q3 based on your cost distribution
4. **Modify temporal_month** handling for different period definitions

---

## 📚 Dataset Citation

**Dataset Source:** Real-world supply chain operations across logistics and manufacturing industries

**Fields:** 22 features spanning supplier performance, delivery metrics, demand forecasting, and procurement decisions

**Size:** 3,090 transactions over 12 months

---

## 🤝 Contributing

Contributions welcome! To improve this analysis:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Add enhancements to notebooks or analysis methodology
4. Submit a pull request

### **Suggested Improvements:**
- Add interactive Plotly visualizations
- Implement predictive modeling for demand forecasting
- Create a dashboard for real-time supplier monitoring
- Add machine learning classification for supplier selection

---

## 📄 License

This project is provided as-is for educational and business intelligence purposes.

---

## 👤 Author

**Supply Chain Analytics Team**  
*Data-Driven Procurement & Operations Strategy*

---

## 📧 Questions or Feedback?

For questions about the analysis framework, methodology, or results interpretation, refer to the individual notebooks or review the original PDF specification: `Supply_Chain_EDA_Report.pdf`

---

## 📎 Quick Reference

| Notebook | Question | Output | Use Case |
|----------|----------|--------|----------|
| `eda_q1.ipynb` | Supplier Selection | Performance Scorecard | Vendor strategy |
| `eda_q2.ipynb` | Demand Volatility | Seasonal Summary | Demand planning |
| `eda_q3.ipynb` | Price-Quality | Correlation Matrix | Cost optimization |

---

**Last Updated:** 2026  
**Status:** Production-Ready | **Audience:** Executive & Analytical Teams