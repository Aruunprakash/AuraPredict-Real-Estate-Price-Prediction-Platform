# Real-Estate-Price-Prediction

## Data Cleaning

### Step 1: Missing Value Analysis
- Used `isna().sum()` to identify missing values

### Step 2: Missing Value Treatment
- Removed rows with missing values
- Considered median imputation for numerical columns

### Step 3: BHK Extraction
- Extracted BHK count from `size` column

### Step 4: Square Footage Cleaning
- Identified invalid `total_sqft` values
- Converted ranges such as `2100-2850` into numeric values

### Step 5: Dataset Preparation
- Created cleaned dataset for feature engineering

