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

# import csv
# records = [
#     ['Name', 'Age', 'City', 'Marks', 'sub_marks1', 'sub_marks2', 'sub_marks3', 'sub_marks4', 'sub_marks5'],
#     ['kapil', 22, 'Indore', 88, 85, 90, 87, 89, 86],
#     ['lava', 21, 'Indore', 98, 95, 92, 94, 96, 93],
#     ['yash', 23, 'Indore', 81, 78, 80, 79, 82, 80],
#     ['snaha', 22, 'Indore', 89, 86, 88, 87, 90, 89],
#     ['mahesh', 22, 'Indore', 87, 84, 86, 85, 88, 87]
# ]