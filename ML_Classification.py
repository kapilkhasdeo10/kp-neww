import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
import seaborn as sns; import matplotlib.pyplot as plt

# Generate student pass/fail dataset
np.random.seed(42); n=300
study = np.random.uniform(0,10,n)  # Study hours
attend = np.random.uniform(48,100,n)  # Attendance percentage
tasks = np.random.randint(0,11,n)  # Completed tasks
score = study*5 + attend*0.3 + tasks*2 + np.random.normal(0,8,n)  # Overall score
passed = (score >= 65).astype(int)

df =pd.DataFrame({'Study':study,'attend':attend,'tasks':tasks,'passed':passed})
X = df[['Study','attend','tasks']]
Y = df['passed']

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

scaler = StandardScaler()
Xtr = scaler.fit_transform(X_train)
Xte = scaler.transform(X_test)

model = LogisticRegression()
model.fit(Xtr,Y_train)

y_pred = model.predict(Xte)
print(f'Accuracy: {accuracy_score(Y_test,y_pred)*100:.1f}%')
print(classification_report(Y_test,y_pred,target_names=['Fail','Pass']))

# Confusion Matrix
cm = confusion_matrix(Y_test,y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Fail','Pass'], yticklabels=['Fail','Pass'])
plt.title('Confusion Matrix')
plt.show()

# Predict new student
new = scaler.transform([[7,85,9]])
pred = model.predict(new)[0]
prob = model.predict_proba(new)[0]
print(f'Prediction: {"Pass" if pred==1 else "Fail"} (Pass Probability: {prob[1]*100:.1f}%)')