# Telco Customer Churn Prediction  
End-to-End Machine Learning Pipeline using Scikit-learn  

##  Project Overview

This project builds a production-ready Machine Learning pipeline to predict customer churn using the Telco Customer Churn dataset.

The solution demonstrates proper ML engineering practices including:

- Data preprocessing using `ColumnTransformer`
- Feature scaling and encoding inside a unified `Pipeline`
- Model training with Logistic Regression and Random Forest
- Hyperparameter tuning using `GridSearchCV`
- Cross-validation
- Model evaluation (F1-score, ROC-AUC)
- Exporting the final model using `joblib`

The goal is to build a reusable and deployable churn prediction system.

---

##  Dataset

Dataset used:
**Telco Customer Churn Dataset**

Source:
https://www.kaggle.com/datasets/blastchar/telco-customer-churn

- 7,043 customer records
- 21 features
- Target variable: `Churn` (Yes / No)

---

##  Problem Statement

Customer churn prediction helps businesses:

- Identify customers at risk of leaving
- Improve retention strategies
- Increase long-term revenue

This model predicts whether a customer will churn based on service usage, billing, and demographic features.

---

##  Project Structure


---

## 🔬 ML Workflow

### 1️⃣ Data Cleaning
- Dropped `customerID`
- Converted `TotalCharges` to numeric
- Removed missing values
- Encoded target variable

### 2️⃣ Preprocessing Pipeline
- Numerical features → `StandardScaler`
- Categorical features → `OneHotEncoder`
- Combined using `ColumnTransformer`

### 3️⃣ Models Used
- Logistic Regression
- Random Forest Classifier

### 4️⃣ Hyperparameter Tuning
- Performed using `GridSearchCV`
- 5-fold Cross Validation
- Optimized using F1-score

### 5️⃣ Evaluation Metrics
- Classification Report
- ROC-AUC Score

### 6️⃣ Model Export
Final trained pipeline saved using:

```python
joblib.dump(best_model, "churn_pipeline.pkl")

