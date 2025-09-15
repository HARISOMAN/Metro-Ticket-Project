# Data Science Project — Combined Dataset

**Author:** Harisoman K

## Goal
This project combines multiple CSVs into a single cleaned dataset and analyzes stock-like price/volume trends.  
It also demonstrates simple predictive modeling.

## Structure
- `data/raw/` - raw input data (includes combined_data.csv)
- `data/processed/` - cleaned/processed dataset
- `src/` - ETL and helper scripts
- `notebooks/` - EDA, feature engineering, modeling
- `reports/` - figures and summary

## How to run
1. Create a virtual environment and install requirements:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/Mac
   # OR .\.venv\Scripts\Activate.ps1   # Windows PowerShell

   pip install -r requirements.txt
   ```

2. Run ETL to clean and combine data:
   ```bash
   python src/etl_combined.py
   ```

3. Open notebooks:
   ```bash
   jupyter lab
   ```

## Notebooks
1. **01_data_exploration** → EDA, plots, stats
2. **02_feature_engineering** → lag features, rolling averages, returns
3. **03_modeling** → Linear Regression & Random Forest for next-day price prediction

## Output
- Cleaned dataset: `data/processed/cleaned_data.csv`
- Figures: `reports/figures/`
