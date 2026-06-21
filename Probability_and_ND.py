import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm #Normal Distribution calculator

mean_h, std_h = 170, 10
prob = 1 - norm.cdf(175, mean_h, std_h)


print(f'(Height > 175cm) = {prob:.4f} = {prob*100:.1f}%')

# The 68-95-99.7 Rule
print(f'68% of people: {mean_h - std_h:.0f}cm to {mean_h + std_h:.0f}cm')
print(f'95% of people: {mean_h - 2*std_h:.0f}cm to {mean_h + 2*std_h:.0f}cm')
print(f'99.7% of people: {mean_h - 3*std_h:.0f}cm to {mean_h + 3*std_h:.0f}cm')


from sklearn.model_selection import train_test_split, cross_val_score
import numpy as np

np.random.seed(42)
X = np.random.rand(100, 5)
Y = np.random.randint(0, 2, 100)  # Binary classification labels

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42, stratify=Y
)

print(f'Training samples: {len(X_train)} | Test samples: {len(X_test)}')

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
cv_scores = cross_val_score(model, X, Y, cv=5, scoring='accuracy')
print(f'CV Scores each fold: {cv_scores.round(3)}')
print(f'Mean: {cv_scores.mean():.4f} ± {cv_scores.std():.4f}')


