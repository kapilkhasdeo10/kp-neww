
# 1. Import Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    ConfusionMatrixDisplay
)

from xgboost import XGBClassifier


# 2. Load Dataset

df = pd.read_csv("loan_prediction.csv")

print("First 5 Rows")
print(df.head())

print("Shape")
print(df.shape)

print("Data Types")
print(df.dtypes)

print("Missing Values")
print(df.isnull().sum())

print("Target Distribution")
print(df["Loan_Status"].value_counts())


# 3. Data Cleaning


# Fill missing values
cat_cols = df.select_dtypes(include="object").columns
num_cols = df.select_dtypes(exclude="object").columns

for col in cat_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

for col in num_cols:
    df[col].fillna(df[col].median(), inplace=True)

# Encode categorical variables
encoder = LabelEncoder()

for col in cat_cols:
    df[col] = encoder.fit_transform(df[col])


# 4. Exploratory Data Analysis


# Chart 1
plt.figure(figsize=(6,4))
sns.countplot(x="Loan_Status", data=df)
plt.title("Loan Status Distribution")
plt.show()

# Chart 2
plt.figure(figsize=(7,5))
sns.histplot(df["ApplicantIncome"], bins=30)
plt.title("Applicant Income Distribution")
plt.show()

# Chart 3
plt.figure(figsize=(7,5))
sns.boxplot(x="Education", y="LoanAmount", data=df)
plt.title("Loan Amount by Education")
plt.show()

# Chart 4
plt.figure(figsize=(6,4))
sns.countplot(x="Gender", hue="Loan_Status", data=df)
plt.title("Gender vs Loan Status")
plt.show()

# Chart 5
plt.figure(figsize=(10,8))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()


# 5. Split Dataset

X = df.drop("Loan_Status", axis=1)
y = df["Loan_Status"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)


# 6. Logistic Regression

lr = LogisticRegression(max_iter=1000)
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)


# 7. Random Forest

rf = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)


# 8. XGBoost

xgb = XGBClassifier(
    use_label_encoder=False,
    eval_metric="logloss"
)

xgb.fit(X_train, y_train)
xgb_pred = xgb.predict(X_test)


# 9. Model Comparison

models = {
    "Logistic Regression": lr_pred,
    "Random Forest": rf_pred,
    "XGBoost": xgb_pred
}

print("====== Model Performance =======")

for name, pred in models.items():

    print(name)
    print("Accuracy :", accuracy_score(y_test, pred))
    print("Precision:", precision_score(y_test, pred))
    print("Recall   :", recall_score(y_test, pred))
    print("F1 Score :", f1_score(y_test, pred))
    print("-"*45)


# 10. Confusion Matrices


print("Logistic Regression Confusion Matrix")
ConfusionMatrixDisplay.from_predictions(y_test, lr_pred)
plt.show()

print("Random Forest Confusion Matrix")
ConfusionMatrixDisplay.from_predictions(y_test, rf_pred)
plt.show()

print("XGBoost Confusion Matrix")
ConfusionMatrixDisplay.from_predictions(y_test, xgb_pred)
plt.show()


# 11. Feature Importance

importance = pd.Series(
    rf.feature_importances_,
    index=X.columns
)

importance = importance.sort_values()

plt.figure(figsize=(8,6))
importance.plot(kind="barh")
plt.title("Random Forest Feature Importance")
plt.show()


# 12. Predict New Applicants


new_applicants = pd.DataFrame({

    "Gender":[1,0,1,1,0],
    "Married":[1,1,0,1,0],
    "Dependents":[0,2,1,3,0],
    "Education":[1,1,0,1,0],
    "Self_Employed":[0,1,0,0,1],
    "ApplicantIncome":[5000,8000,3000,12000,4500],
    "CoapplicantIncome":[0,1500,1200,0,800],
    "LoanAmount":[150,220,100,250,130],
    "Loan_Amount_Term":[360,360,180,360,240],
    "Credit_History":[1,1,0,1,1],
    "Property_Area":[2,1,0,2,1]

})

prediction = rf.predict(new_applicants)
probability = rf.predict_proba(new_applicants)

result = new_applicants.copy()

result["Prediction"] = prediction
result["Default Probability"] = probability[:,0]
result["Approval Probability"] = probability[:,1]

print("\nPrediction for New Applicants")
print(result)


print("""
This project implements an end-to-end machine learning pipeline for loan prediction.
The dataset was explored, cleaned by handling missing values, and categorical
variables were encoded using LabelEncoder. Five visualizations were created,
including loan status distribution, applicant income distribution, loan amount
by education, gender vs loan status, and a correlation heatmap.

Three machine learning models—Logistic Regression, Random Forest, and XGBoost—
were trained and evaluated using accuracy, precision, recall, F1-score, and
confusion matrices. Random Forest was also used to determine feature importance,
highlighting the most influential variables in loan approval decisions.

Finally, predictions were generated for five new applicants along with approval
and default probabilities. In most cases, XGBoost provides the highest prediction
accuracy because it effectively captures complex relationships and minimizes
overfitting through boosting. Random Forest offers a good balance between
performance and interpretability, while Logistic Regression serves as a simple
baseline model.
""")