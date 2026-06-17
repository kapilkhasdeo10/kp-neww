# Data plot

# import matplotlib.pyplot as plt

# Months = ['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sep','Oct','Nov','Dec']
# sales = [45,35,55,56,65,75,57,67,85,69,99,81]

# plt.figure(figsize=(12,5))
# plt.plot(Months, sales, marker= 'o', color='steelblue', linewidth=2, markersize=8)
# plt.fill_between(Months, sales, alpha=0.15, color='steelblue')
# plt.title('Monthly Sales 2025 (Rs . Thousand)')
# plt.xlabel('Month')
# plt.ylabel('Sales (Rs . Thousand)')
# plt.grid(True, alpha=0.3)
# plt.tight_layout()
# plt.show()

# # Data Bar
# import matplotlib.pyplot as plt

# Cities = ['Bhopal', 'Indore', 'Jabalpur', 'Gwalior', 'Ujjain']
# students = [762, 1150, 990, 880, 310]
# colors = ['steelblue', 'orange', 'green', 'red', 'purple']

# plt.figure(figsize=(9, 6))
# bars = plt.bar(Cities, students, color=colors, edgecolor='black', linewidth=1.5)
# plt.title('Number of Students in Different Cities (2025)')
# plt.ylabel('Number of Students')
# for bar,val in zip(bars, students):
#     plt.text(bar.get_x() + bar.get_width() / 2, val + 30, str(val), ha='center', fontweight='bold')
# plt.tight_layout()
# plt.show()

import matplotlib.pyplot as plt
import numpy as np

study_hrs = np.random.uniform(2, 10, 50)
marks = study_hrs * 7 + np.random.normal(0, 8, 50)
marks = np.clip(marks, 38, 100)

plt.figure(figsize=(8, 5))
plt.scatter(study_hrs, marks, c=marks, cmap='RdYlGn', s=100, edgecolor='black', linewidth=0.8)
plt.colorbar(label='Marks')
plt.title('Study Hours vs Marks')
plt.xlabel('Study Hours/Day')
plt.ylabel('Exam Marks')
plt.show()