# Capstone Project - Step 7: Experiment With Various Models

This notebook documents Step 7 of the Machine Learning Engineering & AI Bootcamp Capstone Project, focused on evaluating and selecting the best model for a classification problem using rigorous experimentation, cross-validation, and ensemble techniques.

---

## 📌 Objective

- Automate testing of multiple machine learning models.
- Select and justify performance metrics.
- Apply robust cross-validation.
- Perform hyperparameter tuning.
- Identify and mitigate overfitting/underfitting.
- Build ensemble models to improve prediction.
- Document and present the best-performing model.

---

## 📊 Dataset

- **Dataset Used**: Breast Cancer Wisconsin Diagnostic Dataset (from `sklearn.datasets`)
- **Target Variable**: `malignant` vs `benign`

---

## 🧠 Models Evaluated

- Logistic Regression
- Random Forest Classifier
- Support Vector Classifier (SVC)
- Gradient Boosting (optional)
- Voting Classifier (Soft Voting Ensemble of top 3 models)

---

## 🎯 Performance Metrics

- **Accuracy**
- **ROC AUC Score**
- Confusion Matrix
- Classification Report

---

## 🧪 Cross-Validation and Tuning

- 5-Fold Stratified Cross-Validation
- GridSearchCV for hyperparameter tuning:
  - Logistic Regression (`C`)
  - Random Forest (`n_estimators`)
  - SVC (`C`)

---

## 🏆 Best Model

| Metric             | Value              |
|--------------------|--------------------|
| Model              | Voting Classifier  |
| Accuracy           | ~97.37%            |
| ROC AUC            | ~0.997             |
| Training Time      | ~Measured and reported |
| Model Size         | ~Measured and reported |
| Best Params        | Listed in notebook |

---

## 📈 Visualizations

- Confusion Matrix
- ROC Curve

---

## 🗃️ File Structure

```
📁 Capstone_Step7_Model_Experimentation_Enhanced.ipynb
📄 best_ensemble_model.pkl
📄 README.md
```

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
jupyter notebook Capstone_Step7_Model_Experimentation_Enhanced.ipynb
```

---

## ✅ Submission Notes

- [x] Multiple models tested
- [x] Automated training pipeline
- [x] Hyperparameter tuning performed
- [x] Cross-validation applied
- [x] Ensemble model evaluated
- [x] Visual and tabular results shared
- [x] Final model saved and exported

---

## 📌 Author

This project was completed as part of the Machine Learning Engineering & AI Bootcamp Capstone by [Your Name].
