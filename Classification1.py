from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Decision Tree
dt = DecisionTreeClassifier(max_depth=3, random_state=42)
dt.fit(X_train, y_train)
print(f'Decision Tree Accuracy: {accuracy_score(y_test, dt.predict(X_test))*100:.2f}%')
print(export_text(dt, feature_names=iris.feature_names))

# Visualize Decision Tree
# plt.figure(figsize=(14,6))
# plot_tree(dt, feature_names=iris.feature_names, class_names=iris.target_names, filled=True,rounded=True,fontsize=9)
# plt.title('Decision Tree, Iris classification')
# plt.show()

# Random Forest, multiple trees
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
print(f'Random Forest Accuracy: {accuracy_score(y_test, rf.predict(X_test))*100:.2f}%')

# Feature importance, which inputs matter most?
import pandas as pd
imp = pd.Series(rf.feature_importances_, index=iris.feature_names).sort_values(ascending=False)
imp.plot(kind='bar', color='steelblue')
plt.title('Feature Importance')
plt.tight_layout()
plt.show()

