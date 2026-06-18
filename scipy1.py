# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from scipy import stats

# # Employee salaries (in thousands Rs.)
# salaries = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140]

# # Central Tendency Measures - Where is the 'centre' of the data?
# mean_salary = np.mean(salaries)
# median_salary = np.median(salaries)
# mode_salary = stats.mode(salaries,keepdims=True).mode[0]

# print(f"Mean (Average):                   Rs.{mean_salary: .1f}K")
# print(f"Median: (Middle Value)            Rs.{median_salary: .1f}K")
# print(f"Mode:  (Most Common Value)        Rs.{mode_salary: .1f}K")


# # Spread - how varied is the data?
# std = np.std(salaries)
# var = np.var(salaries)
# rng = max(salaries) - min(salaries)
# q1 = np.percentile(salaries, 25) 
# q3 = np.percentile(salaries, 75)
# iqr = q3 - q1

# print(f'Std Deviation: {std:.2f}K (most important spread measure)')
# print(f'IQR {iqr}K (Q1={q1}, Q3={q3}')


# # Outliers detection using IQR
# lower = q1 - 1.5 * iqr
# upper = q3 + 1.5 * iqr
# outliers = [x for x in salaries if x < lower or x > upper]
# print(f'Outliers: {outliers}')


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from scipy import stats

# data = {
#     'name': np.random.choice(['Gangadhar','Bhupinder','Katappa','Mogembo','Gabbar','Shakha','Sambha','Thanos','Modi','Hidimba',
#                 'Putna','Surpankha','None'],25),

#     'age': np.random.randint(18,24,25).astype(float),
    
#     'city': np.random.choice(['Nusantara','Melbourne','Seoul','Manila','Bangkok','Hanoi','Beijing','Sydney','Canberra','None'],25),

#     'math_marks': np.random.randint(30,100,25).astype(float),
#     'chemistry_marks': np.random.randint(30,100,25).astype(float),
#     'hindi_marks': np.random.randint(30,100,25).astype(float),
#     'english_marks': np.random.randint(30,100,25).astype(float),
#     'physics_marks': np.random.randint(30,100,25).astype(float)
# }

# df = pd.DataFrame(data)

# df.loc[np.random.choice(df.index,5), 'name'] = np.nan
# df.loc[np.random.choice(df.index,3), 'age'] = np.nan
# df.loc[np.random.choice(df.index, 2), 'city'] = np.nan
# df.loc[np.random.choice(df.index, 4), 'math_marks'] = np.nan
# df.loc[np.random.choice(df.index, 2), 'chemistry_marks'] = np.nan
# df.loc[np.random.choice(df.index, 3), 'english_marks'] = np.nan

# df.to_csv('students_25.csv', index=False)
# df2 = pd.read_csv('students_25.csv')

# print('Missing Values\n')
# print(df2.isnull().sum())

# np.random.seed(42)
# study = np.random.uniform(1, 10, 100)
# marks = study * 8 + np.random.normal(0, 5, 100) 
# marks = np.clip(marks, 30, 100)
# absent = 10 - study + np.random.normal(0, 1, 100)
# df = pd.DataFrame({'study_hrs': study, 'marks': marks, 'absences': absent})

# corr_matrix = df.corr()
# print(corr_matrix.round(3))

# plt.figure(figsize=(8, 6))
# sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, fmt='.2f')
# plt.title('Correlation Heatmap')
# plt.show()

# # Pearson correlation
# r, p_value = stats.pearsonr(study, marks)
# print(f"Study-Marks Correlation: r = {r:.3f}, p-value = {p_value:.4f}")
# print(f"Interpretation: {'Strong positive' if r >= 0.8 else 'Moderate' if r >= 0.5 else 'Weak'}")

