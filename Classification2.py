from xgboost import XGBClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd

data = load_breast_cancer()

X = pd.DataFrame(data.data, columns=data.feature_names)
Y = data.target

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

xgb = XGBClassifier(n_estimators=100, max_depth=4, learning_rate=0.1, random_state=42, eval_metric='logloss', verbosity=0)

xgb.fit(X_train, Y_train)
print(f'XGBoost Accuracy: {accuracy_score(Y_test, xgb.predict(X_test))*100:.2f}%')
# print(f'classification report: {classification_report(Y_test, xgb.predict(X_test), target_names=data.target_names)}')