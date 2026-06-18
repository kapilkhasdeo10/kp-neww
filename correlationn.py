import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from scipy import stats

np.random.seed(42)
study = np.random.uniform(1, 10, 100)
marks = study * 8 + np.random.normal(0, 5, 100) 
marks = np.clip(marks, 30, 100)
absent = 10 - study + np.random.normal(0, 1, 100)
df = pd.DataFrame({'study_hrs': study, 'marks': marks, 'absences': absent})

corr_matrix = df.corr()
print(corr_matrix.round(3))

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()

# Pearson correlation
r, p_value = stats.pearsonr(study, marks)
print(f"Study-Marks Correlation: r = {r:.3f}, p-value = {p_value:.4f}")
print(f"Interpretation: {'Strong positive' if r >= 0.8 else 'Moderate' if r >= 0.5 else 'Weak'}")   