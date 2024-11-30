# CKD Detection Project

## Overview

This project uses machine learning to predict the likelihood of Chronic Kidney Disease (CKD) based on clinical and laboratory features. The dataset includes critical health metrics like blood pressure, glucose levels, and hemoglobin to identify CKD in individuals.

## Features

- **Preprocessed Dataset**: Optimized dataset with essential features tailored for Chronic Kidney Disease (CKD) prediction.  
- **Multiple Machine Learning Models**: Implementation of models such as K-Nearest Neighbors (KNN), Support Vector Machine (SVM), and XGBoost to ensure robust predictions.  
- **Hyperparameter Optimization**: Automated tuning with `RandomizedSearchCV` for improving model performance and accuracy.  
- **Performance Metrics Visualization**: Confusion matrix, ROC curves, and other evaluation metrics for comprehensive model analysis.  
- **Interactive UI**: User-friendly interface with dynamic visualizations to distinguish between healthy and infected kidneys.

---

## Dataset
[Dataset](/kidney.csv)

### Source
The dataset contains the following features:
- **age**: Age of the patient (numerical)
- **bp**: Blood pressure (numerical)
- **sg**: Specific gravity (categorical)
- **al**: Albumin levels (categorical)
- **bgr**: Blood glucose random (numerical)
- **sc**: Serum creatinine (numerical)
- **hemo**: Hemoglobin levels (numerical)
- **htn**: Hypertension (binary: 1 for yes, 0 for no)
- **dm**: Diabetes mellitus (binary: 1 for yes, 0 for no)
- **ane**: Anemia (binary: 1 for yes, 0 for no)
- **classification**: Target variable (1 for CKD, 0 for not CKD)

---

## Tools & Technologies

- **Python**: Data processing and model implementation.
- **XGBoost**: Main classification algorithm.
- **Matplotlib & Seaborn**: Data visualization and analysis.
- **Pandas**: Data manipulation.
- **Scikit-learn**: Machine learning pipeline and metrics.
- **DALL·E**: Generated images for visualization.

---

## How to Use

### 1. Clone the Repository
```bash
git clone https://github.com/NissanJK/ckd_detection.git
cd ckd_detection
```

### 2. Install Dependencies
Ensure you have Anaconda installed. Then, run:
```bash
conda create -p venv python=3.12 -y
conda activate venv/
```

Ensure you have Python installed. Then, run:
```bash
pip install -r requirements.txt
python app.py
```

### 3. Run the Notebook
Open `class.ipynb` in Jupyter Notebook or VS Code and execute the cells step by step.

### 4. Train and Test Models  

- Train multiple models, including **XGBoost**, **KNN**, and **SVM**, on the preprocessed dataset for comparison.  
- Utilize **hyperparameter tuning** with `RandomizedSearchCV` to optimize performance for the XGBoost model.  
- Evaluate each model's performance using metrics like accuracy, confusion matrix, ROC curves, and classification reports.

---

## Visualization

- **Healthy Kidney**: Showcases a visual representation of a healthy kidney for better understanding.  
  ![Healthy Kidney](static/healthy.webp)  
- **Infected Kidney**: Represents an infected kidney for comparison and clarity.  
  ![Infected Kidney](static/infected.webp)  
- **ROC Curves**:  
  - Displays the trade-off between true positive rate (TPR) and false positive rate (FPR) for various models.  
  - Evaluates the discriminatory power of each classifier.  
- **Feature Importance**:  
  - Highlights key features contributing to predictions.  
  - Provides insights into critical factors influencing CKD detection.  

---

## Performance Metrics

- **Accuracy**: Achieved high accuracy across multiple models, with XGBoost delivering the best results after hyperparameter tuning.  
- **ROC-AUC Score**: Demonstrates the area under the ROC curve for model comparisons.  
- **Classification Report**: Comprehensive metrics including precision, recall, and F1 score for each model.  
- **Confusion Matrix**: Visualized true vs. predicted classifications for KNN, SVM, and XGBoost.  
  - Heatmaps offer clear insights into model performance.  

---

## Future Scope

- Add advanced feature engineering.
- Integrate additional classification models for comparative analysis.
- Deploy the project as a web app using Flask/Django.



