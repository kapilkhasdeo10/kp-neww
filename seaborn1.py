# import numpy as np
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# np.random.seed(0)
# df = pd.DataFrame({
#     'marks': np.random.randint(40, 100, 50),
#     'study_hrs': np.random.uniform(2, 10, 50),
#     'city': np.random.choice(['Bhopal', 'Indore', 'Jabalpur', 'Gwalior', 'Ujjain'], 50),
#     'gender': np.random.choice(['Male', 'Female'], 50)
# })

# plt.figure(figsize=(10, 6))
# sns.histplot(df['marks'], bins=10, kde=True, color='steelblue')
# plt.title('Distribution of Marks')
# plt.xlabel('Marks')
# plt.ylabel('Study Hours')
# plt.grid(True, alpha=0.3)
# plt.show()

# Box Plot - outliers and spread per group
# sns.boxplot(data=df, x='city', y='marks', palette='Set1')
# plt.title('Marks Distribution by City')
# plt.show()

# plt.figure(figsize=(10, 6))
# sns.heatmap(df[['marks', 'study_hrs']].corr(), annot=True, cmap='coolwarm', vmin=-1, vmax=1)
# plt.title('Correlation Heatmap')
# plt.show()

# sns.pairplot(df[['marks', 'study_hrs']], diag_kind='kde')
# plt.show()

